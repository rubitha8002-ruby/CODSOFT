# Password Generator - CodSoft Task 3

# User input for password length
pass_len=int(input("Enter your desired password length:"))
import random
import string
# Characters to choose from
strong_pass_chars=string.ascii_letters+string.digits+string.punctuation
# Generating the password
final_password=""
for i in range(pass_len):
    final_password+=random.choice(strong_pass_chars)

print("Generated Password:",final_password)
