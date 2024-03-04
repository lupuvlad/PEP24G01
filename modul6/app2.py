text = "Hello, World!"

encrypted_text = ""

for char in text:
    encrypted_text += chr(ord(char) ^ 200)
print(encrypted_text)

decrypted_text = ""
for char in encrypted_text:
    decrypted_text += chr(ord(char) ^ 200)
print(decrypted_text)