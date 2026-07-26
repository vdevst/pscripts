import requests, bs4, os

res = requests.get(r"https://github.com/qbittorrent/search-plugins/wiki/Unofficial-search-plugins")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')

data = soup.select('tr a')
urls = [link['href'] for link in data if '.py' in link['href']]

for url in urls:
    with open(os.path.basename(url), 'wb') as f:
        res = requests.get(url)
        if res.status_code == 404:
            continue
        for c in res.iter_content(100000):
            f.write(c)