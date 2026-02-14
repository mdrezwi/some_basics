import pandas as pd

df = pd.read_json("data.json")
data_structure = df.to_dict(orient="records")

for s in data_structure:
     print(s["division"])

    
