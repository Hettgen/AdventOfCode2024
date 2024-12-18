'''
Red-Nosed Reports

Dataset is a string of numbers, separated by spaces, each new line delimited by a newline.

Goal : Check each line for safety,
Lines are safe when:
    1. The numbers are either all in increasing or decreasing order. Can not swap
    2. Any 2 adjacent numbers are between 1 and 3 apart
'''

import requests


def requestHtml(url, sessionCookie):
    
    headers = {
        "Cookie": f"session={sessionCookie}"
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def checkSafety(text):

    lines = text.count("\n")
    validatedLevels = [0] * lines

    while(len(text) > 0):



def checkLine(line):

    totalNumbers = line.count(' ') + 1
    numbers = [0] * totalNumbers

    for x in numbers:
        space = line.find(' ')
        numbers[x] = int(line[:space])
        text = text[space+1:]


    
    #using boolean value to track if increasing or decreasing. Increasing == true, Decreasing == false

    direction:bool = False if numbers[0] > numbers[1] else True

    for x in range(1,len(numbers)):
        
        if(direction):
            if(numbers[x] <= numbers[x-1] | numbers[x] > numbers[x-1] + 3):
                return False
        else:
            if(numbers[x] >= numbers[x-1] | numbers[x] < numbers[x-1] - 3):
                return False

    return True





def main():

    url = 'https://adventofcode.com/2024/day/2/input'
    sessionCookie = '53616c7465645f5fcdde4f3fd0b01830e3f05c8208a401c2f30aec774c7717cd1bdef9938620f66cc5bca2e04711d0325fdae3f47e7fb0e94bed8926d9ccc01b'
    
    return 0

if __name__ == '__main__':
    main()

