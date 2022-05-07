from email import charset
from operator import length_hint


def palindrome(str):
    for i in range(len(str)):
        if(str[i] != str[-i-1]):
            print("la chaine est non palindrome")
            return 0
    print("la chaine est palindrome")
    return 1

palindrome("hollo")