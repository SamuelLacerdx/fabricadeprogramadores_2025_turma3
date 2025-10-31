import requests, os, bs4

url = "https://www.saopaulofc.net"
os.makedirs("são paulo", exist_ok= True)
while not url.endswith ("#"):
    print ("dowloanding page %s..." %url)
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
print(soup)
