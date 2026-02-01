# RSA Algorithm with User Input

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    # Find modular inverse of e mod phi
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

print("=== RSA Algorithm Implementation ===")

# Step 1: Input from user
p = int(input("Enter a prime number p: "))
q = int(input("Enter another prime number q: "))

# Step 2: Compute n and phi(n)
n = p * q
phi = (p - 1) * (q - 1)
print(f"n = {n}, φ(n) = {phi}")

# Step 3: Choose e
e = int(input("Enter public key exponent e (1 < e < φ(n) and gcd(e, φ(n)) = 1): "))
while gcd(e, phi) != 1:
    print("Invalid e! gcd(e, φ(n)) must be 1. Try again.")
    e = int(input("Enter another e: "))

# Step 4: Compute d
d = mod_inverse(e, phi)
print(f"Private key exponent d = {d}")

# Step 5: Input message
M = int(input(f"Enter message (number less than {n}): "))

# Step 6: Encryption
C = pow(M, e, n)
print(f"Encrypted message C = {C}")

# Step 7: Decryption
M_decrypted = pow(C, d, n)
print(f"Decrypted message M = {M_decrypted}")

print(f"\nPublic Key: (n={n}, e={e})")
print(f"Private Key: (n={n}, d={d})")