import time
import colorama
from colorama import Fore
from colorama import Style
import random
import string
 
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
print("")
 
crypto = str(input('Choose Between ETH and BTC: '))
 
if crypto == "ETH" or crypto == 'BTC':
    print("Okay, Wallets are being prepard for mining!")
    time.sleep(3)
 
LicenseKey = input("Input License Key: ")    
if LicenseKey == "admin":
    print("Key is VAILD!")
    time.sleep(0.5)
else:
    print("Invaild Key!") 
    print("Press Enter to quit!")   
    input()
    exit()
 
print("Checking if Key is Vaild... ")
time.sleep(1)
 
if crypto == "ETH":
    adress = str(input ("Please enter your Etheruem adress: "))
    print("Checking if adress exists... ")
    time.sleep(2)
    print("Check has been successfully!")
 
 
elif crypto == 'BTC':    
    adress = str(input ("Please enter your Bitcoin adress: "))
    print("Checking if adress exists... ")
    time.sleep(2)
    print("Check has been successfully!")
 
    class bcolors:
        Won = '\033{92m'
        Fail = '\003{91m'
 
def id_gen(size = 40, chars = string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))     
 
tries = 0
 
 
if crypto == 'ETH':
    colorama.init()
    while(True):
        if(tries > random.randint(2500000, 10000000000)):
             print(Fore.GREEN + "[-] 0x" + id_gen() + " | Valid | " + "2.163 ETH")
             print("Transfering 2.163 ETH", adress)
             print("Your ETH will be added to your ETH adress of 72 Hours Times can differ! ")
             time.sleep(6)
             tries - 0
             print("Done! Pixel Miner is running again!")
             time.sleep(3)
        else:
            print(Fore.RED + "[-] bc1" + id_gen() + "| Invaild |" + "0.0000 ETH")   
            tries += 1
 
elif crypto == 'BTC':
    colorama.init()
    while(True):
        if(tries > random.randint(150, 10000000000)):
             print(Fore.GREEN + "[-] bc1" + id_gen() + " | Valid | " + "1.673 BTC")
             print("Transfering 1.673 BTC to", adress)
             print("Your BTC will be added to your ETH adress of 72 Hours Times can differ! ")
             time.sleep(6)
             tries - 0
             print("Done! Pixel Miner is running again!")
             time.sleep(3)
        else:
            print(Fore.RED + "[-] bc1" + id_gen() + "| Invaild |" + "0.0000 BTC")   
            tries += 1
else:
    print("Invaild currency. Please choose between 'ETH and 'BTC'") 
 