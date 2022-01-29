
'''
    访问美国的https://www.electronicsweekly.com网站，分别对google news（数量较少）和本网站的进行爬取
'''
import requests
import bs4
import os
import datetime
import time
import  xml.dom.minidom
import re

def getUrl(url):
    '''
        访问url的网页，获取网页内容并返回HTML内容。
    '''
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print(url)
        return "exception!"

def getUrlLink():
    linkList = []
    front = "https://www.reuters.com/pf/api/v3/content/fetch/articles-by-search-v2?query=%7B%22keyword%22%3A%22China%20chip%22%2C%22offset%22%3A"

    back = "%2C%22orderby%22%3A%22relevance%22%2C%22size%22%3A10%2C%22website%22%3A%22reuters%22%7D&d=69&_website=reuters"
    i = 0
    while i < 10:
        url = front + str(i) + back
        linkList.append(url)
        i += 10
    return linkList

def getNewsUrl(url):
    html = getUrl(url)
    print(html)
    soup = bs4.BeautifulSoup(html,'html.parser')
    items=soup.find_all('div',attrs={'class':'item-details'})
    linkList=[]
    for item in items:
        link=item.find('a')['href']
        linkList.append(link)
    #print(linkList)
    return linkList

def getTitle(title):
    title = title.replace(":",".")
    title = title.replace("?",".")
    title = title.replace("/",".")
    title = title.replace("\\",".")
    title = title.replace("*",".")
    title = title.replace("\"",".")
    title = title.replace("<",".")
    title = title.replace(">",".")
    title = title.replace("|",".")
    return title

def getContent(soup):
    #article = soup.find('div',attrs = {'class':'post-inner'})
    #item= article.find_all('p')
    article = soup.find('div',attrs={'class':'td_block_wrap tdb_single_content tdi_149 td-pb-border-top td_block_template_1 td-post-content tagdiv-type'})
    items = article.find_all('p')
    ret = ""
    for item in items:
        ret = ret + item.get_text()
    return ret


def getDetail(url):
    html = getUrl(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')

    title = soup.find('h1', attrs={'class': 'tdb-title-text'}).string
    title = getTitle(title)

    area = soup.find('div', attrs={
        'class': 'td_block_wrap tdb_single_date tdi_146 td-pb-border-top td_block_template_1 tdb-post-meta'})
    time = area.find('time', attrs={'class': 'entry-date updated td-module-date'}).string
    content = getContent(soup)

    infoList = []
    infoList.append(title)
    infoList.append(time)
    infoList.append(content)
    # print(infoList)
    return infoList

def saveFile(content,path,filename):
    '''
        将内容为content、名字为filename的文件保存在path中
    '''
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + filename,'w',encoding = 'utf-8') as f:
        f.write(content)

def download_news(infoList):
    print(infoList)
    title = infoList[0]
    time = infoList[1]
    content = infoList[2]
    filename = time + ' ' + title + '.txt'
    path = "C:/Users/song/All about learning/news"
    saveFile(content,path,filename)

if __name__ == '__main__':
    linkList = getUrlLink() #从googlenews的xml文件获取所有文章列表
    #print(linkList)
    print(len(linkList))
    num = 0
    while num < len(linkList):
        try:
            url = linkList[num]
            links = getNewsUrl(url)
            print(links)
            for link in links:
                print("enter for")
                infoList = getDetail(link)
                download_news(infoList)
                print("infoList: ")
                print(infoList)
            # print("page " + str(num))
            num = num + 1
        except:
            print("error occurs")
            num = num + 1
            pass
            continue
