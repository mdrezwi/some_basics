import pandas as pd

df = pd.read_json("data.json")
# print(df)
data_structure = df.to_dict(orient="records")
# 
#   for s in data_structure:
#       d = "Data Science"
#       if s["division"] == d
#           h = s["management"]["VP"]
#           print(f"VP of {d} divison is {h}")

for s in data_structure:
     print(s)
         

    
    
      
    
   
    
    
    
        
        
        
        
        
#         
# c = 0
# 
# for _ in data_structure:
#     c = c+1
# 
# print(f"Total number of division is {c}")
    
    










