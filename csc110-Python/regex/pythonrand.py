import re
print(__doc__)

einstein1 = "Logic will get you from A to Z"
print("re.sub")
einstein2 = re.sub("a", "aa", einstein1)
einstein3 = re.sub("e", "ee", einstein2)
einstein4 = re.sub("i", "ii", einstein3)
einstein5 = re.sub("o", "oo", einstein4)
einstein6 = re.sub("u", "uu", einstein5)
print(einstein6)
print("re.split")
tokenlist = re.split("\s", einstein6)
print(tokenlist)
print("re.fineall")
foundlist = re.findall("ee", einstein6)
print(foundlist)
print("end")
