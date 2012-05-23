import urllib2
from outgoingip import IP
from bs4 import BeautifulSoup

URL = 'http://whatismyipaddress.com/ip/'

class IP2Location(object):
    def __init__(self, ip=None):
        if not ip:
            ip = IP
        url = URL + ip
        req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
        content = urllib2.urlopen(req).read()
        self.__soup = BeautifulSoup(content)
        self.location = self.__get_location()
        self.business = self.__get_business()

    def __get_location(self):
        location = {}
        table = self.__soup.find_all('table')[1]
        text = table.get_text()
        loc_list = text.split('\n')
        for item in loc_list:
            if ':' in item:
                location[item.split(':')[0]] = item.split(':')[1]
        return location

    def __get_business(self):
        business = {}
        table = self.__soup.find_all('table')[0]
        for b in table.find_all('tr'):
            business[b.get_text().split(':')[0]] = b.get_text().split(':')[1]
        return business

    def get_location(self, key):
        if key in self.location:
            return self.location[key]
        else:
            return 'Invalid Query'

    def get_business(self, key):
        if key in self.business:
            return self.business[key]
        else:
            return 'Invalid Query'
