import camelcase
c = camelcase.CamelCase()
txt = "welcome to edge project kuet"
print(c.hump(txt))

#This method capitalizes the first letter of each word.


import re
txt = "The rain in Spain and Ukraine"
x = re.findall("ai", txt)
print(x)

#import re

txt = "The Strom in Spain"
x = re.search("Spain", txt)
print(x)

x = re.sub("\s", "  ", txt)
print(x)
txt = "hossain55@gmail.com"
x, y = re.split("\@", txt)
print(x)
print(y)
