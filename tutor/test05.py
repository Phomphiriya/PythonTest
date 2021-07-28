dict = {
    "name":"Boom",
    "age":"19",
    "height" : "180"
}
add ={"weight" : "60"}
dict.update(add)

print(dict["name"])
print(dict.get("age"))

lsKey = list(dict.keys())
lsValue = list(dict.values())

index = lsValue.index("19")
print(lsKey[index])
print(dict)