from .utils import get_soup
from .utils import now

def parse_page(url):
    """
    Argument
    --------
    url : str
        Web page url

    Returns
    -------
    json_object : dict
        JSON format web page contents
        It consists with
            title : article title
            time : article written time
            content : text with line separator \\n
            url : web page url
            scrap_time : scrapped time
    """

    try:
        soup = get_soup(url)
        title = soup.find('h1').text
        time = soup.find('p', class_= 'date').text
        author = soup.find('p', class_='author-callout').text[3:]
        temp_content = soup.find('div', class_= 'post').find_all()
        content = '\n'.join([p.text.strip() for p in temp_content])

        json_object = {
            'title' : title,
            'time' : time,
            'content' : content,
            'url' : url,
            'author' : author,
            'scrap_time' : now()
        }
        return json_object
    except Exception as e:
        print(e)
        print('Parsing error from {}'.format(url))
        return None
