@echo off
echo BUILD DEBUG VERSION
pyinstaller.exe --onefile --icon="img/favicon.ico" --name="instaru" instaru.py
echo BUILD END USER VERSION
pyinstaller.exe --onefile --icon="img/favicon.ico" --noconsole --name="instaru-enduser" instaru.py
echo CLEANUP
rmdir /s  build