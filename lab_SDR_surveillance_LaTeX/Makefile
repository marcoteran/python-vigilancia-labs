JOB = laboratorio_sdr_surveillance
TEX = xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build -jobname=$(JOB)

.PHONY: all clean
all:
	mkdir -p build
	$(TEX) main.tex
	$(TEX) main.tex
	$(TEX) main.tex
	cp build/$(JOB).pdf $(JOB).pdf
clean:
	rm -rf build
