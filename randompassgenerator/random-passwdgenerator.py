#!/usr/bin/python3
import os
import random 
import termcolor
import string 

valid_letters = string.ascii_letters
valid_digits = string.digits
valid_punct = string.punctuation

class PasswordTooShortError(Exception):
    pass 

class NotValidAnswer(Exception):
    pass 

class ColoredText():
    def __init__(self, text: str, color: str) -> None:
        self.text = text
        self.color = color

    def __str__(self) -> str:
        return termcolor.colored(self.text,self.color)#

   
def passwd_length():
    while character_count_str := input("How many characters should your password be?  "):
        try:
            character_count = int(character_count_str)
            if character_count < 8:
                raise PasswordTooShortError
        except PasswordTooShortError:    
            print(f"{ColoredText("minimum length of password is 8 characters","light_red")}\n")
        except ValueError:
            print(f"{ColoredText("must enter valid integer greater than or equal to 8", "light_red")}\n")
        else:
            print(f"you have chosen a password length of {character_count}\n")
            break
    return character_count

def passwd_contains_digits():
    while digit_count_str := input("How many digits should password contain?  \n"):
        try:
            digit_count = int(digit_count_str)
            if digit_count > passwd_length:
                raise NotValidAnswer
        except NotValidAnswer:
            print(f"{ColoredText("Amount of digits exceeds total specified password length","light_red")}\n")
        except ValueError:
            print(f"{ColoredText("must enter a valid integer","light_red")}\n")
        else:
            print(f"Your password will contain {digit_count} digits\n")
            break 
    return digit_count

def passwd_contains_punct():
    while punct_count_str := input("How many punctuation characters should password contain?  \n"):
        try:  
            punct_count = int(punct_count_str)
            if punct_count > (passwd_length - digit_count):
                raise NotValidAnswer
        except NotValidAnswer:
            print(f"{ColoredText("Amount of punctuation characters exceeds available remaining characters for given password length","light_red")}\n")
        except ValueError:
            print(f"{ColoredText("must enter a valid integer less than or equal to password length","light_red")}\n")
        else:
            print(f"Your password will contain {punct_count} punctuation characters\n") 
            break
    return punct_count

def random_digits():
    for i in range(0, digit_count):
        passwd_list.append(random.choice(valid_digits))
    return passwd_list

def random_punct():
    for i in range(0,punct_count):
        passwd_list.append(random.choice(valid_punct))
    return passwd_list

def random_letters():
    for i in range(0,(passwd_length - len(passwd_list))):
        passwd_list.append(random.choice(valid_letters))
    return passwd_list

def shuffle_password_list():
    return random.shuffle(passwd_list)

def gen_password_str():
    password = ''
    for char in passwd_list:
        password += "".join(char)
    return password 

def main():
    random_digits()
    random_punct()
    random_letters()
    shuffle_password_list()
    password = gen_password_str()
    print(f"random generated password: {ColoredText(f"{password}","light_green")}")

if __name__ == "__main__":
    passwd_list = []
    passwd_length = passwd_length() 
    digit_count = passwd_contains_digits()
    punct_count = passwd_contains_punct()
    main()
