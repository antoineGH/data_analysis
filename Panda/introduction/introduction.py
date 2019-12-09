import pandas as pd

# --- FUNCTIONS

def df_info(df):
    df_lines, df_columns = df.shape
    print(f"Dataframe has {df_columns} columns and {df_lines} entries")

    for i in range(df_columns):
        print(f"| {df.columns[i]} |")

    print(f"\n{df.head(2)}\n")


# --- DATAFRAME DECLARATION

# From a dictionnary
df1 = pd.DataFrame({
    'Product ID': [1, 2, 3, 4],
    'Product Name': ["t-shirt", "t-shirt", "skirt", "skirt"],
    'Color': ["blue", "green", "red", "black"]
    })

# From a list of lists
df2 = pd.DataFrame([
    [1, 'San Diego', 100],
    [2, 'Los Angeles', 120],
    [3, 'San Francisco', 90],
    [4, 'Sacramento', 115]
    ],
     columns=['Store ID', "Location", "Number of Employees"])

# Write a CSV 

#name,cake_flavor,frosting_flavor,topping
#Devil's Food,chocolate,chocolate,chocolate shavings
#Birthday Cake,vanilla,vanilla,rainbow sprinkles
#Carrot cake,carrot,cream cheese,almonds

# From a CSV

df3 = pd.read_csv("E:/git/data_analysis/seaborn/seaborn_distribution/fifa.csv")

# --- CODE
 
df_info(df1)
df_info(df2)
df_info(df3)

