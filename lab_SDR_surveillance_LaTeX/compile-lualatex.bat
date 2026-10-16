@echo off
rem Alternativa a compile-xelatex.bat (la compilacion de referencia es XeLaTeX).
setlocal
cd /d "%~dp0"
if not exist build mkdir build
for /L %%r in (1,1,3) do (
  echo Ronda LuaLaTeX %%r/3...
  call :pass laboratorio_sdr_surveillance main.tex || goto :error
  call :pass anexo_a_fundamentos_sdr anexo_a.tex || goto :error
  call :pass anexo_b_evaluacion_sdr anexo_b.tex || goto :error
  call :pass guia_instructor_sdr guia_instructor.tex || goto :error
)
for %%d in (laboratorio_sdr_surveillance anexo_a_fundamentos_sdr anexo_b_evaluacion_sdr guia_instructor_sdr) do copy /Y build\%%d.pdf %%d.pdf >nul
echo.
echo OK: cuatro documentos generados con LuaLaTeX.
exit /b 0

:pass
lualatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build -jobname=%1 %2 >nul
if errorlevel 1 (echo Fallo en %2 & exit /b 1)
exit /b 0

:error
echo.
echo ERROR: revise los archivos .log de la carpeta build.
exit /b 1
