# bipartisan_scraper

미국의 씽크탱크인(Bipartisan Policy Center)의 자료들(blog, press realease)을 받아오기 위한 크롤러입니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py 그리고 parser.py 총 세가지로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리합니다.
scraper는 util.py내의 사이트내의 url 링크들을 get_soup함수를 통해 모아줍니다.
parser는 이렇게 만들어진 url리스트를 통해서 각 분석들의 제목/일자/내용을 모아줍니다.

```
python scraping_latest_news.py
```

```
[1 / 10] (Monday, February 4, 2019) Previewing the 2019 State of the Union
[2 / 10] (Thursday, January 31, 2019) A Roadmap for a DACA Deal
[3 / 10] (Thursday, January 31, 2019) Healthy Congress Index: 115th Congress Functioned Poorly, Derelict in Basic Duties
[4 / 10] (Thursday, January 31, 2019) Healthy Congress Index Q & A with John Fortier
[5 / 10] (Wednesday, January 30, 2019) State and Local Governments Take On Deferred Maintenance
[6 / 10] (Tuesday, January 22, 2019) Blockchain Shows Promise for Open Data, but Is Not a Silver Bullet
[7 / 10] (Tuesday, January 22, 2019) History Shows the U.S. Doesn’t Do Well at Preparing for Migration Crises
[8 / 10] (Thursday, January 17, 2019) GREAT(er) Transformation for Federal Grant Process Focus of House Bill
[9 / 10] (Friday, January 11, 2019) The House Has New Rules. Now It Needs Bold Leaders.
[10 / 10] (Wednesday, January 9, 2019) Where Will the Next Migrant Flow Come From? A Look at Venezuela and Nicaragua
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
