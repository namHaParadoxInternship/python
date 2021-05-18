# Simple example about try-except
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except KeyboardInterrupt:
        print(
            "You can't leave without input any NUMBER !!! (And please don't kill me :(()")
