import re

data = "Rhea-is a/ coder!"

print("The original string is : " + data)
res = re.split(', |_|-|!', data)
print("The list after performing split functionality : " + str(res))
