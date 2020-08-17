FROM alpine:latest

RUN ["apk", "add", "--quiet", "--no-cache", "privoxy"]
USER privoxy

WORKDIR /etc/privoxy
COPY ["privoxy.cfg", "/etc/privoxy/config"]

EXPOSE 8000/tcp
CMD ["privoxy", "--no-daemon", "/etc/privoxy/config"]
