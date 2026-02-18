data = [{
    "name" : "rezwi",
    "skills" : {
        "html" : "expert",
        "python" : "intermediate"
    },
    "active" : True
},
{
    "name" : "neha",
    "skills" : {
        "html" : "basic",
        "python" : "intermediate"
    },
    "active" : True
},
{
    "name" : "rezwi",
    "skills" : {
        "html" : "intermediate",
        "python" : "basic"
    },
    "active" : False
}]

# Desired output
# Rezwi -> Intermediate



# for d in data:
#     name = d["name"].capitalize()
#     p_level = d["skills"]["python"]
#     print(f"Name : {name} --> Python Level : {p_level}")
#     print(f"Name : {name} --> Python Level : {p_level}")
#     print(f"Name : {name} --> python Level : {p_level}")
#     
    



# my_info = data[0]

# {'name': 'rezwi', 'skills': {'html': 'expert', 'python': 'intermediate'}, 'active': True}

# print(my_info)
# print(my_info['name'])

# print(my_info['skills'])
     
Name : Rezwi----> Skill: intermediate---> Active : True
Name : Neha----> Skill: intermediate---> Active : True
Name : Rezwi----> Skill: basic---> Active : False
Name : Rezwi
Name : Rezwi----> Skill: basic---> Active : False



for i in data:
    name = i['name'].capitalize()
    level = i['skills']['python']
    Status = i['active']
    print(f"Name : {name}----> Skill: {level}---> Active : {Status}")
    Status = i['active']
    if Status == False:
         print (f"Name : {name}")
         print(f"Name : {name}----> Skill: {level}---> Active : {Status}")
    