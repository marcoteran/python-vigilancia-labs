@echo off
rem Compila los cuatro documentos. Se citan entre si (xr-hyper), por eso se hacen
rem tres rondas completas: cada ronda lee los .aux que dejo la anterior.
setlocal
cd /d "%~dp0"
if not exist build mkdir build
for /L %%r in (1,1,3) do (
  echo Ronda %%r/3...
  call :pass laboratorio_sdr_surveillance main.tex || goto :error
  call :pass anexo_a_fundamentos_sdr anexo_a.tex || goto :error
  call :pass anexo_b_evaluacion_sdr anexo_b.tex || goto :error
  call :pass guia_instructor_sdr guia_instructor.tex || goto :error
)
for %%d in (laboratorio_sdr_surveillance anexo_a_fundamentos_sdr anexo_b_evaluacion_sdr guia_instructor_sdr) do copy /Y build\%%d.pdf %%d.pdf >nul
echo.
echo OK: manual, anexo A, anexo B y guia del instructor generados.
exit /b 0

:pass
xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build -jobname=%1 %2 >nul
if errorlevel 1 (echo Fallo en %2 & exit /b 1)
exit /b 0

:error
echo.
echo ERROR: revise los archivos .log de la carpeta build.
exit /b 1
