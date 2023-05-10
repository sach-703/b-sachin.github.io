from mymodule import add

print("Hello world")
print("Changes added")

print(add(2,3))

with open("greeting.txt", "r") as f:
    print(f.read())