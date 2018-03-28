#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Module for getting Alexa top 1 million domains and writing this all to the database.

import requests
import zipfile
import sqlite3
import pandas


def get_domains_list():
    url = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"
    local_filename = "temp/top-1m.csv.zip"
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    zip = zipfile.ZipFile(r'temp/top-1m.csv.zip')
    zip.extractall(r'temp')
    column_names = ['rank', 'domain']
    df = pandas.read_csv("temp/top-1m.csv", names=column_names)
    df.to_sql("domain_list", sqlite3.connect("db/adstxt.db"), if_exists='replace',
              index=False)
