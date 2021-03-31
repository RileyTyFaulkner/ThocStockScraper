import requests #To retrieve Stock Info
import re #For dissecting raw HTML grabbed via Requests
import numpy #For comparing New Stock List and Old Stock List
import os #For overwriting Old stock with evaluated New stock
import time

def getCurrentStock(type):
    global matches
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-GPC': '1',
    'DNT': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
    }
    response = requests.get('https://thocstock.com/'+type, headers=headers)
    uncleaned = response.text
    pattern =r'<h2 class=\"text-lg\">\s*.*?\s*>\s*(.*?)\n\s*<\/a>'
    matches = re.findall(pattern,uncleaned)
    listToStr = map(str,matches)
    stringForFile = '\n'.join(listToStr)
    fileName = "New {} Stock.txt".format(type)
    with open(fileName, "w") as file:
        file.write(stringForFile)

def overwriteOldStock(type):
    oldFile = "Old {} Stock.txt".format(type)
    newFile = "New {} Stock.txt".format(type)
    os.remove(oldFile)
    os.rename(newFile,oldFile)

def getOldStock(type):
    with open("Old {} Stock.txt".format(type)) as file:
        oldStock = file.read().split('\n')
    return(oldStock)

def findDifference(type):
    oldStock = getOldStock(type)
    currentStock = matches
    difference = len(numpy.setdiff1d(currentStock,oldStock))>0
    if difference:
        print("{}: New Stock found! New items:".format(type))
        print(difference)
        print("Old Stock: {}".format(oldStock))
        print("New Stock: {}".format(currentStock))
        print("Old Stock overwritten.")
        overwriteOldStock(type)
    else:
        print("{}: No new Stock, old stock overwritten.".format(type))
        overwriteOldStock(type)

types = ['keycaps', 'accessories', 'deskpads', 'keyboards', 'pcbs', 'stabs', 'switches', 'switch-mod']

#This could be done with the Schedule module
x = 1
while x:
    for stock in types:
        getCurrentStock(stock)
        findDifference(stock)
    time.sleep(600)
