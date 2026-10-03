### **What is Symmetric Encryption?**
* Symmetric Encryption is an encryption method where the same key is used for both:
  * Encrypting (converting plaintext into ciphertext)
  * Decrypting (converting ciphertext back into plaintext)
```python
# Example
Suppose the secret key is:
Key = mysecret123

# Original Data (Plaintext):
Hello Mohit

# After encryption:
X7#kP9@Lm2
```

#### Popular Symmetric Encryption Algorithms
| Algorithm | Key Size           |
| --------- | ------------------ |
| AES       | 128, 192, 256 bits |
| DES       | 56 bits            |
| 3DES      | 168 bits           |
| Blowfish  | 32-448 bits        |
| ChaCha20  | 256 bits           |
* **AES-256** is the most commonly used today.

### Advantages of Symmetric Encryption
* ✅ Very fast
* ✅ Suitable for large amounts of data
* ✅ Less CPU usage
* ✅ Commonly used in databases, file encryption, VPNs


### Disadvantages of Symmetric Encryption
* ❌ Key sharing problem
* Both sender and receiver must securely share the same key.
* If someone steals the key, they can decrypt all messages.

#### Python Example
* Using the **cryptography** package:
* **cryptography** Python ka ek security/cryptography package (library) hai, jiska use Python applications mein encryption, decryption, hashing, digital signatures, keys etc. ke liye kiya jata hai.

```python
# install
pip install cryptography
```

```python
from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key() # ➡️ secret encryption key generate karta hai.

cipher = Fernet(key)

# Encrypt
encrypted = cipher.encrypt(b"Hello Mohit")  # ➡️ Data ko encrypt karta hai.
print(encrypted)

# Decrypt
decrypted = cipher.decrypt(encrypted)   # ➡️ Data ko decrypt karta hai.
print(decrypted.decode())
```


### **What is Asymmetric Encryption?**
* Asymmetric Encryption ek cryptographic technique hai jisme 2 different keys use hoti hain:
  * Public Key 🔓
  * Private Key 🔐
* Important: Public key ko share kiya ja sakta hai, lekin private key secret rakhni hoti hai.
* **RSA** asymmetric encryption ka famous algorithm hai.
* Other examples:
  * RSA
  * ECC (Elliptic Curve Cryptography)
  * ElGamal
```python
Original Data
     ↓
Encrypt with Public Key
     ↓
Encrypted Data
     ↓
Decrypt with Private Key
     ↓
Original Data
```
* Real-world example:- HTTPS/TLS mein asymmetric cryptography ka use secure key establishment/authentication ke liye hota hai, while actual bulk data encryption generally symmetric encryption se hota hai.

### Symmetric vs Asymmetric?
| Feature  | Symmetric             | Asymmetric               |
| -------- | --------------------- | ------------------------ |
| Keys     | 1 key                 | 2 keys                   |
| Keys     | Same secret key       | Public + Private         |
| Speed    | Fast                  | Relatively slow          |
| Example  | AES                   | RSA, ECC                 |
| Main use | Large data encryption | Key exchange, signatures |
