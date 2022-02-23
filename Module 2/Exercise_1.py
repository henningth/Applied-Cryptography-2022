"""
Exercise 1: Let plaintext = 0b0110 and key = 0b1101. (Note: in Python, you 
can define an integer by using e.g. x = 0b1111 (which will create a variable 
called x with the value 15). Also note that XOR is only defined between two integers.
(a): Compute the XOR of plaintext and key, call this the ciphertext.
(b): Compute the XOR of ciphertext and the key. What do you observe?
(c): Change one bit of the ciphertext, and compute the XOR of it and the key. 
What happens to the plaintext? (Note: This property is called malleability.)
"""

# (a):
plaintext = 0b0110
key = 0b1101
ciphertext = plaintext ^ key
print("ciphertext: ", bin(ciphertext))

# (b):
result = ciphertext ^ key
print("result: ", bin(result))

# (c):
result2 = 0b1111 ^ key
print("result2: ", bin(result2))