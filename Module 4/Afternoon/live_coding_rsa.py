"""
Live coding: RSA
• Write a Python program that implements a simple RSA scheme
• Use p=7 and q=11
• Add code that computes the modulus n and generates the private key e and
public key d (use small numbers for simplicity)
• Use the generated private key to encrypt a message
• Use the generated public key to decrypt the ciphertext
"""

"""
RSA: Key generation
• 1: Choose randomly two large prime numbers p and q (of size 2048 bits)
• Lower numbers (of size 1024 bits) compromise security
"""
p = 7  # Chosen per live coding text
q = 11

print("Prime numbers:")
print("p:", p, " q:", q)
"""
• 2: Let n = p * q be the modulus. This number is known to all
• This part is crucial, easy to multiply, difficult to factorize
"""
n = p*q
print("Modulus n:", n)

"""
• 3: Find a number e such that e and (p-1)*(q-1) have no common prime factors
• Technical requirement on e, Greatest Common Divisor of e and (p-1)*(q-1) is 1
"""
def gcd(a, b):
    while a != b:
        if a == 0:
            break
        a, b = b % a, a
    return b

for e in range(2,(p-1)*(q-1)):
    result = gcd(e, (p-1)*(q-1))
    if result == 1: # They don't have common prime factors
        break

print("Public exponent e:", e)

"""
• 4: Find the inverse of e, call it d.
• e * d = 1 mod (p-1)*(q-1)
• We get public key: (n,e), private key: d
"""

for d in range(2,(p-1)*(q-1)):
    result = e*d % ((p-1)*(q-1))
    if result == 1:
        break

print("Private key d:", d)

"""
Encrypt a message
"""

p = 5 # Plaintext
c = p**e % n # Ciphertext ( Encryption formula (RSA))
print("Plaintext p:", p)
print("Ciphertext c:", c)

"""
Decrypt a message
"""
dp = c**d % n # Decryption formula (RSA)
print("Decr. pl.text:", dp)
