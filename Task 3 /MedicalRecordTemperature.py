#!/bin/python3

import math
import os
import random
import re
import sys
import requests



def getAverageTemperatureForUser(userId):
    page = 1
    total_records = float('inf')
    temperatures = []
    
    while total_records > 0:
        url = f"https://jsonmock.hackerrank.com/api/medical_records?userId={userId}&page={page}"
        response = requests.get(url).json()
        data = response['data']
        total_records = response['total']
        
        for record in data:
            temperatures.append(record['vitals']['bodyTemperature'])
        
        if len(data) == 0:
            break
        page += 1
    
    if temperatures:
        average = sum(temperatures) / len(temperatures)
        return f"{average:.1f}"
    return "0"

fptr = open(os.environ['OUTPUT_PATH'], 'w')

userId = int(input().strip())

result = getAverageTemperatureForUser(userId)

fptr.write(result + '\n')

if __name__ == '__main__':
    fptr.close()
