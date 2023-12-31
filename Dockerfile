FROM alpine:3.18.3

WORKDIR /app

RUN apk add --no-cache \
    bcc-doc \
    bcc-tools \
    bpftool

COPY xdp_drop.* .

ENV DEVICE=cni0
ENV SLEEP_TIME=0

CMD ["python3", "xdp_drop.py"]
