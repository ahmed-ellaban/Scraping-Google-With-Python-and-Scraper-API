# How to scrape Google Search Engine using Requests and Scraper API?
**Scraping google search isn't easy, It is one of the hardest scraping tasks due to many things
first, the strong protection of google and the way it changes the HTML code which spoils your CSS Selectors and Xpath Selectors and makes you have to edit your code every time, second it is blocking you after a few requests sent
in this article, I am going to solve the two issues above
Creating a scraper works without having to change the selectors every time
attaching scraper Api to the code to avoid getting banned**

## 1-let us first import the libraries
    import requests
    from requests_html import HTMLSession
we will use these libraries in the script
## 2-we need the user to type the query
    query = input('Please type the query\t')  # take the queryp
## 3-we need to make the url used so we will use this function
    def get_url(query):
        """
        :param query:the query sent by user
        :return: the url
        """
        url = "https://www.google.com//search?q=" + query
        print(f'google search url:{url}')
        return url
## 4-we will use this function it is used to fetch the URL given and return the response and it uses HTMLSession
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
## 5-we need to use another function that will take the URL and send it to get_source and takes the response but we need first to exclude the unwanted links that found on the google page

    unwanted_starts = ('https://www.google',
                       'https://google',
                       'https://webcache.googleusercontent',
                       'http://webcache.googleusercontent',
                       'https://policies.google',
                       'https://support.google',
                       'https://maps.google')  # used to ignore any url starts with these urls
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
this function will parse the response and extract all links from it and get the original URL instead of the google URL referring link
and delete_duplicates function will delete the dubpliactes from the listduplicates
the code now is

    import requests
    from requests_html import HTMLSession

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
        print(f'google search url:{url}')
        return url

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
NOW RUN IT
This is the result

        Please type the query Ahmed Ellban Upwork
        google search url:https://www.google.com//search?q=Ahmed Ellban Upwork
        Found 16 result
        ['https://www.upwork.com/freelancers/~01d75e30c7fc520854&prev=search&pto=aue', 'https://ar.quora.com/%D9%85%D8%A7-%D9%87%D9%8A-%D8%A3%D9%81%D8%B6%D9%84-%D9%85%D9%86%D8%B5%D8%A7%D8%AA-%D8%A7%D9%84%D8%B9%D9%85%D9%84-%D8%A7%D9%84%D8%AD%D8%B1-Freelance-%D9%84%D8%B9%D9%85%D9%84-%D8%AA%D8%B5%D9%85%D9%8A%D9%85', 'https://www.upwork.com/freelancers/~016685de2bf39abdc0', 'https://www.upwork.com/o/profiles/users/~0134c871122a97089c/', 'https://www.upwork.com/freelancers/~016685de2bf39abdc0&prev=search&pto=aue', 'https://www.upwork.com/freelancers/~0134899edfdeb25a8b', 'https://www.upwork.com/o/profiles/users/~0134c871122a97089c/&prev=search&pto=aue', 'https://www.upwork.com/freelancers/~0161bba932184b0be4&prev=search&pto=aue', 'https://www.upwork.com/freelancers/~0194f169492bbccbc7', 'https://ar.quora.com/%D8%A8%D8%AD%D9%83%D9%85-%D8%AA%D8%AC%D8%B1%D8%A8%D8%AA%D9%83%D9%85-%D8%A7%D9%84%D8%B4%D8%AE%D8%B5%D9%8A%D8%A9-%D9%85%D8%A7-%D9%87%D9%8A-%D8%A3%D9%81%D8%B6%D9%84-%D8%A7%D9%84%D9%85%D9%88%D8%A7%D9%82%D8%B9', 'https://m.facebook.com/%D9%85%D8%B3%D8%A7%D8%B9%D8%AF%D8%A9-%D9%81%D9%8A-%D8%AC%D9%85%D9%8A%D8%B9-%D8%A7%D9%84%D8%AA%D8%AE%D8%B5%D8%B5%D8%A7%D8%AA-%D9%88%D8%A7%D9%84%D9%85%D8%B4%D8%A7%D9%83%D9%84-131395444082178/posts/', 'https://www.upwork.com/freelancers/~0161bba932184b0be4', 'https://www.upwork.com/freelancers/~01d75e30c7fc520854', 'https://ar.quora.com/%D8%A8%D8%AD%D9%83%D9%85-%D8%AA%D8%AC%D8%B1%D8%A8%D8%AA%D9%83%D9%85-%D8%A7%D9%84%D8%B4%D8%AE%D8%B5%D9%8A%D8%A9-%D9%85%D8%A7-%D9%87%D9%8A-%D8%A3%D9%81%D8%B6%D9%84-%D8%A7%D9%84%D9%85%D9%88%D8%A7%D9%82%D8%B9?top_ans=399139736', 'https://www.upwork.com/freelancers/~0134899edfdeb25a8b&prev=search&pto=aue', 'https://www.upwork.com/freelancers/~0194f169492bbccbc7&prev=search&pto=aue']

        Process finished with exit code 0


**Now we have a working script but we cannot run it a lot because we will get banned
so let us go to the next step using [Scraper API](https://www.scraperapi.com/?fp_ref=ae)
[Scraper API](https://www.scraperapi.com/?fp_ref=ae) is a web service that enables automated data extraction from websites. Scrapers are used for a variety of purposes, but the most common is to collect data that would be too difficult or time-consuming to obtain manually. A scraper is an API that allows for automated data collection, whereas a crawler is a software that crawls and indexes web pages.
This can be done manually or with the use of software tools known as web scrapers. These software tools are typically favored because they are more powerful, quicker, and, hence, handier.
After extracting the user's desired data, web scrapers frequently reformat the data into a more usable format, such as an Excel spreadsheet.
the most important thing it provides a free plan which we can use and avoid the banning of google and it provides bigger plans in good cost you can see the [Pricing Page](https://www.scraperapi.com/pricing?fp_ref=ae)**

## 6-let us first create an account
go to [sign-up page](https://www.scraperapi.com/signup?fp_ref=ae) and create an account then copy your API key
copy the API key

## 7-let us add api key param in the script
    api_key = 'Your_API_key'
then we should edit get_url function to handle the new changes we used another libaray called urllib to quote the google url to avoid the errors
so don't forget to import it by
from urllib.parse import quote

    def get_url(query):
        """
        :param query:the query sent by user
        :return: the url
        """
        url = "https://www.google.com//search?q=" + query
        api_url = f"http://api.scraperapi.com?api_key={api_key}&url={quote(url)}"
        print(f'google search url:{url}') # will only print google url
        return api_url

**Now the full code is:**
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
    
### Now you can run it and benefit from the strength of Scraper API and Google search Engine
**Thank you for reading**
**if you have any question don't hesitate to ask me❤️❤️**
