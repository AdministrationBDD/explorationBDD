import pandas as pd

from prophet import Prophet
print("fdfd")
df= pd.read_csv("C:\\Users\\Jeremy\\Documents\\Ynov\\python\\projet_explorationBDD\\Bdd.csv")
df.head()
m = Prophet()
m.fit(df)
futuresVente = m.make_future_dataframe(periods=300)
futuresVente.tail(10)