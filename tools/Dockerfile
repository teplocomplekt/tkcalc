# Используем готовый Wine образ для Ubuntu 22.04
FROM tobix/wine:stable

ENV DEBIAN_FRONTEND=noninteractive
ENV WINEARCH=win64
ENV WINEDEBUG=-all

# Устанавливаем сборочные инструменты и MinGW
RUN dpkg --add-architecture i386 \
    && apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        mingw-w64 \
        patchelf \
        wget \
        ca-certificates \
        xvfb \
    && rm -rf /var/lib/apt/lists/*

# Скачиваем Windows Python
RUN wget https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe -O /tmp/python.exe

# Устанавливаем Python через Wine под Xvfb (без GUI)
RUN xvfb-run wine /tmp/python.exe /quiet InstallAllUsers=1 PrependPath=1 TargetDir="C:\\Python312"

# Обновляем pip и устанавливаем Nuitka
RUN wine "C:\\Python312\\python.exe" -m pip install --upgrade pip setuptools wheel
RUN wine "C:\\Python312\\python.exe" -m pip install nuitka

WORKDIR /app

CMD ["bash"]