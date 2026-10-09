"""Valida plantillas y soluciones con kernels nuevos, sin modificar las respuestas del alumno."""
from pathlib import Path
import base64, copy, json, re, sys, traceback
import nbformat
from IPython.utils.capture import capture_output
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
answers = json.loads((ROOT / 'instructor/soluciones.json').read_text())
report = []

def verify_embedded_assets(book):
    """Las imágenes del archivo individual deben coincidir con sus PNG del paquete."""
    count = 0
    for cell in book.cells:
        if cell.cell_type != 'markdown': continue
        assert 'attachment:' not in cell.source, 'Recurso attachment: sin conversión para Colab'
        asset = cell.metadata.get('asset_path')
        if not asset: continue
        images = re.findall(r'!\[[^\]]*\]\(data:image/png;base64,([A-Za-z0-9+/=]+)\)', cell.source)
        assert len(images) == 1, ('Imagen incrustada ausente o duplicada', asset)
        path = (ROOT / asset).resolve()
        assert path.is_relative_to(ROOT) and path.is_file(), asset
        assert base64.b64decode(images[0], validate=True) == path.read_bytes(), asset
        count += 1
    assert count == 2, 'Cada notebook debe incluir encabezado e ilustración'
    return count

def execute(book):
    if '--in-process' not in sys.argv:
        return NotebookClient(book, timeout=120, kernel_name='python3',
                              resources={'metadata': {'path': str(ROOT)}}).execute()
    # An actual in-process IPython kernel needs no network sockets. Use this
    # explicit option in managed environments which disable socket binding.
    from ipykernel.inprocess.manager import InProcessKernelManager
    manager = InProcessKernelManager()
    manager.start_kernel()
    shell = manager.kernel.shell
    shell.reset(new_session=True)
    shell.run_line_magic('matplotlib','inline')
    count = 0
    try:
        for cell in book.cells:
            if cell.cell_type != 'code': continue
            count += 1
            with capture_output() as captured:
                result = shell.run_cell(cell.source, store_history=True)
            if result.error_before_exec or result.error_in_exec:
                raise RuntimeError(f'Celda {count}: '+''.join(traceback.format_exception(result.error_before_exec or result.error_in_exec)))
            cell.execution_count=count
            outputs=[]
            if captured.stdout: outputs.append(nbformat.v4.new_output('stream',name='stdout',text=captured.stdout))
            if captured.stderr: outputs.append(nbformat.v4.new_output('stream',name='stderr',text=captured.stderr))
            outputs += [nbformat.v4.new_output('display_data',data=o.data,metadata=o.metadata) for o in captured.outputs]
            cell.outputs=outputs
    finally:
        manager.shutdown_kernel()
    return book

def strip_widgets(book):
    book.metadata.pop('widgets', None)
    for cell in book.cells:
        if cell.cell_type == 'code':
            clean = []
            interactive = 'interactive' in cell.metadata.get('tags', [])
            for out in cell.get('outputs', []):
                if interactive and out.output_type in ('display_data','execute_result'): continue
                if out.output_type in ('display_data','execute_result'):
                    out.get('data', {}).pop('application/vnd.jupyter.widget-view+json', None)
                    if 'text/plain' in out.get('data', {}) and str(out.data['text/plain']).startswith('interactive('):
                        continue
                    if not out.get('data'): continue
                clean.append(out)
            cell.outputs = clean

