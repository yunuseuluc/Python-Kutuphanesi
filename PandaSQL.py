#Dataset üzerinde sql sorgusu yapma
import pandas as pd
from pandasql import sqldf

data = {
    'id': [1,2,3,4],
    'name': ['Ali','Hamza','Mehmet','Furkan'],
    'age': [25,23,20,69],
    'score': [89,61,70,13]
}

df = pd.DataFrame(data)

query = "SELECT name , age FROM df  where score > 80"

result = sqldf(query, locals())
print(result)