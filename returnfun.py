
def add_variables(x,x1):
    return x+x1

sum = add_variables(5,7)
sum1 = add_variables("hello ","ajit")
print("Addition is ", sum,sum1)
x1 = "hello raj".split(" ")[1]
x3 = sum1.split(" ")[1]
print(x1)
print(x3)
print(str(sum) + " jagtap")
print(sum1 + " jagtap")

def second_function(str1, str2):
    return str1 + str2

string = second_function(" My first argument ", " my second argument")
string1 = second_function(" Ajit "," radha")
string2 = second_function(" R ","B")
print(string)
print(string1)
print(string2)

print(string2 + string1)
print(len(string))
print(len(string1))
print(len(string2))

print(sorted(["R", "B", "z", "a", "8", "1", "s"]))

string2 = string1
string3 = string1

if string2 == string:
    print("good")
elif string2 == string:
    print("moody")
elif string2 == string3:
    print("best")

else:
    print("bad")

sort = ["R","B","z","a","8","1","s"]

for items in sort:
    print(sorted(sort))

ajit = True
radha = 0

while ajit:
    if radha == 100:
        ajit = False

    else:
        print(radha)
        radha +=1


