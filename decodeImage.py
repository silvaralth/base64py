# -*- coding: utf-8 -*-
#!/usr/bin/python

import base64
import sys
import csv

csv.field_size_limit(sys.maxsize)
arr = []

# decode an image
def decodeStr(stringb64, fileName, extensionFile):
  decodeImbg = base64.b64decode(stringb64)
  image_result = open(fileName + extensionFile, 'wb')
  image_result.write(decodeImbg)
  image_result.close()

# return the file type
def assignExtension(extensionStr):
  if extensionStr == 'JPG_B64':
    return '.jpg'
  else:
    return '.png'

# Read a csv and build an array
def readCSV():
  strb64 = 'Valor'
  formatb64 = 'Formato'
  #logic
  lector = open('imgbk.csv', 'r')
  temp = lector.readline()
  headArr = temp.split(';')
  #setting variables
  strb64pos = headArr.index(strb64)
  formatb64pos = headArr.index(formatb64)
  lector.close()
  # csv test
  with open('imgbk.csv', 'r', newline = "") as file:
    reader = csv.reader(file, delimiter = ';')
    for row in reader:
      tmpList = [row[strb64pos], row[formatb64pos]]
      arr.append(tmpList)

def main():
  readCSV()
  # decode & export
  arrayLong = len(arr)
  i = 1
  while i < arrayLong:
    decodeStr(arr[i][0], str(i), assignExtension(arr[i][1]))
    i += 1
  # end :)
  print("Process finished")

if __name__== "__main__":
  main()