# given a string remove the first and last letter and return the string 

def remove_char(s):
    return s[1 : -1]

# negative index does the same thing as len(s)-1 but for flex ;

def remove_char(s):
    return s[1:len(s)-1]
# this is how i wrote it the first time before realising . 

