# You are asked to ensure that the first and last names of people begin with a 
# capital letter in their passports. 
# For example, alison heck should be capitalised correctly as Alison Heck.


def solve(s):
    # Split the input string into words
    words = s.split(" ")
    
    # Process each word:
    # - If the word exists (not empty) and doesn't start with a digit,
    #   capitalize it using word.capitalize()
    # - Otherwise keep the word as is
    # Then join all words back together with spaces
    return " ".join(
        word.capitalize() if word and not word[0].isdigit() else word 
        for word in words
    )

# i strugled in the beginning because of the space between the words and i was using str.tiltle() but some 
# words had digits in them and i was getting the wrong result.
# i used the solution from the internet and i understood the solution better.