import base64

def encrypt(password, iterations):
    encrypted_pass = password
    a = input("you wanna see all iterations of encryption y/n")

    for c in range(iterations):
        encoded_bytes = base64.b64encode(encrypted_pass.encode())
        encrypted_pass = encoded_bytes.decode()

        if (a.lower() == 'y'):
            print(encrypted_pass)
    return encrypted_pass


#one stage decryption
def decrypt(passw, iterations):
    decrypted_pass = passw  # Initialize with the encrypted password
    a = input("you wanna see all iterations of decryption y/n")
    for i in range(iterations):
        decrypti = base64.b64decode(decrypted_pass.encode())
        decrypted_pass = decrypti.decode()
        if(a.lower()=='y'):
           print(decrypted_pass)
    return decrypted_pass

u_pass = input("Enter password: ")
encrypted_password = encrypt(u_pass, 5)
print(f"Final encrypted password: {encrypted_password}")

dec_pass = decrypt(encrypted_password, 5)
print(f"Final decrypted password: {dec_pass}")
