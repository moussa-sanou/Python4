# Basic file operations in Python


# TODO: open a file for writing data
#"w" means write, "r" means read, "a" means append, "r+" means read and write
fp = open("testfile.txt", "w")
fp.write("This is some text\n")
fp.close()

# TODO: read a file's data
with open("testfile.txt", "r") as fp:
    data = fp.read()
    print(data)

# TODO: Add data to an existing file
with open("testfile.txt", "a+") as fp:
    fp.write("This is data added onto the file\n")
    fp.seek(0)
    data = fp.read()
    print(data)