#!/bin/bash

docker run -v "./:/src/" batonogov/pyinstaller-windows:python-3.10 "pyinstaller --onefile --windowed --icon=./src/icon.ico --add-data './src/icon.png;.' --add-data './src/watermark.png;.' --name=TkCalc_alpha_0.9.4 ./src/main.py"
