#DESCRIPTION:
#For every good kata idea there seem to be quite a few bad ones!
#In this kata you need to check the provided array (x) for good ideas 'good'
#  and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', 
# if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case,
#  return 'Fail!'.
#my Solution:
def well(x):
    j=0
    for i in x:
        if i =='good':
            j+=1
    if j>=1 and j<=2:
        return 'Publish!'
    elif j>2:
        return 'I smell a series!'
    else:
        return 'Fail!'