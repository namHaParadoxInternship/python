# Simple example about try-except-else
while True:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    else:
        print("Thanks for your support!")
        break
