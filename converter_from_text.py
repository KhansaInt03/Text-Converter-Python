import time

def to_ascii(text):
    to_ascii = [ ord(i) for i in text ]

    return to_ascii

def to_binary(text):
    to_binary = [ bin(ord(i)) for i in text ]
    c = 'b'
    result = [ ele.replace(c,'') for ele in to_binary ]

    return result

def to_octal(text):
    to_octal = [ oct(ord(i)) for i in text ]
    c = 'o'
    result = [ ele.replace(c,'') for ele in to_octal ]

    return result

def to_hexa(text):
    to_hexa = [ hex(ord(i)) for i in text ]
    c = 'x'
    result = [ ele.replace(c,'') for ele in to_hexa ]

    return result

print("Welcome to Converter!!!\nWhat would you like to do?")
time.sleep(0.5)

while True:
    to_do = input("[1] Convert from text to ASCII\n[2] Convert from text to Binary\n[3] Convert from text to Octal\n[4] Convert from text to Hexa\nYour choice >> ")
    if to_do == "1":
        time.sleep(0.5)
        text = input("Input your text/data\n>>> ")
        time.sleep(0.5)
        print(*to_ascii(text))
    
    elif to_do == "2":
        time.sleep(0.5)
        text = input("Input your text/data\n>>> ")
        time.sleep(0.5)
        print(*to_binary(text))
    
    elif to_do == "3":
        time.sleep(0.5)
        text = input("Input your text/data\n>>> ")
        time.sleep(0.5)
        print(*to_octal(text))
    
    elif to_do == "4":
        time.sleep(0.5)
        text = input("Input your text/data\n>>> ")
        time.sleep(0.5)
        print(*to_hexa(text))
    
    else:
        time.sleep(0.5)
        print("Invalid Value. Try Again")
    
    time.sleep(0.5)
    cont = input("Would you like to continue? [y/n]\n>> ").lower()
    if cont == "y":
        time.sleep(0.5)
        continue
    else:
        break