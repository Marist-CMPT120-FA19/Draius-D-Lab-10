##Draius Disimone Lab 10

import string

def main():

    filename = input("Enter the filename(s): ")
    file = open("Censor.txt", 'r').readlines()
    val = open("Sentence.txt", 'w')
    w = 'dumb'
    
    for w in file:
        s = w.split( )
        for word in s:
            counter = 0
            for letter in word:
                if not letter in string.punctuation:
                    counter += 1
            if counter == 5:
                if "." in word:
                    word = "****."
                elif "," in word:
                    word = "****,"
                elif "?" in word:
                    word = "****?"
                else:
                    word = "****"
            print(word + " ", file = val, end = "")
    val.close()
main()

