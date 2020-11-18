#Email Collector

import re

str = '''

'''


email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+",str)
print(email)
# print(type(email))
num = 0
for mail in email:

    with open("Email_list.txt","a") as f:
        num = num+1
        f.write(f"Email- {num} = {mail}"+"\n")






