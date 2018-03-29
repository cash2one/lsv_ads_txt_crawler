#!/usr/bin/env python
# -*- coding: utf-8 -*-

# README
# Ads.txt Scraper Function, this only scrapes the URL and expects a good response. All other responses are ignored.
# This should push scraped ads.txt to a parser which will write the entries to a database.

DOMAINS_TO_SCRAPE_START = 1
DOMAINS_TO_SCRAPE_END = 10

# Logging, need this setup first.
import logging
from datetime import datetime

logs_location = 'logs/'
logger = logging.getLogger('ads_txt_crawler_lsv1')
log_handler = logging.FileHandler(logs_location + 'scraper{:%Y-%m-%d_%H_%M}.log'.format(datetime.now()))
log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
log_handler.setFormatter(log_formatter)
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)

# Install any missing modules and prepare to scrape.
import pip


def init_modules():
    packages = ['backoff', 'beautifulsoup4', 'bs4', 'certifi', 'chardet',
                'click', 'flask', 'idna', 'itsdangerous', 'jinja2', 'markupsafe',
                'numpy', 'pandas', 'pip', 'python-dateutil', 'pytz',
                'requests', 'setuptools', 'six', 'sqlalchemy', 'urllib3',
                'werkzeug', 'wheel']
    try:
        for package in packages:
            pip.main(['install', '--upgrade', package])
        logger.info("Modules checked, good to proceed.")
    except Exception as er:
        logger.error("Module install failed:", er)


from modules import scrape_domains, get_domains_list

import sqlite3
import time

database_location = 'db/adstxt.db'

conn = sqlite3.connect(database_location)
c = conn.cursor()


def init_db():
    # Certificate Authority not used because it is of no importance in this simple app.
    try:
        logger.info("Creating database table.")
        c.execute(
            "CREATE TABLE IF NOT EXISTS adstxt(unix REAL, datestamp TEXT, domain TEXT, ssp TEXT, account_id TEXT, relationship TEXT)")
        conn.commit()
        logger.info("Database table created.")
    except sqlite3.Error as er:
        logger.error("Failed to init db:", er)


def remove_existing_rows(site):
    try:
        logger.debug("Deleting entry for : {0}".format(site))
        c.execute("DELETE FROM adstxt WHERE domain=?", (site,))
        conn.commit()
        logger.debug("Deleted entry for : {0}".format(site))
    except sqlite3.Error as er:
        logger.info("Failed to remove existing row:", er)


def dynamic_data_entry(domain, ssp=None, account_id=None, relationship=None, certauth=None):
    try:
        logger.debug("Inserting rows: {0},{1},{2},{3}".format(domain, ssp, account_id, relationship))
        unix = int(time.time())
        date = str(datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        c.execute(
            "INSERT INTO adstxt (unix, datestamp, domain, ssp, account_id, relationship) VALUES (?, ?, ?, ?, ?, ?)",
            (unix, date, domain, ssp, account_id, relationship))
        conn.commit()
        logger.debug("Rows inserted: {0},{1},{2},{3}".format(domain, ssp, account_id, relationship))
    except sqlite3.Error as er:
        logger.error("Failed to write row:", er)


def read_domains_to_scrape(low, high):
    try:
        logger.debug("Reading domains.")
        c.execute('SELECT domain FROM domain_list WHERE rank BETWEEN ? AND ?', (low, high))
        domains = c.fetchall()
        domain_data = (x[0] for x in domains)
        conn.commit()
        return domain_data
    except sqlite3.Error as er:
        logger.info("Failed to remove existing row:", er)


def scrape(start, end):
    sites = read_domains_to_scrape(start, end)

    for site in sites:
        try:
            remove_existing_rows(site)
            logger.info(site + " Starting scrape.")
            for entry in scrape_domains(site):
                entry = entry.replace(" ", "").split(",")
                if len(entry) >= 3:
                    dynamic_data_entry(site, entry[0], entry[1], entry[2].split("#")[0])
                    print site, entry
            logger.info(site + " Scrape successful, committed to database.")

        except:
            dynamic_data_entry(site, None, None, None)
            print site
            logger.info(site + " No ads.txt found.")
            pass


init_modules()
init_db()
get_domains_list()
logger.info("Probably got domains succesfully.")  # Need to refactor this at some point.
scrape(DOMAINS_TO_SCRAPE_START, DOMAINS_TO_SCRAPE_END)  # Scrape domains start and stop.
c.close()
conn.close()
