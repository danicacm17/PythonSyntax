def print_upper_words(words, must_start_with=None):
    """Print each word in uppercase, only if it starts with one of the specified letters.
    
    words: list of words to process
    must_start_with: set of letters that words must start with
    """
    
    if must_start_with is None:
        must_start_with = set() # Default to an empty set

    must_start_with = {letter.upper() for letter in must_start_with}    

    for word in words:
        upper_word = word.upper()
        if upper_word[0] in must_start_with:
            print(upper_word)

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})