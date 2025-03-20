alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar(text,shift,direction):
    text = text.lower()
    ciphered = ""
    for letter in text:
        if direction == "encode":
            shifted = alphabet.index(letter) + shift
        elif direction == "decode":
            shifted = alphabet.index(letter) - shift
        else:
            print("Not valid")
            break
        shifted = shifted % len(alphabet)
        ciphered += alphabet[shifted]
    print(ciphered)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or type 'done' to be done\n")
    if direction=="done":
        break
    text = input("Type your message\n")
    shift = int(input("Type the shift number\n"))

    caesar(text,shift,direction)