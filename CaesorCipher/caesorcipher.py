from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "encode" or cipher_direction == "decode" and -26 < shift_amount <= 26:

        for latter in start_text:
            if not latter.isalpha():
                end_text += latter
            else:
                position = alphabet.index(latter)
                if cipher_direction == "encode":
                    new_position = position + shift_amount
                    if new_position > 26:
                        new_position = new_position % 26
                else:
                    new_position = position - shift_amount
                    if new_position < 0:
                        new_position = new_position + 26

                end_text += alphabet[new_position]

        return end_text

    else:
        return "Invalid shift amount or cipher direction : shift amount must in range -26 to 25 and cipher direction " \
               "should encode or decode "


print(logo)
direction = input("What do you want to do encode or decode enter end to end the program :")

while direction.lower() != "end":
    amount = int(input("Enter shift amount to encode or decode message :"))
    text = input("Enter message to encode or decode :")

    message = caesar(start_text=text, shift_amount=amount, cipher_direction=direction)
    print(message)

    direction = input("What do you want to do encode or decode enter end to end the program :")
