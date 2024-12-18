import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift,direction):
    if(direction=='encode'):
        encrypted_word = ""
        for letter in text:
            if letter not in alphabet:
                encrypted_word+=letter
            else:
                shifted_index=alphabet.index(letter)+shift
                if shifted_index > 25 :
                     shifted_index=shifted_index%alphabet.index(letter)
                encrypted_word+=alphabet[shifted_index]
        print(f"Here is the encoded result: {encrypted_word}")
    else:
        decrypted_word = ""
        for letter in text:
            if letter not in alphabet:
                decrypted_word+=letter
            else:
                shifted_index = alphabet.index(letter) - shift
                if shifted_index < 0:
                    shifted_index = shifted_index % alphabet.index(letter)
                decrypted_word += alphabet[shifted_index]
        print(f"Here is the decoded result: {decrypted_word}")

caesar(text, shift, direction)
should_continue=True
while should_continue:
    retry=input("Type 'yes' if you want to go again. Otherwise,type 'no'")
    if retry=='yes':
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u',
                    'v', 'w', 'x', 'y', 'z']
        direction = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
    else:
        should_continue=False
        print("Goodbye")



