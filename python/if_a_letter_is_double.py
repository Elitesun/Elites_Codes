def duplicate_encode(word):
    word= word.lower()
    return "".join(")" if word.count(i)>1 else "(" for i in word)


# if a letter is double in the word replace it with ) else if it only appears once replace it with (