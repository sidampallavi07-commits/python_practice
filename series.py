import pandas as pd

#data=[100,102,104,200,202]

#series=pd.Series(data,index=['a','b','c','d','e'])


#print(series [series<200])

#calories={"day 1":1750,"day 2":2100,"day 3":1700}
#series=pd.Series(calories)

#print(series[series <2000])



city={1:"mumbai",2:"pune",3:"Nepal",4:"dubai",5:"UAS",6:"INDIA"}
series=pd.Series(city)
print(series)




import pandas as pd
data={"Name":["pallavi", "Aditya","Ashutosh"],
      "Age":[24,18,21]
      }
df=pd.DataFrame(data,index=["employee 1","employee 2","employee 3"])

# Add a new column

df["job"]= ["cook","N/A","cashier"]


# Add a new row

new_rows=pd.DataFrame([{"Name":"vanita","Age":47,"job":"Gov_Emp"},
                      {"Name": "Ambadas","Age":54,"job":"Self Emp"}],
                     index=["employee 4","employee 5"])
df=pd.concat([df,new_rows])
print(df)





