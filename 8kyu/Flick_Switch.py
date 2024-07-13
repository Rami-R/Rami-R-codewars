#Instructions

#Task
#Create a function that always returns True/true for every item in a given list.
#However, if an element is the word 'flick', switch to always returning the opposite boolean value.

#Examples
#['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

#['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

#['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]

# my solution
def flick_switch(lst):
    result=[]
    stat= True
    for i in lst :
        if i != 'flick':
            result.append(stat)    
        else:
            stat = not stat
            result.append(stat)   
    return result 