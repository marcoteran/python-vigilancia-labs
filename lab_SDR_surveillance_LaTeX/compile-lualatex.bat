@echo off
rem Alternativa a compile-xelatex.bat. La compilación de referencia es XeLaTeX.
setlocal
cd /d "%~dp0"
if not exist build mkdir build
call :build laboratorio_sdr_surveillance main.tex || goto :error
call :build guia_instructor_sdr guia_instructor.tex || goto :error
echo.
echo OK: laboratorio_sdr_surveillance.pdf y guia_instructor_sdr.pdf generados con LuaLaTeX.
exit /b 0

:build
for /L %%i in (1,1,3) do (
  echo Compilacion LuaLaTeX de %1, pasada %%i/3...
  lualatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build -jobname=%1 %2 >nul
  if errorlevel 1 exit /b 1
)
copy /Y build\%1.pdf %1.pdf >nul
exit /b 0

:error
echo.
echo ERROR: revise los archivos .log de la carpeta build.
exit /b 1
