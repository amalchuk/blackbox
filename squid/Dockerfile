FROM alpine:latest

RUN ["apk", "add", "--quiet", "--no-cache", "squid"]
USER squid

WORKDIR /etc/squid
COPY ["squid.conf", "tordomains.txt", "/etc/squid/"]

EXPOSE 8000/tcp
CMD ["squid", "-CNY"]
