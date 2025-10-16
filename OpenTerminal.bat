@echo off
REM Öffnet CMD und Visual Studio Code im Ordner, in dem dieses Skript liegt

setlocal
cd /d "%~dp0"

REM Starte eine neue CMD im aktuellen Ordner
start cmd 

REM Öffne VS Code im aktuellen Ordner
code "%~dp0"
