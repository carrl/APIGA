#! /usr/bin/env python
#-*- coding:utf-8 -*-
# http://www.google.com/__utm.gif
# utmac: profile number
# utmcc: Cookie Values
# utmcs: Language encoding for the browser. Some browsers don't set this, in which case it is set to "-"
# utmdt: Page Title, which is a URL-encoded string
# utmhn: Host Name, which is a URL-encoded string
# utmn:  Unique ID generated for each GIF request to prevent caching of the GIF image.
# utmwv: Tracking code version
# utmp:  Page request of the current page. 
# utmr:  Referral, complete URL
# utmip: IP

import Cookie
import urlparse
import urllib
import urllib2
import os
import random
import time
import math

def my_rand(cnt) :
    return str(random.randint((10 ** (cnt - 1)), ((10 ** cnt) - 1)))

def google_analytics_track(account="", title="my-title") :
    gat_params = {}

    env = os.environ

    http_host = ""
    remote_addr = ""
    server_name = ""
    request_uri = ""
    referer = ""
    if os.environ.has_key("HTTP_HOST") :
        http_host = os.environ["HTTP_HOST"]
    if os.environ.has_key("REMOTE_ADDR") :
        remote_addr = os.environ["REMOTE_ADDR"]
    if os.environ.has_key("SERVER_NAME") :
        server_name = os.environ["SERVER_NAME"]
    if os.environ.has_key("REQUEST_URI") :
        request_uri = os.environ["REQUEST_URI"]
    if os.environ.has_key("HTTP_REFERER") :
        referer = os.environ["HTTP_REFERER"]

    try :
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    except :
        cookie = {}

    domain_hash = my_rand(8)
    visitor_id = my_rand(9)
    now_timestamp = str(math.trunc(time.mktime(time.gmtime())))

    try :
        utma = cookie["__utma"].value
        domain_hash = string.split(utma,".")[0]
    except :
        utma = domain_hash + "." + visitor_id + "." + now_timestamp + "." + now_timestamp + "." + now_timestamp + "." + my_rand(2)

    try :
        if (referer) :
            utmz = domain_hash + "." + now_timestamp + '.2.2.utmccn=(referral)|utmcsr=' + urlparse.urlsplit(referer).netloc + '|utmcmd=referral'
        else :
            utmz = cookie["__utmz"].value
    except :
        utmz = domain_hash + "." + now_timestamp + '.2.2.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none)'

    gat_params["utmac"] = account
    gat_params["utmcc"] = '__utma%3D'+utma+'%3B%2B'+'__utmz%3D'+utmz+'%3B%2B'
    gat_params["utmcs"] = '-'
    gat_params["utmdt"] = urllib.quote_plus(title)
    if (http_host) :
        gat_params["utmhn"] = urllib.quote_plus(http_host)
    gat_params["utmn"] = my_rand(9)
    gat_params["utmwv"] = "4.4sp"
    if (request_uri) :
        gat_params["utmp"] = urllib.quote_plus(request_uri)
    if (referer) :
        gat_params["utmr"] = referer
    if (remote_addr) :
        gat_params["utmip"] = remote_addr

    gat_url = "http://www.google-analytics.com/__utm.gif?"
    gat_params_str = ""
    for key in gat_params :
        gat_params_str += key + "=" + gat_params[key] + "&"

    gat_url = gat_url + gat_params_str[:-1]

    urllib2.urlopen(gat_url, timeout=1)


if __name__ == "__main__" :
    print "Content-type: text/plain"
    print

    google_analytics_track(account="XX-XXXXXX-X", title="Test APIGA")

    print "Test APIGA"
