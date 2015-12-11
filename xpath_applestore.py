from lxml import html
import requests

page = requests.get('http://www.apple.com/retail/internationalplaza/')
tree = html.fromstring(page.content)

#This will obtain the address

absolute_adress_path = '/html/body/div[@id="main"]/section' +\
              '[@class="section section-store-summary section-wide"]/' +\
              'div[@class="section-content"]/div[@id="gallery-mapSwap"]/' +\
              'div[@id="gallery-mapSwap-section-1"]/' +\
              'div[@class="store-details column large-4 medium-12 medium-pull-0"]/' +\
              'div[@class="column large-12 medium-6 small-12"]/span[@class="store-street"][1]/text()'

absolute_adress = tree.xpath(absolute_adress_path)

relative_adress_path = '//div[@class="column large-12 medium-6 small-12"]//span[@class="store-street"][1]/text()'
relative_adress = tree.xpath(relative_adress_path)

relative_hours_path = '//section[@class="section section-store-calendar section-fullwidth"]' +\
                      '/div[@class="section-content"]/div[@class="store-calendar-view"]'

relative_hours = tree.xpath(relative_hours_path)


print absolute_adress
print relative_adress
print relative_hours


