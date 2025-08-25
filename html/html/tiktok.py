from bs4 import BeautifulSoup
import requests

url ='https://www.tiktok.com/login?redirect_url=https%3A%2F%2Fwww.tiktok.com%2F%3Flang%3Den&lang=en&enter_method=mandatory'
resposta = requests.get(url)    

conteudo_html = resposta.content

soup = BeautifulSoup(conteudo_html,'html.parser')

links = soup.find_all('h2')

for link in links:
    print("Texto:{%s}, URL:{%s}"%(link.text, link.get('href')))