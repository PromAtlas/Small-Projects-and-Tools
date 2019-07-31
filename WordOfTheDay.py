import requests
import re
from bs4 import BeautifulSoup

#These two lines make the request and initiate the html parser
url = 'https://www.merriam-webster.com/word-of-the-day'
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')

#Scrape word
word = soup.h1.string
print("The word of the day is:", word)

#Scrape parts of speech
pos =  soup.find('span',"main-attr").string
print("The parts of speech are:", pos)


#Scrape phonetic spelling
pronunciation = soup.find('span',"word-syllables").string
print("The phonetic spelling is:", pronunciation)

#Scrape the definitions
definitionListings = soup.find('div','wod-definition-container').find_all('strong')
definitions = soup.find('div','wod-definition-container').find_all('p')

print("The defintion(s) are: ")

#Removes any non alphanumerical characters picked up in the list
pattern = "[a-zA-Z0-9_.-]"
for x in range (len(definitionListings)-1):
    if not re.match(pattern, definitionListings[x].string[0]):
        definitionListings.pop(x)

#Casts tags to string, then uses regex to remove all tags
for x in range (len(definitionListings)-1):
    definitions[x] = str(definitions[x])
    definitions[x] = re.sub('<[^>]*>', '', definitions[x])
    print(definitions[x])
