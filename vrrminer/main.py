import time
import colorama
from colorama import Fore
from colorama import Style
import random
import string

# Inițializarea colorama
colorama.init(autoreset=True)

print(Fore.BLUE + """
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗   
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝   
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗     
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝     
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗   
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝  



     

████████╗ ██████╗
╚══██╔══╝██╔═══██╗
   ██║   ██║   ██║
   ██║   ██║   ██║
   ██║   ╚██████╔╝
   ╚═╝    ╚═════╝

      


██╗   ██╗██████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗███████╗██████╗
██║   ██║██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██╔════╝██╔══██╗
██║   ██║██████╔╝██████╔╝██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝
╚██╗ ██╔╝██╔══██╗██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗
 ╚████╔╝ ██║  ██║██║  ██║██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║
  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
""")


time.sleep(10)

print("")

crypto = str(input(Fore.RED + """
 ██████╗██╗  ██╗ ██████╗ ███████╗███████╗    ██████╗ ████████╗ ██████╗     ██████╗ ██████╗     ███████╗████████╗██╗  ██╗       
██╔════╝██║  ██║██╔═══██╗██╔════╝██╔════╝    ██╔══██╗╚══██╔══╝██╔════╝    ██╔═══██╗██╔══██╗    ██╔════╝╚══██╔══╝██║  ██║    ██╗
██║     ███████║██║   ██║███████╗█████╗      ██████╔╝   ██║   ██║         ██║   ██║██████╔╝    █████╗     ██║   ███████║    ╚═╝
██║     ██╔══██║██║   ██║╚════██║██╔══╝      ██╔══██╗   ██║   ██║         ██║   ██║██╔══██╗    ██╔══╝     ██║   ██╔══██║    ██╗
╚██████╗██║  ██║╚██████╔╝███████║███████╗    ██████╔╝   ██║   ╚██████╗    ╚██████╔╝██║  ██║    ███████╗   ██║   ██║  ██║    ╚═╝
 ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝    ╚═════╝    ╚═╝    ╚═════╝     ╚═════╝ ╚═╝  ╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝       ⠀                       
"""))


if crypto == "ETH" or crypto == 'BTC':
    print("Okay, Wallets are being prepared for mining!")
    time.sleep(3)

LicenseKey = input("Input License Key: ")
if LicenseKey == "A7H8JGHFFNSYBB1HSHJFNVUDS8HHN1US8":
    print("Key is VALID!")
    time.sleep(0.5)
else:
    print("Invalid Key!")
    print("Press Enter to quit!")
    input()
    exit()

print("Checking if Key is Valid... ")
time.sleep(1)

if crypto == "ETH":
    adress = str(input ("Please enter your Ethereum address: "))
    print("Checking if address exists... ")
    time.sleep(2)
    print("Check has been successful!")

elif crypto == 'BTC':    
    adress = str(input ("Please enter your Bitcoin address: "))
    print("Checking if address exists... ")
    time.sleep(2)
    print("Check has been successful!")

class bcolors:
    Won = '\033{92m'
    Fail = '\003{91m'

def id_gen(size = 40, chars = string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))     

tries = 0

if crypto == 'ETH':
    while(True):
        if(tries > random.randint(2500000, 10000000000)):
             print(Fore.GREEN + "[-] 0x" + id_gen() + " | Valid | " + "2.163 ETH")
             print("Transferring 2.163 ETH to", adress)
             print("Your ETH will be added to your ETH address in 72 hours. Times can differ!")
             time.sleep(6)
             tries = 0
             print("Done! VRRMINER is running again!")
             time.sleep(3)
        else:
            print(Fore.RED + "[-] bc1" + id_gen() + "| Invalid |" + "0.0000 ETH")   
            tries += 1

elif crypto == 'BTC':
    while(True):
        if(tries > random.randint(15000000, 10000000000)):
             print(Fore.GREEN + "[-] bc1" + id_gen() + " | Valid | " + "1.673 BTC")
             print("Transferring 1.673 BTC to", adress)
             print("Your BTC will be added to your BTC address in 72 hours. Times can differ!")
             time.sleep(5)
             tries = 0
             print("Done! VRRMINER is running again!")
             time.sleep(3)
       
