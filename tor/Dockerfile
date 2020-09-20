FROM alpine:latest
RUN ["apk", "add", "--quiet", "--no-cache", "tor"]

WORKDIR /etc/tor
COPY ["tor.cfg", "/etc/tor/torrc"]

VOLUME ["/var/lib/tor"]
EXPOSE 9050/tcp
CMD ["tor", "-f", "/etc/tor/torrc"]
