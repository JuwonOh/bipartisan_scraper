# bipartisan_scraper

미국의 씽크탱크인 Bipartisan Policy Center(https://bipartisanpolicy.org)의 자료들(blog, press realease)을 받아오기 위한 크롤러입니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py, parser.py 그리고 scraping_latest_news.py 총 네가지로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리하는 등 scraper가 필요한 기본적인 기능을 가지고 있습니다.
parser.py는 모아진 url리스트를 통해서 각 분석들의 제목/일자/내용 등의 문자, 시간 데이터들을 parsing 합니다.
scraper.py는 사이트내의 url 링크들을 get_soup함수를 통해 모아주고, parser를 통해서 json형식으로 변환시킵니다.
scraping_latest_news.py는 scraper.py를 통해 만들어진 json파일을 저장시켜줍니다. scraping_latest_news.py파일의 parameter는 다음과 같습니다.

Using Python script with arguments

| Argument name | Default Value | Note |
| --- | --- | --- |
| begin_date | 2018-07-01 | datetime YYYY-mm-dd |
| directory | ./output/ | Output directory |
| max_num | 1000 | Maximum number of news to be scraped |
| sleep | 1.0 | Sleep time for each news |
| verbose | False, store_true | If True use verbose mode |

만일 2018년 7월 1일부터 작성된 자료를 1000개까지 받고 싶다면 다음과 같이 실행코드를 입력해주시면 됩니다.

```
scraping_latest_news.py --begin_date 2018/07/01 --directory ./output --max_num 1000 --sleep 1.0
```
최근 순서대로 크롤링한 파일을 살펴보고 싶을때는 usage.ipynb를 사용하세요.

```
from bipartisan_scraper import parse_page
from bipartisan_scraper import get_allnews_urls

urls = get_allnews_urls(begin_page=1, end_page=3, verbose=True)
for url in urls[:3]:
    json_object = parse_page(url)    
    
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
## 참고 코드

본 코드는 https://github.com/lovit/whitehouse_scraper를 참조하여 만들어졌습니다.

