blackbox
========
[![pipeline status][pipeline]][homepage]

**Tor** and **Privoxy** bundle.

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

Distribution
------------
This project is licensed under the terms of the [MIT License](LICENSE).

Links
-----
- Code: <https://gitlab.com/amalchuk/blackbox>
- GitHub mirror: <https://github.com/amalchuk/blackbox>

[homepage]: <https://gitlab.com/amalchuk/blackbox>
[pipeline]: <https://gitlab.com/amalchuk/blackbox/badges/master/pipeline.svg?style=flat-square>
