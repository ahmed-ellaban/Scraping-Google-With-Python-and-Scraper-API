import requests
from requests_html import HTMLSession
from urllib.parse import quote

api_key = 'Your_API_key'

unwanted_starts = ('https://www.google',
                   'https://google',
                   'https://webcache.googleusercontent',
                   'http://webcache.googleusercontent',
                   'https://policies.google',
                   'https://support.google',
                   'https://maps.google')  # used to ignore any url starts with these urls


# main functions
def get_url(query):
    """
    :param query:the query sent by user
    :return: the url
    """
    url = "https://www.google.com//search?q=" + query
    api_url = f"http://api.scraperapi.com?api_key={api_key}&url={quote(url)}"
    print(f'google search url:{url}')  # will only print google url
    return api_url


def get_source(url):
    """Return the source code for the provided URL.

    Args:
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html.
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        raise (e)


def scrape_google(url):
    """
    :param query:
    :param num:
    :return: the links found in the google search
    """

    response = get_source(url)
    if response.status_code != 200:
        raise Exception(f"error from scraping, status_code:{response.status_code}")
    absolute_links = list(response.html.absolute_links)
    # filter the links
    links = [url.split('/translate?hl=ar&sl=en&u=')[-1].split('?utm_')[0] for url in absolute_links[:] if
             not url.startswith(unwanted_starts)]
    links = delete_duplicates(links)
    return links


# supporter functions
def delete_duplicates(x):
    """it deletes the duplicates from a list"""
    return list(dict.fromkeys(x))


if __name__ == '__main__':
    query = input('Please type the query\t')  # take the query
    url = get_url(query)  # make the url
    links = scrape_google(url)
    print(f'Found {len(links)} result')
    print(links)
