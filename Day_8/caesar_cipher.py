import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    # this line stores what happens in the loops
    output_text = ""
    #decoding is the opposite of encoding so the signs are opposites
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        #in case we get symbols,numbers, or spaces
        if letter not in alphabet:
            output_text += letter
        else:
            #what happens when we have only letters
            shifted_position = alphabet.index(letter) + shift_amount
            # what is 17 on a clock? it's 5, this works the same
            shifted_position %= len(alphabet)
            # reports to the empty line outside the loop
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

#while the user wants to continue this is true
should_continue = True

while should_continue:#(while true)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        # this helps escape the while loop
        #the condition is now false
        should_continue = False
        print("Goodbye")


