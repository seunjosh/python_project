import string
import random

vowels = 'aeiouy'#creating a variable for vowel
consonants='bcdefghijklmnopqrstvuwxyz'#create a variable for consonants
letters = string.ascii_lowercase#create a variable for any letter entered

#prompting the user for input
letter1_in1 =input("Enter 'v' for vowels 'c' for consonants and 'l' for any letter:")
letter2_in2 =input("Enter 'v' for vowels 'c' for consonants and 'l' for any letter:")
letter3_in3 =input("Enter 'v' for vowels 'c' for consonants and 'l' for any letter:")
letter4_in4 =input("Enter 'v' for vowels 'c' for consonants and 'l' for any letter:")





#function for letter generation

def generator():
    if letter1_in1 == 'v':
         letter1 = random.choice(vowels)
    elif letter1_in1 == 'c':
         letter1 = random.choice(consonants)
    elif letter1_in1 == 'l':
         letter1 = random.choice(letters)
    else:
         letter1 = letter1_in1


    if letter2_in2 =='v':
       letter2 = random.choice(vowels)
    elif letter2_in2 == 'c':
         letter2=random.choice(consonants)
    elif letter2_in2=='l':
         letter2=random.choice(letters)
    else:
        letter2=letter2_in2

    if   letter3_in3 =='v':
         letter3= random.choice(vowels)
    elif letter3_in3 == 'c':
         letter3=random.choice(consonants)
    elif letter3_in3=='l':
         letter3=random.choice(letters)
    else:
         letter3=letter3_in3

    if letter4_in4 == 'v':
       letter4 = random.choice(vowels)
    elif letter4_in4 == 'c':
          letter4 = random.choice(consonants)
    elif letter4_in4 == 'l':
          letter4 = random.choice(letters)
    else:
          letter4 = letter3_in3

    names = letter1 + letter2 + letter3+letter4
    return (names)




for n in range(30):
    print(generator())