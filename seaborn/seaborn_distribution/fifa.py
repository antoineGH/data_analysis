from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# Import Dataframe !!! Full Path
df = pd.read_csv("E:/git/data_analysis/seaborn/seaborn_distribution/fifa.csv")

#print(df.head(10))

### shape return tupple with number of rows and columns
#df_shape = df.shape
#rows, columns = df_shape

#print(f"Rows: {rows}, Columns: {columns}")

### return panda object with dataframe's columns
#print(df.columns)

### Create columns
df["Total Goals"] = df["Home Team Goals"] + df["Away Team Goals"]
#print(df["Total Goals"].head(10))

### Plot Seaborn Style
sns.set_style("whitegrid")
sns.set_context(context="poster", font_scale=0.8)

f, ax = plt.subplots(figsize=(12, 7))
ax = sns.barplot(data = df, x= df["Year"], y= df["Total Goals"], ci=None)
ax.set_title("Average Number Of Goals Scored In World Cup Matches By Year")
plt.xticks(rotation=45)
plt.show()

goals_df = pd.read_csv("E:/git/data_analysis/seaborn/seaborn_distribution/goals.csv")

#print(goals_df.head())
#print(goals_df.columns)

### Box Plot
sns.set_style("whitegrid")
sns.set_context(context="poster", font_scale=0.8)

f, ax2 = plt.subplots(figsize=(12, 7))

sns.boxplot(data=goals_df, x= goals_df["year"], y= goals_df["goals"])
ax2.set_title("Distribution of the goals data")
plt.xticks(rotation=45)
plt.show()

