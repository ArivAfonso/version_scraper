import bs4
import requests


def pandas():
    pandas_website = requests.get("https://pandas.pydata.org/").text
    soup = bs4.BeautifulSoup(pandas_website, 'lxml')

    match = soup.find('div', class_='col-md-3')
    version = match.h4.text
    python = version.split('version: ')[1]
    print('Pandas '+python)

def numpy():
    numpy_website = requests.get("https://github.com/numpy/numpy/releases").text
    soup = bs4.BeautifulSoup(numpy_website, 'lxml')

    match = soup.find('div', class_='f1 flex-auto min-width-0 text-normal')
    version = match.a.text
    python = version.split('v')[1]
    print('Numpy '+python)


def aesara():
    aesara_website = requests.get("https://github.com/aesara-devs/aesara/releases").text
    soup = bs4.BeautifulSoup(aesara_website, 'lxml')

    match = soup.find('div', class_='f1 flex-auto min-width-0 text-normal')
    version = match.a.text
    python = version.split('v')[1]
    print('Numpy '+python)

def bootstrap():
    bootstrap_website = requests.get("https://getbootstrap.com/").text
    soup = bs4.BeautifulSoup(bootstrap_website, 'lxml')

    match = soup.find('p', class_='text-muted mb-0')
    version = match.strong.text
    python = version.split('v')[1]
    print('Bootstrap '+python)

