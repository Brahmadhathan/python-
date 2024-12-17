#encode and decode your message in caecercipher
import caeserlogo
print(caeserlogo.logo)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def caeser(original_text,shift_amount,encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
                shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter

        else:
            shifted_postion=  alphabet.index(letter) + shift_amount 
            shifted_postion %= len(alphabet) 
            output_text += alphabet[shifted_postion]
    print(f"here is the {encode_or_decode}d result {output_text}")

#restart the program again
should_continue = True

while should_continue:
    
    direction = input("type encode to encrypt and decode to decrypt:\n").lower()
    text = input("type your text ")
    shift=int(input("enter the shift number \n"))

    caeser(original_text=text,shift_amount=shift,encode_or_decode=direction)


    restart = input("type YES if you want to continue , or NO\n").lower()
    if restart == "no":
        should_continue = False
        print("the messagae is delivered ")



