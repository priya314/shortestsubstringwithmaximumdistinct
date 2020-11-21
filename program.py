from collections import defaultdict as dictionary
def findMinimumSubString(string):

    length = len(string) 
    distinctCount = len(set([givenString for givenString in string])) 
    startIndex = 0
    minimumLength = length
    total = 0
    begin = 0
    currentCount = dictionary(lambda: 0) 
    
    for index in range(length): 
        currentCount[string[index]] += 1
        if currentCount[string[index]] == 1: 
            total += 1
        if total == distinctCount: 
            while currentCount[string[begin]] > 1: 
                if currentCount[string[begin]] > 1: 
                    currentCount[string[begin]] -= 1
                begin += 1
            len_window = index - begin + 1
            if minimumLength > len_window: 
                minimumLength = len_window 
                startIndex = begin
    return len(string[startIndex: startIndex + minimumLength])
givenString = input()
print(findMinimumSubString(givenString))
