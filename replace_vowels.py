test = input("ENTER THE STRING : ")
test = test[::-1]
new_str = test.replace("A", "1").replace("E", '2').replace("I", "3").replace("O", '4').replace("U", '5')\
    .replace("a", "1").replace("e", '2').replace("i", "3").replace("o", '4').replace("u", '5')
print(new_str)
