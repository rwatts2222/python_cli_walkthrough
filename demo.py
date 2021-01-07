for i in range(10):
    if i == 20:
        print("found 20")
else: # Else is outside the for loop, which is different from other languages
    print("didn't find 20")

# versus:

for i in range(10):
    if i == 20:
        print("found 20")
    else: # Else inside for loop produces different result
        print("didn't find 20")