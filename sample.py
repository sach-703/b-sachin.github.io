from mymodule import add

print("Hello world")
print("Changes added")
print("This line is added to show how push command works")

print(add(2,3))

with open("greeting.txt", "r") as f:
    print(f.read())

msg_file = open("greeting.txt","r")
msg = msg_file.read()
msg_file.close()

nms = open("names.txt","r")
lines = nms.readlines()

msg_file = open("greeting.txt","a")

for line in lines:
    print("{} {}".format(msg,line.strip()))
    msg_file.write("{} {}".format(msg,line.strip()))

msg_file.close()
nms.close()
