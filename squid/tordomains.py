#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http.client import HTTPSConnection
from json.decoder import JSONDecoder
from pathlib import Path
from typing import List

DEFAULT_ENCODING = "utf-8"


def blacklisted_domains() -> List[str]:
    """
    Download the list of domains currently forbidden in the Russian Federation.
    """
    connection = HTTPSConnection("reestr.rublacklist.net")
    connection.request("GET", "/api/v2/domains/json/")
    response_bytes = connection.getresponse().read()

    response = response_bytes.decode(DEFAULT_ENCODING)
    connection.close()

    decoder = JSONDecoder()
    return decoder.decode(response)


if __name__ == "__main__":
    tordomains_file = Path(__file__).with_name("tordomains.txt")
    domains_list = blacklisted_domains()
    print(f"Downloaded {len(domains_list):d} domains")

    with tordomains_file.open("wt", encoding=DEFAULT_ENCODING) as io:
        for domain in domains_list:
            io.write(f"{domain}\n")
