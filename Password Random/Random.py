import random

characters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz1234567890!#@$%&/="

password = ""

for i in range(16):
    password += random.choice(characters)


print(f"Your Password Is: {password}")
