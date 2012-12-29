"""
This file is part of tinybuddha-wisdom.

tinybuddha-wisdom is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

tinybuddha-wisdom is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with tinybuddha-wisdom.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys

major_version = sys.version[:3].split('.')[0]

if(major_version == '2'):
    from httplib import HTTPConnection
if(major_version == '3'):
    from http.client import HTTPConnection

class TinyBuddhaWisdom:
    def fetch(self):
        try:
            h1 = HTTPConnection('tinybuddha.com')       
            h1.request('GET', '/wp-content/plugins/tiny-buddha-host/wisdom.txt') 
        except Exception:
            return "\"If you are patient in one moment of anger " +\
                   "you will escape one hundred days of sorrow.\" " +\
                   "-Chinese Proverb" 

        headers={
            'Accept':'text/html', 
            'Accept-Charset': 'iso-8859-1', 
            'Accept-Encoding': '',
            'Accept-Language': 'en-us,en;q=0.5',
            'Connection': 'keep-alive',
            'DNT': '1', 
            'Host': 'tinybuddha.com',
            'User-Agent': 'Mozilla/5.0'}        

        response = h1.getresponse()

        if(major_version == '2'):
            data = str(response.read())

        if(major_version == '3'):
            data = str(response.read(), 'utf-8')

        return data 

def main():
    print("Tiny Buddha: " + TinyBuddhaWisdom().fetch())
