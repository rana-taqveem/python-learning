import random

print("welcome to My Password generator. Please follow the below instructions to generate a strong password")
print("  ")

num_of_letters = int(input("Please enter how many letters you want in your password. (min:8, max:16) : "))
num_of_symbols = int(input("Please enter how many symbols you want in your password. (min:1, max:4) : "))
num_of_numbers= int(input("Please enter how many numbers you want in your password. (min:1, max:4) : "))

total_len = num_of_letters + num_of_symbols + num_of_numbers

small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
large_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['~','!','#','$','%','^','&','*','(',')','?']
numbers = ['0','1','2','3','4','5','6','7','8','9']



def pass_gen1():

    symbols_count = 0
    numbers_count = 0
    letters_count = 0
    letter_types = [1,2,3,4]
    password = ''
    while len(password) < total_len:
        nextletterType = random.choice(letter_types)
        if (nextletterType == 1 or nextletterType == 2) and letters_count < num_of_letters:
            if nextletterType == 1:
                password += str(random.choice(small_letters))  # letters
            else:
                password += str(random.choice(large_letters))  # letters
            letters_count = letters_count + 1
        elif nextletterType == 3 and symbols_count < num_of_symbols:
            symbols_count = symbols_count + 1
            password += str(random.choice(symbols))  # letters
        elif nextletterType == 4 and numbers_count < num_of_numbers:
            numbers_count = numbers_count + 1
            password += str(random.choice(numbers)) 
    print(f'Your password is: {password}')


def pass_gen2():
    
    passw = []
    for i in range(0, num_of_letters):
        nextletterType = random.choice([1,2])
        if nextletterType == 1:
            passw.append(str(random.choice(small_letters)))  # letters
        else:
            passw.append(str(random.choice(large_letters)))  # letters

    for i in range(0, num_of_symbols):
        passw.append(str(random.choice(symbols)))

    for i in range(0, num_of_numbers):
        passw.append(str(random.choice(numbers)))


    random.shuffle(passw)
    print(f'Your password is: {passw}')


pass_gen1()
pass_gen2()



