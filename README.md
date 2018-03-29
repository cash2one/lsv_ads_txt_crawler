# ADS.TXT CRAWLER

This simple application retrieves the top 1 million sites on Alexa and scrapes through each domain looking for a valid ads.txt response. Entries are then written to an SQLite database.

My goal is to make this application completely self sufficient, where a user can clone it to their box, run a single python file, and get going. Though I suspect splitting up the scraper and the web server is a good practice to have.  

Additionally, a simple web app is started that will show the last good 1000 scraped entries, and the export CSV option only exports rows with valid ads.txt data, sites with no Ads.txt stuff is not exported, let me know if this is a desirable feature.

<a href="https://i.imgur.com/jG1msrQg.png" target="_blank">Screenshot</a>

## See it Live

A version of this is running <a href="http://luissastre.ca" target="_blank">here</a>, but please note my web server is very slow and this is scraping the top 100k sites indefinitely, so please bare with me :)!

## Getting Started

Make sure you have an internet connection and python 2.7.  

### Prerequisites

This project requires Python 2.7, though it will probably work with Python 3+ out of the box.

### Installing

There's no real "installation" apart from cloning the repo and running the two scripts, on start the scraper will automatically call pip and install any missing modules, the list of used modules is below.

```
['backoff==1.4.3', 'beautifulsoup4==4.6.0', 'bs4==0.0.1', 'certifi==2018.1.18', 'chardet==3.0.4', 'click==6.7', 'flask==0.12.2', 'idna==2.6', 'itsdangerous==0.24', 'jinja2==2.10', 'markupsafe==1.0', 'numpy==1.14.1', 'pandas==0.22.0', 'pip==9.0.1', 'python-dateutil==2.6.1', 'pytz==2018.3', 'requests==2.18.4', 'setuptools==38.5.1', 'six==1.11.0', 'sqlalchemy==1.2.5', 'urllib3==1.22', 'werkzeug==0.14.1', 'wheel==0.30.0']
```

## Deployment and Usage

I wrote this script to run by itself as best I could, I don't want to share this with semi technical friends and have them have to do much more than setup python 2.7. Ideally they are just getting the python executable and going to town.

There are two major variable which should be defined before running this script located in [start_scraper.py](https://github.com/lsv1/lsv_ads_txt_crawler/blob/abd5084a9a76c8708d26738cb63e272376ee1b0c/start_scraper.py#L8).

These two variables denote at what Top 1 Million site rank to start and stop at, the current default value is set to scrape the top 1 million sites. Be careful scraping more than 100,000 sites as sqlite might be a little slow, and also the exported CSV will be over a million rows easily.

```
DOMAINS_TO_SCRAPE_START = 1
DOMAINS_TO_SCRAPE_END = 1000
```

Once you've defined the start/stop ranges run the scraper:

```
python start_scraper.py
```

Once you see the database has initialized you can then run the web server:

```
python start_web_server.py
```

Reach the server by going to http://127.0.0.1 (port 80 is used by default)

## Database and Logging

Once deployed and running the folders db/ and logs/ will be created.

## Built With

* [flask](http://flask.pocoo.org/)
* [requests](http://docs.python-requests.org/en/master/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## Contributing

Feel free to fork and contribute, however, as of 2018-03-28 I am still working heavily on this. 

## Authors

* **Luis Sastre Verzun** - *Initial work* - [lsv1](https://github.com/lsv1)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to the IAB's scraper, which I was not pleased with, so I decided to write my own.