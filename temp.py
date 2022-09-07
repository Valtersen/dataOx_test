from bs4 import BeautifulSoup
import requests
import time



# my_html = """
#       <p>Alex/p>
#       <div class="names">
#             Molly
#              <p>Bob</p>
#              <p>Cathy</p>
#       </div>
# """
html = """    <div class="price">
     $3,600.00
     <div class="price-drop-parent">
      <div class="price-drop">
       <span class="value">
        $3,700.00
       </span>
      </div>
     </div>
    </div>
"""

soup = BeautifulSoup(html)

m = soup.find('div', class_='price')
d = m.find('div', class_='price-drop-parent')
d.extract()

print(m.text.strip())

















# page = 80

# info = requests.get(f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273', allow_redirects=False)
# print(info.status_code)
# print(info.history)
#
# if info.status_code == 200:
#     parsed = BeautifulSoup(info.text, "html.parser")
#     showed = parsed.find('span', class_='resultsShowingCount-1707762110').text.strip()
#     title = parsed.find('h1', class_='resultsHeading-1285903303').text.strip()
#     print(showed)
#     print(title)
#     #
    # ad = parsed.find_all('div', 'search-item')[3]
    # ad_id = ad['data-listing-id']
    # print('ad id', ad_id)
    # link = 'https://www.kijiji.ca' + ad.find('a', class_='title', href=True)['href'].strip()
    # print(link)
    # title = ad.find('a', class_='title').text.strip()
    # print(title)
    # beds = ad.find('span', class_='bedrooms').text.replace("Beds:", "").strip()
    # print(beds)

#find_all(
#     "h2", string=lambda text: "beds:" in text.lower()
# )


# time.sleep(2.5)







