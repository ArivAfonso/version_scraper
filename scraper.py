import requests
import bs4

def swift():
    swift_website = requests.get("https://swift.org/download/").text
    soup = bs4.BeautifulSoup(swift_website, 'lxml')

    match = soup.find('article', class_='page')
    version = match.h3.text
    print(version)

def python():
    python_website = requests.get("https://www.python.org/downloads/").text
    soup = bs4.BeautifulSoup(python_website, 'lxml')

    match = soup.find('p', class_='download-buttons')
    version = match.a.text
    python = version.split('Download ')[1]
    print(python)

def coffeescript():
    swift_website = requests.get("https://coffeescript.org/#introduction").text
    soup = bs4.BeautifulSoup(swift_website, 'lxml')

    match = soup.find('main', class_='main').section
    third_p = match.find("p").find_next_sibling("p").find_next_sibling("p")
    version = third_p.a.text
    print('CoffeeScript ' + version)

def groovy():
    swift_website = requests.get("https://groovy.apache.org/download.html").text
    soup = bs4.BeautifulSoup(swift_website, 'lxml')

    match = soup.find('div', class_='col-lg-8 col-lg-pull-0')
    second_article = match.find("article").find_next_sibling("article")
    second_h = match.find("h3").find_next_sibling("h3").find_next_sibling("h3")
    text = second_h.text
    groovy = text.split(' distributions')[0]
    print("Groovy " + groovy)

def perl():
    swift_website = requests.get("https://www.perl.org/get.html").text
    soup = bs4.BeautifulSoup(swift_website, 'lxml')

    match = soup.find('div', class_='col-xs-12')
    version = match.p.text
    m = version.split("currently")[1]
    n = m.split(".  If")[0]
    print('Perl' + n)

def ruby():
    swift_website = requests.get("https://swift.org/download/").text
    soup = bs4.BeautifulSoup(swift_website, 'lxml')

    match = soup.find('div', id='content')
    version = match.ul.li.a.text
    print(version)
