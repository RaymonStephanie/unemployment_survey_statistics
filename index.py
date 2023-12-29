import pandas as pd
df = pd.read_csv("data.csv")
#sanitize
def sanitize():
   columns=["Timestamp","Email Address", "ifpolicy", "howpolicy", "report"]
   for n in columns: del df[n]
   df["ubi"], unreq_1 = pd.factorize(df["ubi"])
   df["edu"], unreq_2 = pd.factorize(df["edu"])
   df["exp"], unreq_3 = pd.factorize(df["exp"])
   df.to_csv("clean_hopeful.csv")
   print("Mapping of responses to numbers:")
   def printna(na):
       for res, n in zip(na, range(len(na))):
           print(f"{res}: {n}")
   printna(unreq_1)
   printna(unreq_2)
   printna(unreq_3)
sanitize()