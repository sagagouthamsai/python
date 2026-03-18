#a dictionary can contain itself forming nested dict
child1 = {
  "name" : "goutham",
  "year" : 2006
  }
child2 = {
  "name" : "sai",
  "year" : 2006
  }
child3 = {
  "name" : "siri",
  "year" : 2005
  }

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
  }

#accessing nested dict
print(myfamily["child2"]["name"])

#looping in 
data = {
    "s1": {"name": "Sai", "marks": [90, 85, 88]},
    "s2": {"name": "Ram", "marks": [78, 80, 82]}
}

for student, info in data.items():
    print(student,info["name"])
    
    for mark in info["marks"]:
        print(mark)
