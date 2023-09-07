FROM alpine:3.18.3

WORKDIR /app

RUN apk add --no-cache \
    bcc-doc \
    bcc-tools

COPY xdp_drop.* .

ENV DEVICE=cni0

CMD ["python3", "xdp_drop.py"]
