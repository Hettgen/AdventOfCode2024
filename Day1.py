import requests
from bs4 import BeautifulSoup

def getRawHtml(pageUrl, sessionCookie):

    headers = {
        "Cookie": f"session={sessionCookie}"
    }

    response = requests.get(pageUrl, headers=headers)
    response.raise_for_status()
    return response.text



## items is a 2d array
def fillList(items, text):

    x = 0
    line = 0
    
    while(len(text) > 0):

        index1 = text.find(' ')
        index2 = text.find('\n')
        items[line][0] = int(text[:index1])
        items[line][1] = int(text[index1+1:index2])
        text = text[index2+1:]
        line += 1


        
def findDifference():





def main():

    pageUrl = "https://adventofcode.com/2024/day/1/input"
    sessionCookie = "53616c7465645f5fcdde4f3fd0b01830e3f05c8208a401c2f30aec774c7717cd1bdef9938620f66cc5bca2e04711d0325fdae3f47e7fb0e94bed8926d9ccc01b"
    text = getRawHtml(pageUrl, sessionCookie)

    print(type(text))

    textList = [[None for _ in range(2)] for _ in range(text.count('\n'))]

    fillList(textList, text)
    print(textList)




if __name__ == "__main__":
    main()