import pandas as pd

df = pd.read_json("data.json")
data_structure = df.to_dict(orient="records")


print(data_structure[2]["headquarters"])

# there is a variable called data_structure, which is in list format
# In which we have to access index 1 data
# And after accessing the index data we came to know that, 
# it is returning Dictionary data,
# we needed value of 'assest data', it returns a list
# Again we needed  data of index [0] from it,
# then data of 'version' key which was again a list data 
# we accessed last data by '[-1]' index,then
# then finally we accessed version number by 'v' key  
print(data_structure[1]["assets"][0]["versions"][-1]["v"])


print(data_structure[1]["assets"][0]["versions"][-1]["stable"])

print(data_structure[0]["assets"])