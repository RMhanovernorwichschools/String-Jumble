"""
stringjumble.py
Author: Rachel Matthew
Credit: none

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
string=input("Please enter a string of text (the bigger the better): ")
sl=len(string)

characters=[]
print_a=''
print_b=''
print_c=''

for x in range(0,sl):
    characters.append(string[x])
    
for x in range(0,sl):
    print_a=print_a+characters[sl-(x+1)]
    
print(print_a)

space_loci=[]
for x in range (0,sl):
    if characters[x]==' ':
        space_loci.append(x)

reverse_space_loci=space_loci[len(space_loci):0:-1]
reverse_space_loci.append(space_loci[0])

fin=sl
for x in reverse_space_loci:
    start=x+1
    for n in range(start,fin):
        print_b=print_b+characters[n]
    fin=x
    print_b=print_b+' '
for n in range(0,fin+1):
    print_b=print_b+characters[n]

print(print_b)

start=0
for x in space_loci:
    n=0
    while start+n<x:
        print_c=print_c+characters[x-n-1]
        n+=1
    start=x+1
    print_c=print_c+' '
n=0
while space_loci[-1]+n<sl:
    print_c=print_c+characters[sl-n-1]
    n+=1

print(print_c)