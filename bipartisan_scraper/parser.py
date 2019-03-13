from .utils import get_soup
from .utils import now
<<<<<<< HEAD

def parse_page(url):
    if 'blog/' in url:
        return parse_blog(url)
    if '/press-release/' in url:
        return parse_press_release(url)
    return None
=======
from dateutil.parser import parse

def parse_page(url):
    try:
        if 'blog/' in url:
            return parse_blog(url)
        if '/press-release/' in url:
            return parse_press_release(url)
    except Exception as e:
        print(e)
        print('Parsing error from {}'.format(url))
        return None
>>>>>>> final commit

def parse_blog(url):
    def parse_author(soup):
        author = soup.find('div', class_='meta').text
        if not author:
            return ''
        return author[3:]

    def parse_title(soup):
        title = soup.find('h1').text
        if not title:
            return ''
        return title

    def parse_date(soup):
<<<<<<< HEAD
        date = soup.find('p', class_= 'date').text
        if not date:
            return ''
        return date
=======
        date = soup.find('p', class_= 'date')
        if not date:
            return ''
        return parse(date.text)
>>>>>>> final commit

    def parse_content(soup):
        temp_content = soup.find('div', class_= 'post').find_all()
        content = '\n'.join([p.text.strip() for p in temp_content])
        if not content:
            return ''
        return content

    soup = get_soup(url)
<<<<<<< HEAD
    return {
=======
    json_object = {
>>>>>>> final commit
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'author': parse_author(soup),
<<<<<<< HEAD
        'content': parse_content(soup)
    }
=======
        'content': parse_content(soup),
        'scrap_time' : now()
    }
    if None in json_object:
        return None
    return json_object
>>>>>>> final commit

def parse_press_release(url):
    def parse_title(soup):
        title = soup.find('h1')
        if not title:
            return ''
        return title.text

    def parse_date(soup):
        span = soup.find('p', class_ = 'date')
        if not span:
            return ''
<<<<<<< HEAD
        return span.text
=======
        return parse(span.text)
>>>>>>> final commit

    def parse_content(soup):
        p = soup.find('div', class_ = 'post')
        if not p:
            return ''
        return p.text

    soup = get_soup(url)
<<<<<<< HEAD
    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'content': parse_content(soup)
    }
=======
    json_object = {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'content': parse_content(soup),
        'scrap_time' : now()
    }
    if None in json_object:
        return None
    return json_object
>>>>>>> final commit
