#!/bin/bash

docker run -v "./:/src/" batonogov/pyinstaller-windows:python-3.10 "pyinstaller --onefile --windowed --icon=./src/icon.ico --add-data './src/icon.png;.' --name=TkCalc_alpha_0.9.2 ./src/main.py"
#docker run -v "./:/src/" batonogov/pyinstaller-linux "pyinstaller --onefile --windowed --icon=./src/icon.ico --add-data './src/icon.png;.' --name=TkCalc_alpha_0.9 ./src/main.py"
