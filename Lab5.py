str = input("Enter a String: ")
vowels = 0
consonants = 0

for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels += 1
    else:
        if i != ' ' and i.isdigit() == False:
            consonants += 1

count = len(str) - str.count(' ')

print("The number of letters in String:", count)
print("The number of vowels in String:", vowels)
print("The number of consonants in String:", consonants)
