#import all required libraries
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

#extracting html code from the webpage url
Webpage = urllib.request.urlopen("https://docs.python.org/3.11/library/itertools.html#module-itertools")
soup = bs(Webpage)

#extracting function labels from the webpage
Labels = soup.body.findAll('dt')
function_labels = re.findall('id="itertools.\w+', str(Labels))
function_labels = [item[4:] for item in function_labels]

#extracting function definition from the webpage
Definition = soup.body.findAll('dd')
function_details = []

for item in Definition:
  item = item.text
  item = item.replace('\n', ' ')
  function_details.append(item)

print(function_labels)
print(function_details)

#creating a dataframe for the extracted data from the webpage
data = pd.DataFrame({'Function Labels': function_labels, 'Function Details': function_details})
data.head()

#exporting the dataframe to a csv file
data.to_csv('itertools')



