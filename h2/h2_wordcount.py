import re
import unidecode

# my_file = 'mickiewicz.txt'
i = 0
# with open(my_file, 'r',encoding='utf-8') as f:
#     text = f.read
#     print(text)
#     lines = f.readline()
#     for line in lines:
#         for word in line.split():
#             i =+1
#             print("%i: %s" % (i,word))
d1 = {}
with open('mickiewicz.txt', 'r',encoding='utf-8') as f:
    # reading each line
    for line in f:
        # reading each word
        for word in line.split():
            #remove special chars
            word = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", word)
            #remove polish chars
            word = unidecode.unidecode(word)
            #create dict and increase value of key if the same as already existing
            d1[word] = d1[word] + 1 if word in d1 else 1
            # displaying the words
            #print(word)

for n in d1:
    print('WORD: '+'"'+n+'"'+' occurence times:', d1[n])