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

from http.client import HTTPConnection

class TinyBuddhaWisdom:
    def scrape(self):
        h1 = HTTPConnection('www.tinybuddha.com')
        h1.request('GET', '/', 
        headers={
            'Accept':'text/html', 
            'Accept-Charset': 'iso-8859-1', 
            'Accept-Encoding': '',
            'Accept-Language': 'en-us,en;q=0.5',
            'Connection': 'keep-alive',
            'DNT': '1', 
            'Host': 'tinybuddha.com',
            'User-Agent': 'Mozilla/5.0'}
        )

        response = h1.getresponse()
        data = str(response.read(), 'utf-8')

        cut = data.split("Click for Quotes")[1]
        cut = cut.split('home-ad')[0]
        cut = cut[cut.find('<a'):cut.find('</a')]
        cut = cut[cut.find('>')+1:]
        return cut

print("Tiny Buddha: " + TinyBuddhaWisdom().scrape())
