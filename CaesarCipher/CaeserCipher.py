import art

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]


def caesar(originalWord, shiftCount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decrypt":
        shiftCount *= -1
    for letter in originalWord:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shiftCount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode} result: " + cipher_text)

print(art.logo)

should_continue='yes'
while should_continue:
    original_Word=input("Enter the text you want to encrypt/decrypt: ").lower()
    shift_count=int(input("Enter the shift amount: "))
    direction=input("Enter the direction you want to encrypt or decrypt: ")

    caesar(original_Word, shift_count, direction)
    restart=input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if restart=="no":
        print("Thank you for playing!")
        break
    else:
        continue


