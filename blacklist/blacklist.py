#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from http.client import HTTPSConnection
from json.decoder import JSONDecoder
from typing import Iterator, List

DEFAULT_ENCODING = "utf-8"


def domains() -> Iterator[str]:
    """
    Download the list of the domains currently in the registry.
    """
    connection = HTTPSConnection("reestr.rublacklist.net")
    connection.request("GET", "/api/v2/domains/json")
    response = connection.getresponse().read()

    decoder = JSONDecoder()
    domains: List[str] = decoder.decode(response.decode(DEFAULT_ENCODING))
    yield from domains


if __name__ == "__main__":
    with open("blacklist.txt", "wt", encoding=DEFAULT_ENCODING) as blacklist:
        today = datetime.utcnow().strftime(r"%d.%m.%Y %H:%M:%S")
        blacklist.write(f"# Auto generated on {today}\n")

        for domain in domains():
            blacklist.write(f"{domain}\n")
