FROM frolvlad/alpine-python3:latest

RUN apk add --no-cache git

RUN git clone https://github.com/jaimeMF/youtube-dl-api-server && \
    cd youtube-dl-api-server && \
    pip install -e .

EXPOSE 9191

ENTRYPOINT [ "youtube-dl-server", "--number-processes", "1", "--host", "0.0.0.0"]