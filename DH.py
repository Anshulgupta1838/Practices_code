# Diffie-Hellman Key Exchange Algorithm (Simple Version)

print("=== Diffie-Hellman Key Exchange Implementation ===")

# Step 1: Publicly shared prime number and primitive root
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root of p (g): "))

# Step 2: Private keys for User A and User B
a = int(input("Enter private key for User A: "))
b = int(input("Enter private key for User B: "))

# Step 3: Compute public keys
A = pow(g, a, p)  # g^a mod p
B = pow(g, b, p)  # g^b mod p

print(f"User A's Public Key (A): {A}")
print(f"User B's Public Key (B): {B}")

# Step 4: Exchange and compute shared secret key
key_A = pow(B, a, p)  # (B^a) mod p
key_B = pow(A, b, p)  # (A^b) mod p

print(f"User A's Shared Secret Key: {key_A}")
print(f"User B's Shared Secret Key: {key_B}")

# Step 5: Verify both keys match
if key_A == key_B:
    print(f"\nShared Secret Key Established Successfully: {key_A}")
else:
    print("\nError: Shared keys do not match!")