alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabets:
      position = alphabets.index(char)
      new_position = position + shift_amount
      end_text += alphabets[new_position]
    else:
      end_text += char #spaces, special chars, no., etc. remain the same
  print(f"This is the {cipher_direction}d result: {end_text}")

end = False
while not end:

  direction = input("Welcome :)\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26 #for large number of shift value

  cipher(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to continue. Type 'no'to exit.\n")
  if restart == "no":
    end = True
    print("Peace out")
    