import requests
from bs4 import BeautifulSoup
from collections import defaultdict

def getRawHtml(pageUrl, sessionCookie):

    headers = {
        "Cookie": f"session={sessionCookie}"
    }

    response = requests.get(pageUrl, headers=headers)
    response.raise_for_status()
    return response.text



## items is a 2d array
def fillList(Arr1, Arr2, text):
    line = 0
    
    while(len(text) > 0):

        index1 = text.find(' ')
        index2 = text.find('\n')
        Arr1[line] = int(text[:index1])
        Arr2[line] = int(text[index1+1:index2])
        text = text[index2+1:]
        line += 1


        
# def findDifference():





def main():

    pageUrl = "https://adventofcode.com/2024/day/1/input"
    sessionCookie = "53616c7465645f5f4bbbbf992fb3a1b72dc263e30d9abbe167a35eb6c1f08188cc90b459bdf6e543ad0204885f37b4c0e8a4e8028fc3431453bcf646e1539e17"
    text = getRawHtml(pageUrl, sessionCookie)

    lines = text.count('\n')
    Arr1 = [0] * lines
    Arr2 = [0] * lines


    fillList(Arr1, Arr2, text)

    valueCounts = defaultdict(int)

    Arr1.sort()
    Arr2.sort()

    totalVal = 0

    for x in range(len(Arr1)):
        totalVal += abs(Arr1[x] - Arr2[x])
        
    
    print(totalVal)




if __name__ == "__main__":
    main()