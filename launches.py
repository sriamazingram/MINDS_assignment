import urllib.request
from bs4 import BeautifulSoup
import re
import dateutil.parser as parser
import datetime

# Starting from the 1st of January of the year 2019

start="2019 01 January"
start = parser.parse(start)
last_date = start
last_count = 0 # Keeping count for the initial days as 0

year = "2019"

# Fetching the article from Wikipedia

url = 'https://en.wikipedia.org/wiki/2019_in_spaceflight'
req = urllib.request.urlopen(url)
article = req.read().decode()

# Saving the article in HTML format.

with open('spaceflight.html', 'w') as fo:
    fo.write(article)

# Reading the article using BeautifulSoup and find the Orbital Launches table identified
# using the class identier.

article = open('spaceflight.html').read()
soup = BeautifulSoup(article, 'html.parser')
table = soup.find('table', class_='wikitable collapsible')

# Opening output.csv to write the final result

f = open("output.csv","w")
f.write("date,value\n")

final_date = ""

# Iterate each row in table to identify <td> with date and <td> with payload status.

all_rows = table.find_all('tr')[1:]
for r,row in enumerate(all_rows):
    for d,data in enumerate(row.find_all('td')):
        if data.has_attr("rowspan"):
            date = ""

            # The <td> with the date. Has atleast cells of 2 rows merged.

            if int(data["rowspan"])>1:
                date = data.text
                date = re.sub("[\(\[].*?[\)\]]", "", date)+year
                date = parser.parse(date)
                final_date = date

                # Write all previous dates including the last dage with accepted payload status to file.

                while last_date < date:
                    if last_date.date() == date.date():
                        if last_count == 0:
                            break
                    f.write(str(last_date.isoformat())+","+str(last_count)+"\n")
                    last_date = parser.parse(str(last_date.date()))+datetime.timedelta(days=1)
                    last_count = 0
                last_date = date
                last_count = 0
            else:
                # The <td> with payload status has a rowspan of 1.
                if int(data["rowspan"]) == 1:
                    result = data.text

                    # Count the number of accpeted payload statuses for the last date.

                    count_1 = result.count("Successful")
                    count_2 = result.count("Operational")
                    count_3 = result.count("En Route")
                    last_count += count_1+count_2+count_3

# Write last date with payload status to file.

f.write(str(final_date.isoformat())+","+str(last_count)+"\n")
last_count=0

# Writing remaining days 2019 with 0 value.

end_date = "31 December 2019"
end_date = parser.parse(end_date)
final_date = parser.parse(str(final_date.date()))+datetime.timedelta(days=1)
while final_date<=end_date:
    f.write(str(final_date.isoformat())+","+str(last_count)+"\n")
    final_date = parser.parse(str(final_date.date()))+datetime.timedelta(days=1)

# Closing the file.

f.close()
