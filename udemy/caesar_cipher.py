def process_message(message, default_letters, shift_by, process):

    encrypted_message = "" # h
    joined_letters = ''.join(default_letters)
    
    if process == 'decode':
        shift_by *= -1

    for letter in message:
        if letter not in joined_letters:
            encrypted_message += letter
        else:
            shifted_index = default_letters.index(letter) + shift_by
            shifted_index = shifted_index % len(default_letters)  # during decode woth neagive index it worked becasue in python a reminder is always positive

            encrypted_message += default_letters[shifted_index]

    return encrypted_message



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

def process_message2(message, source_letters, target_letters):
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


process = input("Please Type 'encode' to encrypt the message, or 'decode'  to decrypt the message: ")
message = input(f'Please type your message to {process}: ').lower()
shift_by = int(input("Please type the Shift number: "))

# task = 'encode'
# message = 'hello world!'
# shift_by = 9

default_letters = list('abcdefghijklmnopqrstuvwxyz')

if process == 'encode':
    encrypted_message = process_message(message, default_letters, shift_by, process)
    print(encrypted_message)
elif process == 'decode':
    decrypted_message = process_message(message, default_letters, shift_by, process)
    print(decrypted_message)
    

