cat = {"name": "deepak", "age": 23, "is_raining": True, "town":"rajahmundry","loaction":"ap","contact":1234565}
for k,v in cat.items():
    print("this is {} detailes and in formation {}".format(k,v))
print(cat.items())
print([cat])

deep = ["this", 34,"incrment","values"]
print(deep)
print("ages" in cat)
print(deep,"this is deepak")
del cat["is_raining"]
print(cat)
print(deep.clear())
print(deep)

dist = cat.copy()
print(dist)
print(dict.fromkeys(cat,"deepalk"))

print(cat.get("age"))
print(cat.items())
print(cat.keys())
print(dict.values(cat))
sai = {"sex": "male", "address":"rjy"}
cat.update(sai)
print(cat)
print(cat.setdefault("vakeus",None))
print("this" in cat)
print(cat.pop("age"))


dep = {"name":"sai","job":[{"employe":"HCL", "town":"chennai"},
                           {"employe":"HCL", "town":"chennai"}
                           ]}
for employee in dep['job']:
    print("sai" in employee)


dist_dict={num : ("EVEN" if num % 2 == 0 else "ODD")for num in range(0,100)}

print(dist_dict)




print(cat["name"])














