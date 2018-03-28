# ADS.TXT CRAWLER

This simple application retrieves the top 1 million sites on Alexa and scrapes through each domain looking for a valid ads.txt response. Entries are then written to an SQLite database.

My goal is to make this application completely self sufficient, where a user can clone it to their box, run a single python file, and get going. Though I suspect splitting up the scraper and the web server is a good practice to have.  

<a href="https://i.imgur.com/jG1msrQg.png" target="_blank">Screenshot</a>

## Getting Started

Make sure you have an internet connection and python 2.7.  

### Prerequisites

This project requires Python 2.7, though it will probably work with Python 3+ out of the box.

### Installing

There's no real "installation" as long as all modules below are installed.

```
['backoff==1.4.3', 'beautifulsoup4==4.6.0', 'bs4==0.0.1', 'certifi==2018.1.18', 'chardet==3.0.4', 'click==6.7', 'flask==0.12.2', 'idna==2.6', 'itsdangerous==0.24', 'jinja2==2.10', 'markupsafe==1.0', 'numpy==1.14.1', 'pandas==0.22.0', 'pip==9.0.1', 'python-dateutil==2.6.1', 'pytz==2018.3', 'requests==2.18.4', 'setuptools==38.5.1', 'six==1.11.0', 'sqlalchemy==1.2.5', 'urllib3==1.22', 'werkzeug==0.14.1', 'wheel==0.30.0']
```

## Deployment

Call start_scraper, and start_web_server and it'll get going. By default I am scraping the top 10 sites from the Alexa top 10 million. 

```
python start_scraper.py
```

```
python start_web_server.py
```

Reach the server by going to http://127.0.0.1 (port 80 is used by default)

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