print("Robot Cheerleader")
sequence = "bcdfghjklmnpqrstvwxyzBCDFGHIJKLMNPQRSTVWXYZ"
word=input("Enter a word ")
enthusiam=int(input("Enter Enthusiam in a scale of 1-10"))
for i in word:
    if i in sequence:
        print("Give me a "+ i + "!" + i)
    else:
        print("Give ma an " + i + "!" + i)
for i in range(enthusiam):
    print(word+"!")