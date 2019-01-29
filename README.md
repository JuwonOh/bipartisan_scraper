# bipartisan_scraper

미국의 씽크탱크인(Bipartisan Policy Center)의 검색자료들(korea를 검색한 blog자료)을 받아오기 위한 크롤러입니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py 그리고 parser.py 총 세가지로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리합니다.
scraper는 util.py내의 사이트내의 url 링크들을 get_soup함수를 통해 모아줍니다.
parser는 이렇게 만들어진 url리스트를 통해서 각 분석들의 제목/일자/내용을 모아줍니다.

```
python scraping_latest_news.py
```

```
[1 / 50] (Monday, August 6, 2018) The Goal is Workable Bipartisanship
Stop scrapping. 1 / 50 news was scrapped
The oldest news has been created after 2018-07-01

```

특정한 페이지를 parse하기 위해서는

```python
from bipartisan_scraper import parse_page
from bipartisan_scraper import get_allnews_urls

urls = get_allnews_urls(begin_page=1, end_page=3, verbose=True)
for url in urls[:3]:
    json_object = parse_page(url)    
```

## 참고 코드

본 코드는 https://github.com/lovit/whitehouse_scraper를 참조하여 만들어졌습니다.
