try :
    1 / 0

except Exception:
    print("exception")

except TypeError:
    print("error")

except ZeroDivisionError:

    print("zero error")
finally:
    print("divide")

#-----------------------------------

while True:
     try:
         x = int(input("Please enter a number: "))
         break
     except ValueError:
         print("Oops!  That was no valid number.  Try again...")
