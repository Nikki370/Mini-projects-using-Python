import random
import string

password = ""
container = string.ascii_letters + string.digits + string.punctuation

# while True:
#     val = random.choice(container)
#     password += val
#     if len(password) == 8:
#         break
# print("Your random password is:",password)


# or with help of list
password = []

while True:
    val = random.choice(container)
    password.append(val)
    if len(password) == 8:
        break
# IT IS IN THE FORM OF LIST, WE CAN CONVERT LIST TO CONCATENATE  BY USING "".join
res = "".join(password)
#  after this we will get the same result
print("Your random password is:",res)
