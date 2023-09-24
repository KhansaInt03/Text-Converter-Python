import time

def from_ascii(text):
    grouping = text.split()
    res = [ chr(int(ele)) for ele in grouping ]

    return res


def from_bin(text):
    grouping = text.split()
    res = [ chr(int(ele,2)) for ele in grouping ]

    return res


def from_oct(text):
    grouping = text.split()
    res = [ chr(int(ele,8)) for ele in grouping ]

    return res


def from_hexa(text):
    grouping = text.split()
    res = [ chr(int(ele,16)) for ele in grouping ]

    return res


print("Welcome to Converter!!!\nWhat would you like to do?")
time.sleep(0.5)

while True:
    to_do = input("[1] Convert from ASCII to text\n[2] Convert from Binary to text\n[3] Convert from Octal to text\n[4] Convert from Hexa to text\nYour choice >> ")
    if to_do == "1":
        time.sleep(0.5)
        text = input("Input your text/data\n>>> ")
        time.sleep(0.5)
        print(*from_ascii(text), sep='')
   
    elif to_do == "2":
        time.sleep(0.5)
        text = input("Input your text/data\n>>> ")
        time.sleep(0.5)
        print(*from_bin(text), sep='')
    
    elif to_do == "3":
        time.sleep(0.5)
        text = input("Input your text/data\n>>> ")
        time.sleep(0.5)
        print(*from_oct(text), sep='')
    
    elif to_do == "4":
        time.sleep(0.5)
        text = input("Input your text/data\n>>> ")
        time.sleep(0.5)
        print(*from_hexa(text), sep='')
    
    else:
        time.sleep(0.5)
        print("Invalid Value. Try Again")
    
    time.sleep(1)
    cont = input("Would you like to continue? [y/n]\n>> ").lower()
    if cont == "y":
        time.sleep(0.5)
        continue
    else:
        break