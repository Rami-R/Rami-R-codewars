#DESCRIPTION:
#You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:

#As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

#Example (Input --> Output)

#"Hello World" --> "World Hello"
#"Hi There." --> "There. Hi"

# My solution :

def reverse(st):
    # Remove leading and trailing whitespace
    st = st.strip()
    # Split the string into words
    my_list = st.split()
    # Reverse the list of words
    list_reversed = my_list[::-1]
    # Join the reversed list of words into a string
    text_reversed = " ".join(list_reversed)
    return text_reversed
