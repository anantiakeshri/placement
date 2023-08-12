#Testing game module

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_num):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_pos = position + shift_num
        new_letter = alphabet[new_pos]
        cipher_text += new_letter
    print(f"The cipher text is {cipher_text}")

def decrypt(cipher_text, shift_number):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_number
        plain_text += alphabet[new_position]
    print (f"The decrypted text is {plain_text}")
          
if direction == 'encode':
    encrypt(plain_text=text, shift_num=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_number=shift)
    
