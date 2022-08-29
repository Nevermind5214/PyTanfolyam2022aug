# there is no break in the loop

for i in range(10):
    print(i, end=' ')
else:    # nobreak
    print()
    print("there was no break")

# There is a break in the loop!

for i in range(10):
    print(i, end=' ')
    if i == 5:
        break
else:    # nobreak
    print()
    print("there was no break")