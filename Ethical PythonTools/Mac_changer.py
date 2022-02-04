
import re
import subprocess
from random import choice,randint


#new_mac=input("Enter your new mac :").strip()  

print("enter 1 for the maual_change and 2 for automatic : ")
inp =input()
interface=input("Enter the network interface :").strip()

def main():
    if inp == "1":
        #interface=input("Enter the network      interface :").strip()
        new_mac=input("Enter your new mac :").strip()
        Change_Mac(interface,new_mac)
    elif inp == "2":
        random =mac_rand()
        print(random)
        Change_Mac(interface,random)       

def mac_rand():
    cisco =["00","40","96"]
    dell =["00","14","22"]
    mac_address=choice([cisco,dell])
    for i in range(3):
        one = choice(str(randint(0,9)))
        two =choice(str(randint(0,9)))
        three=(str(one+two))
    return ":".join(mac_address)    

def Change_Mac(interface,new_mac):
    subprocess.call(["ifconfig "+str(interface)+" down"],shell= True) #ifconfig eth0 down is the command the code refers
    subprocess.call(["ifconfig "+str(interface)+" hw ether "+str(new_mac)+" "],shell= True) #ifconfig eth0 hw ether  44:s4:53:30:33 this 
    subprocess.call(["ifconfig "+str(interface)+ " up "],shell= True)
    
def CurrentMac():

    out = subprocess.check_output(["ifconfig"+" eth0"],shell= True)
    current_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(out))
    print(f"old macaddress {current_mac}")
    

if __name__=='__main__':
    main()
    
