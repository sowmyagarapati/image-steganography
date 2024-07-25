import cv2
import string
import os
image_path = input("Enter the path to the image : ")
x = cv2.imread(image_path)
if x is None:
    print("Error: Could not load the image.")
    exit()
h, w, ch = x.shape
password = input("Enter the password: ")
msg = input("Enter secret message: ")
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}
tln = len(msg)
kl = 0
z = n = m = 0
l = min(tln, h * w * ch)
for i in range(l):
    x[n, m, z] = d[msg[i]] ^ d[password[kl]]
    n += 1
    m += 1
    z = (z + 1) % 3
    kl = (kl + 1) % len(password)
encrypted_image_path = "encrypted.jpg"
cv2.imwrite(encrypted_image_path, x)
print("Data hiding in image completed successfully.")
ch = int(input("\nEnter 1 to extract data from image: "))
while True:
    if ch == 1:
        while True:
            p1 = input("\nEnter password to extract the secret data: ")
            if password == p1:
                decrypt = ""
                n = m = z = 0
                for i in range(l):
                    decrypt += c[x[n, m, z] ^ d[password[kl]]]
                    n += 1
                    m += 1
                    z = (z + 1) % 3
                    kl = (kl + 1) % len(password)
                print("Secret message:", decrypt)
                break
            else:
                print("Passwords do not match. Try again!")
    else:
        print("Invalid choice. Try again!")
    break
