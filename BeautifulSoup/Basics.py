# If we want to scrape the website:
# 1.Use the API
# 2.HTML web scraping using some tools like bs4

# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup

url="https://www.codewithharry.com"

# ------------------------------------------------------------
# Get the HTML 
r=requests.get(url)
htmlcontent=r.content
print(htmlcontent)

# ------------------------------------------------------------
# Parse the HTML
soup=BeautifulSoup(htmlcontent,'html.parser')
print(soup.prettify)

# ------------------------------------------------------------
# HTML tree traversal

# Get the title from the page
title= soup.title
print(title)

# Get all the paragraphs from the page
paras=soup.find_all('p')
print(paras)

# Get all the anchors from the page
anchors=soup.find_all('a')
print(anchors)

# Get the first element of HTML page
print(soup.find('p'))

# Get the class of the element
print(soup.find('p')['class'])

# Find all elements with class lead
print(soup.find_all('p',class_='mt-2'))

# Get the text from the tags/soup
print(soup.find('p').get_text())

# Get all the links from the page
anchors=soup.find_all('a')
for i in anchors:
    linkText = url+ i.get('href')
    print(linkText)

# Comment
comment='<p><!-- This is comment--></p>'
soup2=BeautifulSoup(comment,'html.parser')
commentString=soup2.p.string
print(commentString)

# Commonly used type of Objects
# 1.Tag
# 2.NavigableString
# 3.BeautifulSoup
# 4.Comment
print(type(title))
print(type(title.string))
print(type(soup))
print(type(commentString))

# ------------------------------------------------------------

IDdata=soup.find(id="nav-content")

# .contents --> Tag's children are available as list
# .children --> Tag's children are available as generators
print(IDdata.contents)
for i in IDdata.children:
    print(i)

# For getting strings from IDdata 
for i in IDdata.strings:
    print(i)

# For getting the parent of the IDdata
print(IDdata.parent)
print(IDdata.parent.name)
# parents ---> create the generator
for i in IDdata.parents:
    print(i.name)

# next_sibling
print(IDdata.next_sibling)
# previous_sibling
print(IDdata.previous_sibling)
print(IDdata.previous_sibling.previous_sibling)
# It also takes br tag(empty line) as sibling

# for selecting id, use #
# for selecting class, use .
element=soup.select('#nav-content')
print(element)
element=soup.select('.text-center')
print(element)