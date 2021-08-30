print("Hello")
name = input("What is your name?" )
print("Hello " + name)

number = input("What is your favorite number ")
triple = int(number) * 3
# Python will not implicitly add a string to an interger, so
# one needs to typecast it
print("Your number multiplied by three is " + str(triple))
