import pandas as pd

df = pd.read_json("data.json")
data_structure = df.to_dict(orient="records")

# Goal : To count total number of divisions

# setting an initial value to store count, initial value set to 0
count=0

# we will loop through all data
for s in data_structure:
    #print(s['division'])   # we don't need to print divisions to just count it 

    count += 1      # we will increment external variable count by 1 in each loop
                    # external variable count's value will keep increasing in each loop
    
print(f"Count : {count}")        # finally we will print the count
                                 # we use f string to add some more information
         

    
    
      
    
   
    
    
    
        
        
        
        
        
#         
# c = 0
# 
# for _ in data_structure:
#     c = c+1
# 
# print(f"Total number of division is {c}")
    
    










