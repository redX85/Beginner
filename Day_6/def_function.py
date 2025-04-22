#print is an example of a function
#But we want to be able to make our own functions
def my_function():
    #do this
    print("Hello")
    #then do this
    print("Bye")
#for this defined function to be executed we need to call it:
my_function()
#we define functions because we don't want to repeatedly type
#the code. instead we want to make something that's reusable

def greet_user():
    name = input("What is your name?")
    print("Hello " + name)
greet_user()