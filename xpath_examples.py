from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/002.html')
tree = html.fromstring(page.content)

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')

#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

#Title
title = tree.xpath('//title/text()[1]')

print buyers
print prices
print title


