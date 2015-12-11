import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from lxml import html

class Render(QWebPage):
  def __init__(self, url):
    self.app = QApplication(sys.argv)
    QWebPage.__init__(self)
    self.loadFinished.connect(self._loadFinished)
    self.mainFrame().load(QUrl(url))
    self.app.exec_()

  def _loadFinished(self, result):
    self.frame = self.mainFrame()
    self.app.quit()


url = 'http://www.apple.com/retail/internationalplaza/'
#This does the magic.Loads everything
r = Render(url)

#result is a QString.
result = r.frame.toHtml()

#QString should be converted to string before processed by lxml
formatted_result = str(result.toAscii())

#Next build lxml tree from formatted_result
tree = html.fromstring(formatted_result)

#Now using correct Xpath we are fetching URL of archives
relative_hours_path = \
  '//section[@class="section section-store-calendar' +\
  ' section-fullwidth"]' +\
  '/div[@class="section-content"]' +\
  '/div[@class="store-calendar-view"]' +\
  '//div[@class="time column large-2 large-pull-9' +\
  ' medium-3 medium-pull-7 small-12 small-pull-0"]/text()'
relative_hours = tree.xpath(relative_hours_path)

print relative_hours