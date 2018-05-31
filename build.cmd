@echo off
set "ANTLR_VERSION=4.7.1
set "CLASSPATH=.;%cd%\antlr-%ANTLR_VERSION%-complete.jar;%cd%\antlr-runtime-%ANTLR_VERSION%.jar;%CLASSPATH%"
set "GRAMMAR_DIR=%cd%\grammar"

if not exist "%GRAMMAR_DIR%" (
   echo "Try to find grammar in %GRAMMAR_DIR%. Nothing found."
   pause
   exit /b 1
)

pushd "%GRAMMAR_DIR%"
del *.interp *.py *.tokens
java org.antlr.v4.Tool -Dlanguage=Python3 Expressions.g4
if %errorlevel% gtr 0 (
   echo "An error occurred."
   pause
   exit /b 1
)
popd

python calc.py
if %errorlevel% gtr 0 (
   echo "An error occurred."
   pause
   exit /b 1
)

pause