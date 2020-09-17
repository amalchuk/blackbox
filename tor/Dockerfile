FROM golang:alpine AS builder

RUN ["apk", "add", "--quiet", "--no-cache", "git"]
RUN ["go", "get", "git.torproject.org/pluggable-transports/obfs4.git/obfs4proxy"]

FROM alpine:latest
COPY --from=builder ["/go/bin/obfs4proxy", "/usr/local/bin/"]

RUN ["apk", "add", "--quiet", "--no-cache", "tor"]
USER tor

WORKDIR /etc/tor
COPY ["tor.cfg", "/etc/tor/torrc"]

VOLUME ["/var/lib/tor"]
EXPOSE 1080/tcp
CMD ["tor", "-f", "/etc/tor/torrc"]
