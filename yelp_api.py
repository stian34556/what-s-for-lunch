# -*- coding: utf-8 -*-
"""
Sample usage of the program:
`python sample.py --term="bars" --location="San Francisco, CA"`
"""
from __future__ import print_function

import argparse
import json
import pprint
import requests
import sys
import urllib

# This client code can run on Python 2.x or 3.x.  Your imports can be
# simpler if you only need one of those.
try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

API_KEY= 'fg7eyQguEvmPsj4s2jsB_ye2iSokB74KcubFseRWjQspbYWs4JxfJkdPggG0nnkvows95Z_KHxkjElREpZ11rFs2c_bed_ejuyjZRLqEp_KFm_4wN4CnQjpixgbMYXYx'

# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.

DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = '2929 Barnet Hwy, Coquitlam, BC V3B 5R5'
DEFAULT_PRICE = '2'
DEFAULT_RADIUS = '10000'
SEARCH_LIMIT = 3


def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()
    #return response


def search(api_key, term, location, price, radius, sort_by):
    """Query the Search API by a search term and location. + price, distance
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'price' : price.replace(' ', '+'),
        'radius' : radius.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'sort_by' : sort_by.replace(' ', '+')
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_business(api_key, business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)


def query_api(term, location, price, radius):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(API_KEY, term, location, price, radius, "rating")

    businesses = response.get('businesses')

    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(term, location))
        return "none"

    business_id = businesses[0]['id']

    response = get_business(API_KEY, business_id)

    places = []

    if (len(businesses) < 3):

        size = len(businesses)
        for x in range(size):
            places.append([businesses[x]['name'], businesses[x]['rating'], businesses[x]['price'], businesses[x]['image_url']])

    else:
        for x in range(3):
            places.append([businesses[x]['name'], businesses[x]['rating'], businesses[x]['price'], businesses[x]['image_url']])
    
    return places

def search_result(term, location, price, radius):

    try:
        return query_api(term, location, price, radius)
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )
