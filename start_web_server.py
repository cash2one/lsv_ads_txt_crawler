#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import sqlite3 as sql
import StringIO
import csv
from flask import make_response
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def list():
    con = sql.connect("db/adstxt.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute(
        "SELECT domain, datestamp, ssp, account_id, relationship FROM adstxt WHERE ssp IS NOT NULL ORDER BY datestamp DESC LIMIT 1000")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)

@app.route('/download')
def download():
    con = sql.connect("db/adstxt.db")
    con.row_factory = sql.Row
    si = StringIO.StringIO()
    cw = csv.writer(si)
    cur = con.cursor()
    cw.writerow(["datestamp", "domain", "ssp", "account_id", "relationship"])
    cw.writerows(cur.execute("SELECT datestamp,domain,ssp,account_id,relationship FROM adstxt WHERE ssp IS NOT NULL"))
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
