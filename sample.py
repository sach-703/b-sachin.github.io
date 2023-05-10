from mymodule import add

print("Hello world")
print("Imaginary error fixed")

print(add(2,3))

with open("greeting.txt", "r") as f:
    print(f.read())

msg_file = open("greeting.txt","r")
msg = msg_file.read()

nms = open("names.txt","r")
lines = nms.readlines()

for line in lines:
    print("{} {}".format(msg,line.strip()))

msg_file.close()
nms.close()