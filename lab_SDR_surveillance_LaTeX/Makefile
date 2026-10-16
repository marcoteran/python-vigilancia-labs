TEX = xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build
DOCS = laboratorio_sdr_surveillance:main.tex anexo_a_fundamentos_sdr:anexo_a.tex anexo_b_evaluacion_sdr:anexo_b.tex guia_instructor_sdr:guia_instructor.tex

.PHONY: all verificar clean
# Los cuatro documentos se citan entre sí: tres rondas completas.
all:
	mkdir -p build
	for r in 1 2 3; do for d in $(DOCS); do $(TEX) -jobname=$${d%%:*} $${d##*:} || exit 1; done; done
	for d in $(DOCS); do cp build/$${d%%:*}.pdf $${d%%:*}.pdf; done

verificar:
	cd datos_adsb && sha256sum -c SHA256SUMS
	python3 herramientas/adsb_iq.py verificar datos_adsb/modes1_dump1090_2MSps_1090MHz.sdriq

clean:
	rm -rf build
