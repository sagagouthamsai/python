#modifying dictionaries
#we can use key_value to modify the value 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018
print(thisdict)

thisdict.update({"year": 2020})
print(thisdict)
