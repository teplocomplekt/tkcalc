 FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    build-essential \
    wine \
    mingw-w64 \

RUN pip3 install nuitka

WORKDIR /
# COPY ./app /app
# COPY ./tools/build.sh /build.sh

ENV APP_OUTPUT_DIR=/output

CMD ["/build.sh"]