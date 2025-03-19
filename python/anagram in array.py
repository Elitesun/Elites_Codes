def stringAnagram(dictionary, query):
    anadict = {}
    
    # Create a dictionary where the key is the sorted word and the value is a list of anagrams
    for w in dictionary:
        sword = ''.join(sorted(w))
        if sword in anadict:
            anadict[sword].append(w)
        else:
            anadict[sword] = [w]
    
    array = []
    
    # For each query, count how many anagrams exist in the dictionary
    for word in query:
        sorted_word = ''.join(sorted(word))
        times = len(anadict.get(sorted_word, []))  # Get the list of anagrams or empty list if not found
        array.append(times)
    
    print(array)
    return array  # Optionally return the result for further use
