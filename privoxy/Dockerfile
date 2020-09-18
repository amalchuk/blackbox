FROM python:alpine AS builder

WORKDIR /etc/tordomains
COPY ["tordomains.py", "/etc/tordomains/"]

ENV PYTHONOPTIMIZE="2" PYTHONUNBUFFERED="1"
RUN ["python", "tordomains.py"]

FROM alpine:latest

RUN ["apk", "add", "--quiet", "--no-cache", "privoxy"]
USER privoxy

WORKDIR /etc/privoxy
COPY --from=builder ["/etc/tordomains/tordomains.action", "/etc/privoxy/"]
COPY ["privoxy.cfg", "/etc/privoxy/config"]

EXPOSE 8000/tcp
CMD ["privoxy", "--no-daemon", "/etc/privoxy/config"]
