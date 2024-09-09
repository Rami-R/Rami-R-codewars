'''Instructions
Input: Array of elements

["h","o","l","a"]

Output: String with comma delimited elements of the array in th same order.

"h,o,l,a"

Note2: the input data can be: boolean array, array of objects,
 array of string arrays, array of number arrays... '''

#My solution:
def print_array(arr):
    return ",".join(str(x) for x in arr)
    