FROM golang:latest
ARG PIKA_ADDR
ENV PIKA_ADDR=${PIKA_ADDR}
RUN test -n "$PIKA_ADDR"
WORKDIR /work
ADD ./info.toml /work/
RUN git clone --depth 1 https://github.com/OpenAtomFoundation/pika &&\
    cd pika/tools/pika_exporter &&\
    make
# https://github.com/OpenAtomFoundation/pika/blob/unstable/tools/pika_exporter/README.md
ENTRYPOINT ["/bin/bash", "-c", "/work/pika/tools/pika_exporter/bin/pika_exporter --config /work/info.toml --log.level error -pika.addr $PIKA_ADDR" ]
