from allimports import argv

script, fileName = argv

txt = open(fileName)

print(f"here's your file called {fileName}")
print(txt.read())

print("=" * 25, '\r')
print(f"finished showing file contents of {fileName}")

fileName_again = "atomTestText.txt"
txt = open(fileName_again)
print(txt.read())
print(f"finished showing file contents of {fileName_again}")
txt.close()

print(f"""
Preparing to erase the contents of file {fileName_again}""")
print("\r\tIf you don't want this type Ctrl-C (^C). \n\tIf you want to do it hit RETURN")

input('?')

print("Opening file...")
file_handle = open(fileName_again, 'w')
print("Truncating file")

#not needed as 'w' truncates - use 'a' for append


file_handle.truncate()

print("Enter new text for file")
newText1 = input('>>> ')
newText2 = input('>>> ')

print("Writing to file...")

file_handle.write(newText1 + '\n')
file_handle.write(newText2 + '\n')
file_handle.write(f"...Finished entering text from script {script}.....")
file_handle.close()

file_handle = open(fileName_again)
print(file_handle.read())
file_handle.close()

HOME_DIR = "C:\\Users\\StevenAlbury\\"
print(HOME_DIR)




