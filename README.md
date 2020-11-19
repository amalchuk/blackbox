blackbox
========
[![pipeline status][pipeline]][homepage]

**Squid** &#8594; **Privoxy** &#8594; **Tor** bundle.

Development
-----------
```shell
# Create a virtual machine:
docker-machine create \
    --driver virtualbox \
    --virtualbox-cpu-count 2 \
    --virtualbox-disk-size 20480 \
    --virtualbox-memory 2048 \
    blackbox

# Build and restart the services:
docker-compose up \
    --detach \
    --force-recreate \
    --build \
    --remove-orphans
```

Distribution
------------
This project is licensed under the terms of the [MIT License](LICENSE).

Links
-----
- Code: <https://gitlab.com/amalchuk/blackbox>
- GitHub mirror: <https://github.com/amalchuk/blackbox>

[homepage]: <https://gitlab.com/amalchuk/blackbox>
[pipeline]: <https://gitlab.com/amalchuk/blackbox/badges/master/pipeline.svg?style=flat-square>
