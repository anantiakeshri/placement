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
    
encrypt(text, shift)