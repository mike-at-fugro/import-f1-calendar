#1. extract f1 start times
#2. import to calendar
#3. tkinter gui showing next race on page one, full list on page 2

#use BeautifulSoup to extract HTML content
from bs4 import BeautifulSoup


"""
    F1 Calendar XML
    - honestly cba splitting this up into lines
    - taken from https://www.formula1.com/en/latest/article/f1-announces-race-start-times-for-2025-season.490KLLD7T1AAM7wQl28tn6
"""
HTML_DATA = """<tbody><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Australia</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">March 16</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">15:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">04:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">China</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">March 23</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">15:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">07:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Japan</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">April 6</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">14:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">05:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Bahrain</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">April 13</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">18:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">15:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Saudi Arabia</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">April 20</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">20:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">17:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Miami</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">May 4</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">16:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">20:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Emilia-Romagna</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">May 18</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">15:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">13:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Monaco</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">May 25</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">15:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">13:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Spain</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">June 1</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">15:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">13:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Canada</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">June 15</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">14:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">18:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Austria</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">June 29</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">15:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">13:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Great Britain</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">July 6</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">15:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">14:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Belgium</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">July 27</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">15:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">13:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Hungary</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">August 3</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">15:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">13:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Netherlands</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">August 31</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">15:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">13:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Italy</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">September 7</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">15:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">13:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Azerbaijan</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">September 21</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">15:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">11:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Singapore</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">October 5</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">20:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">12:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">United States</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">October 19</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">14:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">19:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Mexico City</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">October 26</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">14:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">20:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Sao Paulo</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">November 9</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">14:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">17:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Las Vegas</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">November 22</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">20:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">04:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Qatar</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">November 30</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">19:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">16:00</td></tr><tr class="even:bg-concrete"><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">Abu Dhabi</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">December 7</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left font-bold">17:00</td><td class="p-[15px] font-titillium text-15 text-gray60 break-words text-left">13:00</td></tr></tbody>"""


#extract data from given tags
def extract(soup, row_tag, col_tag):

    data = []

    rows = soup.find_all(row_tag)

    for r in rows:
        cols = r.find_all(col_tag)
        row_data = [c.text for c in cols]
        data.append(row_data)

    return data


#parse html data
f1_soup = BeautifulSoup(HTML_DATA, 'html.parser')

#tags rows and columns of table
rt = 'tr'
ct = 'td'
extracted_data = extract(f1_soup, rt, ct)
print(extracted_data)#format: Country, Date, Local Time, GMT



