######################################################################################
##   An anagram is direct word switch or word play, the result of rearranging the   ## 
##   letters of a word or phrase to produce a new word or phrase, using all the     ##
##   original letters exactly once; for example, the word anagram can be rearranged ##
##   into nag-a-ram.                                                                ##
######################################################################################

import collections, pprint, time, os

start_time = time.time()
print('Creating word list...')
word_list = sorted(list(set([word.strip().lower() for word in open('/Users/padhya/Documents/Python_Code/Data/raw_word_list.txt')])))

def signature(word):
    return ''.join(sorted(word))

word_bysig = collections.defaultdict(list)
for word in word_list:
    word_bysig[signature(word)].append(word)

def anagram(myword):
    return word_bysig[signature(myword)]

print('Finding anagrams...')
all_anagrams = {word: anagram(word)
                for word in word_list if len(anagram(word)) > 1}

print('Writing anagrams to file...')
with open('/Users/padhya/Documents/Python_Code/Outputs/All_Anagrams.txt', 'w') as file:
    file.write('All_anagrams = \n')
    file.write(pprint.pformat(all_anagrams))

total_time = round(time.time() - start_time, 2)
print('\nCompleted Anagram finding with total --> '+ str(total_time) +' seconds.')