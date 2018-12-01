import csv
import urllib.request
from bs4 import BeautifulSoup
f = open("dataOutput.csv", "w", newline="")
writer = csv.writer(f)

wholePage = BeautifulSoup(urllib.request.urlopen("https://biopharmguy.com/"
                                                 "links/country-netherlands-all-location.php").read())

tbody = wholePage("table", {"class":"rightLinks"})[0].find_all('tr')

for row in tbody:
    cols = row.findChildren(recursive=False)
    cols = [ele.text.strip() for ele in cols]
    writer.writerow(cols)
    print(cols)