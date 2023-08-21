"""
assignmentOne.py
The Assignment 1 of COMP1112-01-235

Developer : Dain Shin
Date: June 21, 2023
"""

# Open the 'sample.txt' by using the open method
file = open("sample.txt", "r")

fileText = file.read()  # Reading the whole file

# Organising the text to split and put into a list
fileWord = fileText.lower()   
fileWord = fileWord.replace(',', ' ').replace('.', ' ').replace('-', ' ').replace('"', ' ').replace('\'', ' ').replace('?', ' ').replace('!', ' ').replace('\n', ' ')
fileWord = fileWord.strip()
fileWord = fileWord.split(' ')


# Making fileWord(list) to wordDict(dictionary)
# The key is word, the value is the number of the word
wordDict = {}
for i in fileWord:
    if i.strip() != '':  # if the word is not space
        if i in wordDict:  # if the word in fileWord exist in wordDict, add the the count number
            wordDict[i] += 1
        else:              # if the word in fileWord doesn't exist in wordDict, the count number is 1
            wordDict[i] = 1

# Counting all the values that appeared in the text
print("Word                         Frequency") 
for key, value in wordDict.items():
    print(key.ljust(13) + "|".center(13) + str(value).rjust(10))            

# The least frequent words(Those appear only once in the sample.txt)
for key, value in wordDict.items():
    if value == min(wordDict.values()):
        print("Least Frequent value: " + key+ ", "+ str(value) )
    

# The most frequent word
for key, value in wordDict.items():
    if value == max(wordDict.values()):
        print("Most Frequent value: " + key+ ", "+ str(value) )

# file close
file.close()