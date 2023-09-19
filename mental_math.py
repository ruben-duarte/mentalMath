import random
# numbers in ascci
zero = """
  ___  
 / _ \ 
| | | |
| |_| |
 \___/
"""
one = """
 _ 
/ |
| |
| |
|_|
"""
two = """
 ____  
|___ \ 
  __) |
 / __/ 
|_____|
"""

three = """
 _____ 
|___ / 
  |_ \ 
 ___) |
|____/ 
"""

four ="""
 _  _   
| || |  
| || |_ 
|__   _|
   |_|  
"""

five = """
 ____  
| ___| 
|___ \ 
 ___) |
|____/ 
"""

six = """
  __   
 / /_  
| '_ \ 
| (_) |
 \___/ 
"""

seven = """
 _____ 
|___  |
   / / 
  / /  
 /_/   
"""

eight = """
  ___  
 ( _ ) 
 / _ \ 
| (_) |
 \___/ 
"""

nine ="""
  ___  
 / _ \ 
| (_) |
 \__, |
   /_/
"""

ten ="""
 _  ___  
/ |/ _ \ 
| | | | |
| | |_| |
|_|\___/ 
"""
eleven = """
 _ _ 
/ / |
| | |
| | |
|_|_|
"""
twelve ="""
 _ ____  
/ |___ \ 
| | __) |
| |/ __/ 
|_|_____|
"""

thirteen ="""
 _ _____ 
/ |___ / 
| | |_ \ 
| |___) |
|_|____/
"""
fourteen = """
 _ _  _   
/ | || |  
| | || |_ 
| |__   _|
|_|  |_| 
"""

fifteen = """
 _ ____  
/ | ___| 
| |___ \ 
| |___) |
|_|____/ 
"""

sixteen ="""
 _  __   
/ |/ /_  
| | '_ \ 
| | (_) |
|_|\___/ 
"""

seventeen ="""
 _ _____ 
/ |___  |
| |  / / 
| | / /  
|_|/_/   
"""
eighteen ="""
 _  ___  
/ |( _ ) 
| |/ _ \ 
| | (_) |
|_|\___/ 
"""



equals = """
 _____ 
|_____|
|_____|
"""


plus = """
   _   
 _| |_ 
|_   _|
  |_|  

"""

message_start ="""

    _               _                                    _ 
   / \   __ _ _   _(_) __   ____ _ _ __ ___   ___  ___  | |
  / _ \ / _` | | | | | \ \ / / _` | '_ ` _ \ / _ \/ __| | |
 / ___ \ (_| | |_| | |  \ V / (_| | | | | | | (_) \__ \ |_|
/_/   \_\__, |\__,_|_|   \_/ \__,_|_| |_| |_|\___/|___/ (_)
           |_|                                             
"""
message_success = """
 _____              _            _        
| ____|_  _____ ___| | ___ _ __ | |_ ___  
|  _| \ \/ / __/ _ \ |/ _ \ '_ \| __/ _ \ 
| |___ >  < (_|  __/ |  __/ | | | ||  __/ 
|_____/_/\_\___\___|_|\___|_| |_|\__\___|                                              
"""
message_try = "Intentalo de nuevo, la practica hace al maestro"
# print(one)
# print(plus)
# print(one)
# print(equals)
# print(two)


numbers = { 1:one, 2:two, 3:three, 4:four, 5:five, 6:six, 7:seven, 8:eight, 9:nine, 0:zero, 10:ten, 11:eleven, 12:twelve, 13:thirteen, 14:fourteen, 15:fifteen, 16:sixteen, 17:seventeen, 18:eighteen}
operators = { '+':plus }



print(message_start)
operations_number = int(input("¿cuantas sumas quieres practicar? "))

counter = 0
while counter < operations_number:

  first_number= random.randint(7,9)
  second_number=random.randint(7,9)
  sum = first_number+second_number

  if first_number in numbers:
      print(numbers[first_number])

  print(plus)

  if second_number in numbers:
      print(numbers[second_number])

  result = input("Ingresa resultado: ")
  result = int(result)

  if result == sum:
     print(message_success)
     print("resultado correcto: ",sum)
  else:
     print(message_try)
  
  counter += 1




