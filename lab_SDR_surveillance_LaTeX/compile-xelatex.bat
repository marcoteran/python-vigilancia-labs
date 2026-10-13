@echo off
setlocal
cd /d "%~dp0"
if not exist build mkdir build
for /L %%i in (1,1,3) do (
  echo Compilacion XeLaTeX %%i/3...
  xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build -jobname=laboratorio_sdr_surveillance main.tex
  if errorlevel 1 goto :error
)
copy /Y build\laboratorio_sdr_surveillance.pdf laboratorio_sdr_surveillance.pdf >nul
echo.
echo OK: laboratorio_sdr_surveillance.pdf generado correctamente.
exit /b 0
:error
echo.
echo ERROR: revise build\laboratorio_sdr_surveillance.log.
exit /b 1
