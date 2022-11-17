from data import char_to_morse

def text_to_morse():
  text = input("Write your message: ").upper()
  morse_code = []
  for char in text:
    if char in char_to_morse:
      morse_code.append(char_to_morse[char])
  string = "".join(morse_code)    
  print(f"Your output is {string}")    
    
text_to_morse()   
