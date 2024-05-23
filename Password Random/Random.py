import random

chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz1234567890!#@$%&/="

password = ""

for i in range(16):
    password += random.choice(chars)


print(f"Your Password Is: {password}")
