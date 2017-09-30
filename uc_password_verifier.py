"""
Password Verifier
Chris Mauldin
March 5th 2017

Summary:
Write a program that reads a single string and determines whether or
not is valid as a password based on the rules in UC's password site:


"""
#function to puts the characters of a string into a list
def splice(string):
    str_arr = []
    for c in string:
        str_arr.append(c)

    return str_arr

#function that returns true of an object is present in a list, false otherwise
def isPresent(obj, list):

    for c in list:
        if obj == c:
            return True

#function that modifies elements within a list and appends modified elements to a new list
def append_ascii(list, list2):

    for c in list:
        list2.append(ord(c))

    return list2



def uc_password_verifier(pwrd):
    #Checking the length of the string to make sure it is atleast 8 characters long
    if len(pwrd) < 8:
        print("Password entered is less than eight characters. Enter another password")
        main()

    #Create variables to keep count of the password parameters, with the intent of checking later
    #to make sure they're greater than or equal to one
    numberCount = 0
    lowercaseLetterCount = 0
    uppercaseLetterCount = 0
    symbolCount = 0

    #created a range of ascii numbers to check against; Along with two list
    ascii_lower = range(97, 123)
    ascii_upper = range(65, 91)
    ascii_number = range(48, 58)
    ascii_symbols = [41, 64, 35, 36, 37, 38, 95, 61]

    #split the string into individual characters, so I can iterate through and each one
    pwrd_list = splice(pwrd)
    ascii_pwrd = []
    list_made = lambda l1, l2: append_ascii(l1, l2)
    list_made(pwrd_list, ascii_pwrd)

    #created a lambda expression using the isPresent() function above to verify if certain characters were present
    check = lambda o, l: isPresent(o, l)

    #Loop iterating through the password, and adding to the count of each parameter
    for num in ascii_pwrd:
        if check(num, ascii_lower):
            lowercaseLetterCount+=1

        if check(num, ascii_upper):
            uppercaseLetterCount+=1

        if check(num, ascii_number):
            numberCount+=1

        if check(num, ascii_symbols):
            symbolCount+=1

    #elements in this list are going to be printed based on what criteria isn't met by user inputter password
    requirements = ["Passwords must contain at least one lowercase letter (a, b, c, etc.)",
                    "Passwords must contain at least one uppercase letter (A, B, C, etc.)",
                    "Passwords must contain at least one number (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)",
                    "Passwords must contain at least one of the following: ! @ # $ % & _ ="]

    counts = [lowercaseLetterCount, uppercaseLetterCount, numberCount, symbolCount]

    count_array = []
    i = 0
    for n in counts:

        if n == 0:
            count_array.append(i)

        i+=1

    if len(count_array) == 0:
        print("Password has met criteria, It will be saved")

    for n in count_array:

        print("{}".format(requirements[n]))




def main():
    password = input("Enter password to be verified: ")

    uc_password_verifier(password)

if __name__ == "__main__":

    main()