for path in sorted((ROOT/'notebooks').glob('*.ipynb')):
    book = nbformat.read(path, as_version=4)
    nbformat.validate(book)
    embedded_images = verify_embedded_assets(book)
    lab = path.name[:2]
    # Keep timers and answer keys out of student content.
    markdown = '\n'.join(c.source for c in book.cells if c.cell_type=='markdown')
    assert not re.search(r'\b(180 minutos|60 minutos|duración de la clase|guía del instructor)\b',markdown,re.I)
    assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',markdown), 'Escape LaTeX dañado'
    template = execute(copy.deepcopy(book))
    solved = copy.deepcopy(book)
    exercise_count = 0
    for cell in solved.cells:
        tags = cell.metadata.get('tags', [])
        if 'exercise' not in tags: continue
        identifier = next(t for t in tags if t in answers[lab])
        solution = answers[lab][identifier]
        cell.source = (solution if lab=='02' else cell.source.replace('None', solution, 1))
        exercise_count += 1
    # Add checks which test physical invariants and numerical outcomes.
    if lab == '01':
        check = '''assert total_mision_min == 120
assert total_mision_h == 2 and restante_min == 30 and alcanza
assert promedio_min == 45
print("VERIFICACIÓN: correcta")'''
    else:
        check = '''assert np.isclose(radar_w(120e3)/radar_w(60e3), 1/16)
assert np.isclose(radar_w(60e3, pico_kw=100)/radar_w(60e3), 2)
assert np.isclose(radar_w(60e3, ganancia_dbi=33)/radar_w(60e3), 10**0.6)
assert np.isclose(patron_ula(np.array([0.0]))[0], 1)
assert np.isclose(patron_ula(np.array([np.arcsin(2/16)]))[0], 0, atol=1e-14)
assert np.isclose(patron_ula(np.array([np.deg2rad(20)]), 16, 20)[0], 1)
assert np.allclose(np.sin(2*np.pi*7*tiempos), np.sin(-2*np.pi*3*tiempos))
assert np.isclose(psr_km, ac_km) and np.isclose(ac_km, s_km)
assert np.isclose(margen_db, 10.78909794185924, atol=1e-5)
assert 0 < ruta_pct < par_pct < 100
for identifier, values in [("Q01",[r_ohm,caida_v,carga_v,perdida_w]),
 ("Q02",[i_a,nominal_wh,autonomia_h]),("Q03",[periodo_us,duty,media_w,b_mhz]),
 ("Q04",[fspl,sensibilidad,pr_dbm,margen_db]),("Q05",[horizonte,radio,despeje]),
 ("Q06",[reflexion,vswr,reflejada_pct,polar_db]),("Q07",[ts_us,niveles,paso_mv,sqnr_db]),
 ("Q08",[duracion_us]),("Q09",[psr_km,ac_km,s_km]),("Q10",[camino_m]),
 ("Q11",[latencia_ms,plr_pct]),("Q12",[ruta_pct,par_pct])]:
    assert all(np.isfinite(v) for v in values), identifier
# Exercise alternative controls and fallback calls; numeric models must remain finite.
for n, direction in [(8,-30),(32,30)]:
    p = patron_ula(np.linspace(-np.pi,np.pi,501),n,direction)
    assert np.all(p>=0) and np.all(p<=1+1e-12)
    dibujar_antena(n,direction)
dibujar_radar(100,40,1)
if 'control_antena' in globals():
    control_antena.children[0].value = 8
    control_antena.children[1].value = 20
    assert control_antena.kwargs['elementos'] == 8
    assert control_antena.kwargs['direccion_deg'] == 20
if 'control_radar' in globals():
    control_radar.children[0].value = 100
    assert control_radar.kwargs['pico_kw'] == 100
print("VERIFICACIÓN: correcta")'''
    solved.cells.append(nbformat.v4.new_code_cell(check))
    solved = execute(solved)
    streams = '\n'.join(o.get('text','') for c in solved.cells for o in c.get('outputs',[]) if o.output_type=='stream')
    assert 'revisa' not in streams and 'VERIFICACIÓN: correcta' in streams
    # Compare every exercise stdout with the printed reference, not just finite values.
    for index, cell in enumerate(solved.cells):
        if 'exercise' not in cell.metadata.get('tags',[]): continue
        previous = solved.cells[index-1].source
        expected = previous.split('```text\n')[1].split('\n```')[0]
        actual = ''.join(o.get('text','') for o in cell.outputs if o.output_type=='stream').strip()
        assert actual == expected, (cell.metadata.tags, actual, expected)
    strip_widgets(template)
    # Publish template code with static outputs; never publish the filled version.
    nbformat.validate(template); nbformat.write(template,path)
    # Export exact figures, computed by Python, for README/teacher preview.
    fig_count=0
    for cell in template.cells:
        for out in cell.get('outputs',[]):
            png = out.get('data',{}).get('image/png')
            if png:
                fig_count+=1
                (ROOT/'assets'/f'lab{lab}_fig{fig_count:02d}.png').write_bytes(base64.b64decode(png))
    report.append({'notebook':path.name,'cells':len(book.cells),'exercises':exercise_count,
                   'student_words':len(re.sub(r'data:image/png;base64,[A-Za-z0-9+/=]+', '', markdown).split()),'figures':fig_count,
                   'embedded_markdown_images':embedded_images,
                   'ai_illustrations':sum(c.metadata.get('image_origin') == 'imagegen' for c in book.cells),
                   'embedded_assets':'PASS',
                   'template_clean_kernel':'PASS','solutions_clean_kernel':'PASS',
                   'execution_mode':'in-process kernel' if '--in-process' in sys.argv else 'Jupyter subprocess kernel',
                   'all_exercise_stdout':'PASS','widgets_browser_tested':False})
(ROOT/'docs/verificacion.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
