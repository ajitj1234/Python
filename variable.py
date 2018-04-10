
def hello_name(name="shraddha",Age=27):
    print("hello",name,"My age is :",Age)

hello_name("Ajit",25)
hello_name()

def sort_out(*x):
    for val in x:
        greeting = sorted([*x])
        print(greeting)

sort_out("R","B","z","a","8","1","s")

def first_function():
    print("My first function is " + "1")
    print("Good")

first_function()

def second_function(str1, str2):
    print(str1 + str2)
    print(str2 + str1)
    print(len(str1))
    ##print(sorted([]))
second_function(" My first argument ", " my second argument")
second_function(" Ajit "," radha")
second_function(" R ","B")

##default functions

def data(name="ajit",age=28 ):
    print("my name is ",name, "and age is ",age)

data("radha",26)   ##this value has more priority than default value
data(age = 35,name="ajit")