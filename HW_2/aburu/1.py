import this
import codecs
import os
os.system('cls' if os.name == 'nt' else 'clear')
# use codecs module for encoding this.py and write in 1 row 
s = str(codecs.encode(this.s, 'rot13').split('\n'))

#count is, better, never 
substring = "is"
find_better = "better"
find_never = "never"

count1 = s.count(substring)
count2 = s.count(find_better)
count3 = s.count(find_never)
print ('count of is =' + str(count1))
print ('count of better =' + str(count2))
print ('count of never =' + str(count3))  

# # to upper case 
# print (s.upper()) 
# # replace each "i" to "&"
# print (s.replace('i','&'))

# open(file).read().split('\n') need to check 
