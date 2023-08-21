"""
assignmentOne.py
The Assignment 1 of COMP1112-01-235

Developer : Dain Shin
Date: June 13, 2023
"""

# Open the 'sample.txt' by using the open method
file = open("sample.txt", "r")

fileText = file.read()  # Reading the whole file

# Organising the text to split and put into a list
fileWord = fileText.lower()   
fileWord = fileWord.replace(',', ' ').replace('.', ' ').replace('-', ' ').replace('"', ' ').replace('\'', ' ').replace('?', ' ').replace('!', ' ').replace('\n', ' ')
fileWord = fileWord.strip()
fileWord = fileWord.split(' ')

countI = 0   
countThe = 0   
countAnd = 0

for i in range(len(fileWord)):
    if fileWord[i] == "i" :
        countI += 1
    elif fileWord[i] == "the":
        countThe += 1
    elif fileWord[i] == "and":
        countAnd += 1

# printing out the result
print("Word         Frequency")
print("I       |     "  + str(countI))
print("the     |     "  + str(countThe))
print("and     |     "  + str(countThe))

print("\n===========================\n")

# Making fileWord(list) to wordDict(dictionary)
# The key is word, the value is the number of the word
wordDict = {}
for i in fileWord:
    if i.strip() != '':  # if the word is not space
        if i in wordDict:  # if the word in fileWord exist in wordDict, add the the count number
            wordDict[i] += 1
        else:              # if the word in fileWord doesn't exist in wordDict, the count number is 1
            wordDict[i] = 1

# The least frequent words(Those appear only once in the sample.txt)
for key, value in wordDict.items():
    if value == min(wordDict.values()):
        print("Least Frequent value: " + key+ ", "+ str(value) )
    
print("\n===========================\n")

# The most frequent word
for key, value in wordDict.items():
    if value == max(wordDict.values()):
        print("Most Frequent value: " + key+ ", "+ str(value) )

# file close
file.close()