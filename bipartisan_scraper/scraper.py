import re
import time
from .parser import parse_page
from dateutil.parser import parse
from .utils import get_soup

patterns = [
    re.compile('https://bipartisanpolicy.org/[\w]+')]
url_blogbase = 'https://bipartisanpolicy.org/blog/page/{}'

def is_matched(url):
    for pattern in patterns:
        if pattern.match(url):
            return True
    return False

def yield_latest_allblog(begin_date, max_num=10, sleep=1.0):
    """
    Artuments
    ---------
    begin_date : str
        eg. 2018-01-01
    max_num : int
        Maximum number of news to be scraped
    sleep : float
        Sleep time. Default 1.0 sec

    It yields
    ---------
    news : json object
    """

    # prepare parameters
    d_begin = parse(begin_date)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all = []
        url = url_blogbase.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'content col-lg-8 col-md-7 col-sm-12 col-xs-12')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        urls = [url for url in links_all if is_matched(url)]

        # scrap
        for url in links_all:

            news_json = parse_page(url)
            if None == news_json:
                return None

            # check date
            d_news = news_json['date']
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

            # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)

def get_allblog_urls(begin_page=0, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_blogbase.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'content col-lg-8 col-md-7 col-sm-12 col-xs-12')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))

    return links_all

urlpress_base = 'https://bipartisanpolicy.org/press-release/page/{}'

def yield_latest_allpress(begin_date, max_num=10, sleep=1.0):
    """
    Artuments
    ---------
    begin_date : str
        eg. 2018-01-01
    max_num : int
        Maximum number of news to be scraped
    sleep : float
        Sleep time. Default 1.0 sec

    It yields
    ---------
    news : json object
    """

    # prepare parameters
    d_begin = parse(begin_date)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all = []
        url = urlpress_base.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'content col-lg-8 col-md-7 col-sm-12 col-xs-12')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        urls = [url for url in links_all if is_matched(url)]

        # scrap
        for url in links_all:

            news_json = parse_page(url)
            if None == news_json:
                return None

            # check date
            d_news = news_json['date']
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

            # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)

def get_allpress_urls(begin_page=0, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = urlpress_base.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'content col-lg-8 col-md-7 col-sm-12 col-xs-12')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))

    return links_all

def get_last_page_num():

    """
    Returns
    -------
    page : int
        Last page number.
        eg: 3 in 'https://bipartisanpolicy.org/search/korea?start&end&type%5B0%5D=post&type%5B1%5D=library&type%5B2%5D=press_release&orderby&paged=3'
    """
    def last_element(url):
        parts = [p for p in url.split('=') if p]
        return int(parts[-1])

    soup = get_soup('https://bipartisanpolicy.org/search/korea?paged=1')
    last_page = max(
        last_element(a.attrs['href'])
        for a in soup.select('a[class=page-numbers]')
    )

    return last_page
