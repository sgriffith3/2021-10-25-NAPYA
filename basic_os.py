import os
import os.path
import shutil

print(os.getcwd())
os.chdir("/home/student")
print(os.getcwd())
f = open("3.txt", "r")
text = f.read()
print(text)
f.close()
shutil.copyfile("1.txt", "first.txt")

if os.path.exists('two.txt'):
    shutil.move("two.txt", "2.txt")
else:
    print("two.txt does not exist")
    if os.path.exists("2.txt"):
        print("2.txt already created")
