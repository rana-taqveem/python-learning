def simple_encrypt(message, default_letters, shift_by):

    encrypted_message = "" # h
    joined_letters = ''.join(default_letters)
    for letter in message:
        if letter not in joined_letters:
            encrypted_message += letter
        else:
            shifted_index = default_letters.index(letter) + shift_by
            shifted_index = shifted_index % len(default_letters)
            encrypted_message += default_letters[shifted_index]

    return encrypted_message


def simple_decrypt(message, default_letters, shift_by):
    decrypted_message = "" # b e
      #qnuux fxaum!, 9, e,d,c,b,a, 5-9 => -4
    joined_letters = ''.join(default_letters)
    for letter in message:
        if letter not in joined_letters:
            decrypted_message += letter
        else:
            shifted_index = default_letters.index(letter) - shift_by # 2-5 > -3 25-3 => 22
            # if shifted_index < 0:
            #     shifted_index = len(default_letters) + shifted_index

            shifted_index = shifted_index % len(default_letters) # it worked becasue in python a reminder is always positive


            decrypted_message += default_letters[shifted_index]

    return decrypted_message




def build_shifted_letters(default_letters, shift_by):
    lasti = 0
    shifted_letters = []
    for i in range(0, 26):
        if i + shift_by >= 26:
            shifted_letters.append(default_letters[i-lasti])

        else:
            shifted_letters.append(default_letters[i+shift_by])
            lasti = i + 1

    return shifted_letters

def process_message(message, source_letters, target_letters):
    joined_letters = ''.join(source_letters)
    processed_message = ""

  
    for char in enumerate(message):
        if char[1] == " ":
            processed_message += " "
        else:
            for i in range(0, 26):
                if char[1] == source_letters[i]:
                    processed_message += target_letters[i]
                    break
                elif char[1] not in joined_letters:
                    processed_message += str(char[1])
                    break

    return processed_message


# task = input("Please Type 'encode' to encrypt the message, or 'decode'  to decrypt the message: ")
# message = input(f'Please type your message to {task}: ').lower()
# shift_by = int(input("Please type the Shift number: "))

# task = 'encode'
message = 'hello world!'
shift_by = 9

default_letters = list('abcdefghijklmnopqrstuvwxyz')

em = simple_encrypt(message, default_letters, shift_by)
print(em)

print(simple_decrypt(em, default_letters, shift_by))

# shifted_letters = build_shifted_letters(default_letters, shift_by)

# print(shifted_letters)

# if task == 'encode':
#     encrypted_message = process_message(message, default_letters, shifted_letters)
#     print(encrypted_message)
# elif task == 'decode':
#     decrypted_message = process_message(message, shifted_letters, default_letters)
#     print(decrypted_message)
    

