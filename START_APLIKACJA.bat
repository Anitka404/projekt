@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
    echo Brak pliku .venv\Scripts\python.exe
    echo Otworz terminal w tym folderze i utworz srodowisko albo daj znac.
    pause
    exit /b
)
".venv\Scripts\python.exe" main.py
pause
