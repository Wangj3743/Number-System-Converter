from conversion import *

# you can also use the functions here 
# print(DECtoBASE(BASE, NUMBER))
# print(BASEtoDEC(BASE, "NUMBER"))

print("PLEASE NOTE THAT THIS PROGRAM ONLY SUPPORTS BASE-2 to BASE 10")

base = int(input("\nBASE # ? (BASE-1 to BASE-10)\n"))
type = int(input(f"\nChoose:\n  1) DEC to BASE-{base}\n  2) BASE-{base} to DEC\n"))

if type == 1: # DEC TO BASE
  num = int(input(f"\nDEC # ? (MAX {base**8-1})\n"))
  print(f"\n\n\n{DECtoBASE(base, num)}")

elif type == 2: # BASE TO DEC
  num = str(input(f"\nBASE-{base} # ? (MAX " + f"{(base-1)}"*7 + ")\n******** <- formatting\n"))
  print(f"\n\n\n{BASEtoDEC(base, num)}")

else:
  print("incorrect formatting, restart program")
