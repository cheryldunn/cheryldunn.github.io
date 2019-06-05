words = ['color','color','colour','amok','amok','amuck','adviser','advisor','adviser','pepper']

canonical_spellings = ['color','amuck','adviser','pepper']

#make a dictionary pairing the variants with canonical canonical_spellings

mappings = {"colour":"color", "amok":"amuck", "advisor":"adviser"}

#make an empty list
new_list = []

#compare the words in some way - a la stemming
#loop over the list of words
for word in words:
    #if a word is misspelled, correct the spelling using the mappings dictionary and add the corrected word to the list
    if word in mappings:
        corrected_word = mappings[word]
        new_list.append(corrected_word)
    else:
        new_list.append(word)

print(new_list)
