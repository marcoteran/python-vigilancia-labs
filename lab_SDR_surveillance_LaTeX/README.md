# Laboratorio SDR · Del espectro RF a la información aeronáutica

Manual universitario de cinco prácticas con **HackRF One**, **SDRangel**, **GNU Radio Companion** y un analizador de espectro **SIGLENT SSA3032X Plus**. Es el complemento con hardware de los dos notebooks de Python de este repositorio.

**[Abrir el PDF](laboratorio_sdr_surveillance.pdf)** · versión 1.2 · 41 páginas · autor: Marco Teran

## Las cinco prácticas

| # | Sistema | Práctica | Qué se obtiene |
|---|---|---|---|
| 1 | Windows | SDRangel: recepción FM y AM | Audio demodulado; diferencia entre dispositivo, canal, offset y ancho de banda |
| 2 | Windows | SDRangel: transmisión FM **conducida** | Espectro WFM en el SIGLENT con tono de 1 kHz y micrófono |
| 3 | Windows | GNU Radio: transmisor FM **conducido** | Flowgraph propio; relación entre tasas de audio, cuadratura y HackRF |
| 4 | Ubuntu | Wi-Fi/OFDM y BLE con GNU Radio, `gr-ieee802-11` y Wireshark | Correlación SSID–BSSID–canal–RF y tramas MAC decodificadas cuando es posible |
| 5 | Ubuntu | ADS-B/Mode S con SDRangel | Tabla de aeronaves, mapa, estadísticas, cobertura y separación entre datos radiados y externos |

## Antes de asignarlo

- **No es requisito de los notebooks**, y los notebooks no bastan como preparación: además se necesita instalar software en Windows y Ubuntu, usar una terminal y manejar hardware RF.
- **Seguridad RF:** las prácticas 2 y 3 transmiten **solo por conexión conducida**: HackRF → atenuador de 30–60 dB → SIGLENT, con RF Amp apagado, ganancia baja y la transmisión detenida antes de tocar cualquier conexión. Nunca se transmite por antena.
- **Privacidad:** la práctica 4 es solo de recepción, limitada a tramas de gestión difundidas abiertamente, con PCAP tratados como datos sensibles y direcciones MAC ajenas enmascaradas.
- **Estado de validación:** el PDF se compiló sin errores ni referencias pendientes y el texto se revisó técnicamente. Los procedimientos **no** se ensayaron con hardware en esta revisión; ensaya cada práctica en tu banco antes de la sesión.

## Contenido de la carpeta

```text
lab_SDR_surveillance_LaTeX/
├── laboratorio_sdr_surveillance.pdf   # manual compilado (entregable)
├── main.tex                           # documento maestro: portada, estilos, índice
├── laboratorio_sdr_3.tex              # contenido del laboratorio, cargado por main.tex
├── marco-academic.sty                 # sistema visual MARCO ACADEMIC
├── grc/                               # flowgraphs de referencia de la Práctica 3 (GNU Radio 3.10)
│   ├── lab02_wbfmtx_signalsource.grc  #   tono de 1 kHz
│   └── lab02_wbfmtx.grc               #   micrófono
├── compile-xelatex.bat                # compilación recomendada en Windows
├── compile-lualatex.bat               # alternativa LuaLaTeX
├── Makefile                           # compilación en Linux/macOS
└── latexmkrc                          # configuración para latexmk
```

`build/` (archivos intermedios) y `_hist/` (borradores anteriores y figuras no usadas por esta edición, conservados localmente) están excluidos de Git.

## Compilar

Requisitos: una distribución TeX reciente (MiKTeX o TeX Live) con XeLaTeX y los paquetes que carga `marco-academic.sty`, entre ellos `libertinus`, `plex-sans`, `sourcecodepro`, `tcolorbox`, `listings`, `babel-spanish`, `siunitx`, `cleveref` y `koma-script`. MiKTeX los instala automáticamente la primera vez.

**Windows (PowerShell), desde esta carpeta:**

```powershell
.\compile-xelatex.bat
```

**Manual o en Linux/macOS** (tres pasadas para estabilizar índice, referencias y número total de páginas):

```bash
mkdir -p build
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build -jobname=laboratorio_sdr_surveillance main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build -jobname=laboratorio_sdr_surveillance main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build -jobname=laboratorio_sdr_surveillance main.tex
cp build/laboratorio_sdr_surveillance.pdf .
```

`make` hace lo mismo. Con latexmk y Perl disponibles: `latexmk main.tex` (usa `latexmkrc`).

Verificado el 13 de octubre de 2026 con MiKTeX 25.12 (XeTeX 4.16) en Windows 11: tres pasadas sin errores, sin cajas desbordadas, sin referencias indefinidas y sin glifos ausentes. LuaLaTeX también compila el documento.

### Nota sobre MiKTeX y `\DocumentMetadata`

`main.tex` no usa `\DocumentMetadata` a propósito. En una instalación MiKTeX con módulos `latex-lab`/`tagpdf` y capa L3 desincronizados, esa instrucción activaba el etiquetado PDF experimental y producía comandos y sockets no definidos antes de cargar el contenido. El manual no la necesita.
