

init:
	docker build -t nuitka-wine-builder ./tools
build:
	docker run --rm -v ./app:/app -v ./bin:/output nuitka-wine-builder