"""
Exercise 1: Write a Python program which takes a string as input, and prints the individual byte values of the string
"""
"""
def split(str):
    return [chr for chr in str]

string1 = input("Enter a string: ")
strList = split(string1)
print(strList)
for chr in strList:
    print(bin(ord(chr)))
"""
"""
Exercise 2: Write a Python program which takes a positive integer as input and prints the binary and hexadecimal representation of this integer.
"""
"""
number = input("Enter number: ")
print(bin(int(number)))
print(hex(int(number)))
"""
"""
Exercise 3: Write a Python program which takes a text string as input and saves it as UTF-8 encoded variable. Test if it works when using Danish letters such as æ, ø, å.
"""
"""
string1 = input("Enter string: ")
stringEncoded = string1.encode('UTF-8')
print(stringEncoded)

decodedString = stringEncoded.decode('UTF-8')
print(decodedString)
"""
"""
Exercise 4: Repeat the previous exercise but encode the string in ASCII instead of UTF-8. Does it work? Why or why not?
"""
"""
string1 = input("Enter string: ")
stringEncoded = string1.encode('ASCII')
print(stringEncoded)

decodedString = stringEncoded.decode('UTF-8')
print(decodedString)
"""
"""
Exercise 5: Write a Python program that opens a PNG file in binary mode and prints the first 8 bytes of the file (its signature). Compare with https://en.wikipedia.org/wiki/Portable_Network_Graphics#File_header
"""
with open("./dice.png", "rb") as png:
    f = png.read()
    d = bytearray(f)
    print(d[:8])