#ask user how many criminals
x = input("how many criminals are there?")
x = int(x)

    #check for less than 5
if int(x) < 5:
    print("I got this!")
    #check for between 5 and 10
elif 5 <= int(x) <=10:
    print("Help me Batman")
    #check for more than 5
elif int(x) > 10:
    print("good luck out there!")

