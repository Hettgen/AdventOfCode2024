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




# Second Half of Question
def countSimilarity(arr1, arr2):
    
    valueCounts = defaultdict(int)

    for value in arr2:
        valueCounts[value] += 1

    finalCount = 0

    for value in arr1:
        x = valueCounts[value]

        if(x > 0):
            finalCount += x * value

    return finalCount





def main():

    pageUrl = "https://adventofcode.com/2024/day/1/input"
    sessionCookie = "53616c7465645f5fcdde4f3fd0b01830e3f05c8208a401c2f30aec774c7717cd1bdef9938620f66cc5bca2e04711d0325fdae3f47e7fb0e94bed8926d9ccc01b"
    text = getRawHtml(pageUrl, sessionCookie)

    lines = text.count('\n')
    arr1 = [0] * lines
    arr2 = [0] * lines


    #1st part of question
    fillList(arr1, arr2, text)

    valueCounts = defaultdict(int)

    arr1.sort()
    arr2.sort()

    totalVal = 0


    for x in range(len(arr1)):
        totalVal += abs(arr1[x] - arr2[x])
        
    
    print(totalVal)

    #2nd part
    totalSimilarities = countSimilarity(arr1, arr2)
    print(totalSimilarities)




if __name__ == "__main__":
    main()