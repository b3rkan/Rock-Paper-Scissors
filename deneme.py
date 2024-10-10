import sys
import random
from enum import Enum

class TKM(Enum):
    TAŞ = 1 
    KAĞIT = 2
    MAKAS = 3

print(" ")
playerchoice = input("Enter...\n1 Taş,\n2 Kağıt\n3 Makas : \n\n")

player = int(playerchoice)

if player < 1 | player > 3:
   sys.exit("1,2 veya 3 numaralı seçeneği girmelisiniz!")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("Siz " + str(TKM(player)).replace('TKM.', '') + "'ı seçtiniz" + ".")
print("Phyton " + str(TKM(computer)).replace('TKM.', '') + "'ı seçti " + ".")
print("")

if playerchoice > computerchoice:
    sys.exit("👑 Oyunu siz kazandınız. Bravo !")

    print(" ")

if playerchoice == computerchoice:
    sys.exit("♾️ Berabere. ")

    print(" ")


else:
    sys.exit("🐍 Oyunu Pyhton kazandı.")

    print(" ")
    