

init:
	docker build -t nuitka-wine-builder ./tools

build:
	docker run --rm -v ./app:/app -v ./bin:/output nuitka-wine-builder \
    bash -c "wine python3 -m nuitka --standalone --onefile --mingw64 --windows-disable-console /app/myscript.py && cp /app/myscript.exe /output/"