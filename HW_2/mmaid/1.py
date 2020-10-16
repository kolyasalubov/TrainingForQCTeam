# HW Ex.1
string = """Beautiful is better than ugly.     
Explicit is better than implicit.  
Simple is better than complex.     
Complex is better than complicated.
Flat is better than nested.        
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never."""

print("Better counter = ",string.find("better"),"\n")
print("Never counter  = ", string.find("never"),"\n")
print("Is counter = ", string.find("is"),"\n")
print(string.upper(),"\n")
print(string.replace("i", "&"))