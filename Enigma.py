"""
The Encryption code is structured like this:

[Wheel one(from 0-10 )][wheel2][wheel3][settings(from 0-26)][setting2][setting3]

There are 12 digits that you'd have to input in one long integer. Ex: 010203000000
"""
def enigma():
  out = ""
  alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
  Input = input("Encryption code: \n")
  PINS = input("Enter 10 letters. They must all be different.").lower()
  message = input("\nMessage(lowercased letters and spaces only): \n")

  #First Starting position
  Fdef = int(Input[:2])
  Sdef = int(Input[2:4])
  Tdef = int(Input[4:6])
  FS_pos = int(Input[6:8])
  SS_pos = int(Input[8:10])
  TS_pos = int(Input[10:])
  pin1 = PINS[:2]
  pin2 = PINS[2:4]
  pin3 = PINS[4:6]
  pin4 = PINS[6:8]
  pin5 = PINS[8:10]
  plugs = {pin1[0]: pin1[1], pin2[0]: pin2[1], pin3[0]: pin3[1], pin4[0]: pin4[1], pin5[0]: pin5[1], pin1[1]: pin1[0], pin2[1]: pin2[0], pin3[1]: pin3[0], pin4[1]: pin4[0], pin5[1]: pin5[0]}
  new_msg = ""
  for i in message:
  	if i in plugs:
  		i = plugs[i]
  		new_msg += i
  	else:
  		new_msg += i
  message = new_msg

  F_Defalt = ["f", "h", "a", "l", "w", "i", "b", "s", "e", "c", "x", "j", "k", "z", "o", "t", "r", "p", "n", "d", "y", "g", "v", "u", "q", "m", " "]
  S_Defalt = ["d", " ", "g", "u", "a", "m", "e", "z", "s", "r", "b", "c", "i", "h", "v", "y", "p", "k", "w", "q", "n", "t", "f", "x", "l", "o", "j"]
  T_Defalt = ["p", "t", "v", 'z', "n", "b", "y", "j", "f", "m", "l", "k", "h", "q", " ", "i", "w", "x", "r", "a", "d", "o", "c", "e", "u", "s", "g"]
  F_Defalt = ['g', 'h', 'd', 'q', 'n', 'k', 'x', " ", 'y', 'm', 'e', 's', 'v', 'w', 'a', 'p', 'o', 'b', 'l', 'f', 'c', 'u', 'z', 'r', 'j', 'i', 't']
  Fi_Defalt = ['s', 'h', 'u', 'l', 'j', 'x', 'k', 'b', 'v', 'c', 'm', 'y', 'p', 'r', 'e', 'n', 'f', 'i', 'd', 'q', 't', 'a', 'z', 'o', 'w', 'g', " "]
  Si_Defalt = ['z', 'w', 's', " ", 'f', 'o', 'n', 'i', 'k', 'c', 'q', 'x', 'b', 'h', 'j', 'u', 'e', 'v', 'p', 't', 'r', 'd', 'a', 'm', 'g', 'l', 'y']
  Se_Defalt = ['k', 'h', 'y', 'e', 'v', 'w', 'b', 'x', 'i', 'm',' p', 'f', 'a', 'c', 'r', 'j', 'd', 'o', 'u', 'l', 'z', 'q', 'n', 's', 't', 'g', " "]
  E_Defalt = ['j', 'e', 'z', 'h', 'k', 'b', 'l', 't', 'u', 'n', 'q', 'g', 'a', " ", 'c', 'f', 'p', 'r', 'm', 'x', 'y', 'w', 'i', 'o', 'v', 's', 'd']
  N_Defalt = ['c', 'o', 'q', 'f', 'd', 'k', 'e', 'j', 's', 'w', 'p', 'x', 'l', 'a', 'm', 'y', 'g', 'u', 'h', 'v', 'i', 'n', " ", 'b', 'r', 't', 'z']
  Te_Defalt = ['p', 'x', 'q', 'd', 'a', 'f', 'g', 's', 'u', " ", 'k', 'b', 'o', 'v', 'y', 'r', 'n', 'j', 'w', 'i', 'l', 'z', 'e', 'h', 'c', 'm', 't']
  Default_lists = {1: F_Defalt, 2: S_Defalt, 3: T_Defalt, 4: F_Defalt, 5: Fi_Defalt, 6: Si_Defalt, 7: Se_Defalt, 8: E_Defalt, 9: N_Defalt, 10: Te_Defalt}

  #first wheel
  F_Spin = 0

  F_Wheel_Default = Default_lists[Fdef]
  F_Wheel = F_Wheel_Default[FS_pos:] + F_Wheel_Default[:FS_pos]

  #second wheel
  S_Spin = 0

  S_Wheel_Default = Default_lists[Sdef]
  S_Wheel = S_Wheel_Default[SS_pos:] + S_Wheel_Default[:SS_pos]

  #third wheel
  T_Spin = 0

  T_Wheel_Default =  Default_lists[Tdef]
  T_Wheel = T_Wheel_Default[TS_pos:] + T_Wheel_Default[:TS_pos]

  #Rotate_Stationary
  R_Stat = {"c": "h", "y": "g", "a": "t", "l": "d", "p": "u", "j": "v", "z": "k", "q": "i", "e": "f", "r": "m", "s": "n", "x": "b", "w": "o", "o": "w", "b": "x", "n": "s", "m": "r", "f": "e", "i": "q", "k": "z", "v": "j", "u": "p", "d": "l", "t": "a", "g": "y", "h": "c", " ": " "}

  for i in message.lower():
    
    #a = 1, b = 2, c = 3, d = rotate, e = 4, f = 5, g = 6. 

    #alf_index-1 is the index of the letterin the alphabet, then the index is used to find what's there on the first wheel. 
    alf_index = alphabet.index(i)+1
    a = F_Wheel[alf_index-1]

    alf_index = alphabet.index(a)+1
    b = S_Wheel[alf_index-1]

    alf_index = alphabet.index(b)+1
    c = T_Wheel[alf_index-1]

    #Rotated, now going backwards. 
    d = R_Stat[c]

    index = T_Wheel.index(d)+1
    e = alphabet[index-1]

    index = S_Wheel.index(e)+1
    f = alphabet[index-1]

    index = F_Wheel.index(f)+1
    g = alphabet[index-1]
    F_Wheel = F_Wheel[1:] + F_Wheel[:1]
    F_Spin += 1
    if F_Spin == 26:
      F_Spin = 0
      S_Wheel = S_Wheel[1:] + S_Wheel[:1]
      S_Spin += 1
    if S_Spin == 26:
      S_Spin = 0
      T_Wheel = T_Wheel[1:] + T_Wheel[:1]
      T_Spin += 1
    out = out + g

  new_msg = ''
  for a in out:
    if a in plugs:
      a = plugs[a]
      new_msg += a
    else:
      new_msg += a
  message = new_msg
  message = "\nmessage:\n" + message
  return message

try:
  print(enigma())

except:
  print("\n\nAN ERROR OCCURED \nMake sure: \n1. letters and spaces only. \n2. your Encryption code is correct. \n3. All the letter you entered in the pins sections were all different.")
