blackbox
========
**Squid** &#8594; **Privoxy** &#8594; **Tor** bundle.

Usage
-----
```shell
# Pull images for the services:
docker-compose pull

# Restart the services:
docker-compose up \
    --detach \
    --force-recreate \
    --no-build \
    --remove-orphans
```

Links
-----
- Code: <https://gitlab.com/amalchuk/blackbox>
- GitHub mirror: <https://github.com/amalchuk/blackbox>
