#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Raw scraper function, ignore all errors (and HTTP), expect as fast response.

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.adapters.DEFAULT_RETRIES = 0


def scrape_domains(domain_to_scrape):
    http_protocol = "http://"
    http_resource = "/ads.txt"
    url = http_protocol + domain_to_scrape + http_resource

    headers = {
        "User-Agent": "lsv1_ads.txt_crawler/0.1; +https://github.com/lsv1",
        "Accept": "text/plain",
    }

    try:
        r = requests.get(url, allow_redirects=1, headers=headers,
                         timeout=1, verify=False)

        if r.status_code == 200 and bool(BeautifulSoup(r.text, "html.parser").find()) is False:
            if r.url != domain_to_scrape:
                return r.text.splitlines()

    except:
        pass