# dictionary is like a list which is well formatted, accessed with the key name
family = {
    "father_name": "aderibigbe samuel",
    "mother_name": "rafat oloyinigan",
    "first_child": "itu baba ita",
    "second_child": "dagunro",
    "last_born": "iya gbonkan"
}
'''
family["third_child"] = "raji arowolo"
print(family["father_name"])
family["last_born"] = "omije oju mii"
print(family["last_born"])
print(family)
family.pop("mother_name")
print(family)
'''
for key in family:
    print(f"{key}: {family[key]}")

for key in family.keys():
    print(key)
for values in family.values():
    print(values)