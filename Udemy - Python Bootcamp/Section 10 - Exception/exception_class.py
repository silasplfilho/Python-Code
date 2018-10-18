# Problema 1

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print("There was an error of typing")

# Problema 2
try:
    x = 5
    y = 0
    z = x/y
except:
    print("There is an error of division.")
finally:
    print("All done")

# Problema 3
def ask():
    num = int(input("Input an interger"))
    print(num**2)

while True:
    try:
        ask()
        break
    except:
        print("An error ocurred. Try again")
        print("")
        continue
#Problema 3 - Solucao

def ask():

    waiting = True
    while waiting:
        try:
            n = int(input("Enter a number."))
        except:
            print("Please try again! \n")
            continue
        else:
            waiting = False

    print("Your number squared is: ")
    print(n**2)

ask()
