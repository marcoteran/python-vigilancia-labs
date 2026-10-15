MANUAL = laboratorio_sdr_surveillance
GUIA = guia_instructor_sdr
TEX = xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build

.PHONY: all manual guia verificar clean
all: manual guia

manual:
	mkdir -p build
	$(TEX) -jobname=$(MANUAL) main.tex
	$(TEX) -jobname=$(MANUAL) main.tex
	$(TEX) -jobname=$(MANUAL) main.tex
	cp build/$(MANUAL).pdf $(MANUAL).pdf

guia:
	mkdir -p build
	$(TEX) -jobname=$(GUIA) guia_instructor.tex
	$(TEX) -jobname=$(GUIA) guia_instructor.tex
	$(TEX) -jobname=$(GUIA) guia_instructor.tex
	cp build/$(GUIA).pdf $(GUIA).pdf

verificar:
	sha256sum -c datos_adsb/SHA256SUMS
	python3 herramientas/adsb_iq.py verificar datos_adsb/modes1_dump1090_2MSps_1090MHz.sdriq

clean:
	rm -rf build
