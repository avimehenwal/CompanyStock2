#!/usr/bin/env python

#AUTHOR     :   Avi Mehenwal
#DATED      :   11th-Dec-2013

import csv
import os


INPUT_DIR = '/home/avimehenwal/Documents/Projects/CompanyStock/CompanyStock2'
filename = 'data.csv'
answer = []

def fetchShareValue(companyIndex):
#function to fetch Share value from answer data structure
    return answer[companyIndex][companyIndex]['MaximumShareValue']

def updateCompanyData(companyIndex, year, month, new_ShareValue):
#function to update share, montt and year values in answer ds    
    answer[companyIndex][companyIndex]['MaximumShareValue'] = new_ShareValue
    answer[companyIndex][companyIndex]['month'] = month
    answer[companyIndex][companyIndex]['year'] = year
    return 'Record updated'
    
    
#MAIN
with open(os.path.join(INPUT_DIR,filename), 'rb') as infile:
    #creating reader object for csv
    reader = csv.reader(infile)
    line_no = 0
    
    for row in reader:
        item_no = 0
        
        if line_no == 0 :           #csv header section creates sample answer data structure that stores the problem answer.
            for item in row[2:]:
                itemDict = {}
                itemDict[item_no] = { 'MaximumShareValue':0,
                                      'month':'',
                                      'year':0,
                                      'companyName':item     }
                answer.append(itemDict)
                item_no += 1
        
        else :                      #csv data section that deals with updating answer DS by comparing with required data
            for item in row:
                if item_no == 0:
                    year = item
                elif item_no == 1:
                    month = item
                elif item_no > 1:
                    new_ShareValue = item
                    old_ShareValue = fetchShareValue(item_no-2)
                    if new_ShareValue > old_ShareValue:
                        updateCompanyData(item_no-2, year, month, new_ShareValue)
                item_no += 1
        line_no += 1    
            
print answer
