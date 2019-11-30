#1. Introduction to Seaborn

import seaborn as sns

#2. Using Pandas For Seaborn

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


df = pd.read_csv('survey.csv')
print(df.head())

#3. Plotting Bars with Seaborn

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Load results.csv 
df = pd.read_csv("results.csv")
print(df)

sns.barplot(data= df, x= "Gender", y= "Mean Satisfaction")
plt.show()

#4. Understanding Aggregates

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

gradebook = pd.read_csv("gradebook.csv")
print(gradebook)

assignment1 = gradebook[gradebook.assignment_name == "Assignment 1"]
print("\nGradebook w/ assignment_name == Assignment 1 :\n\n{}".format(assignment1))

assignment2 = gradebook[gradebook.assignment_name == "Assignment 2"]
print("\nGradebook w/ assignment_name == Assignment 2 :\n\n{}".format(assignment2))

asn1_median = np.median(assignment1.grade)
print("\nMedian Grade for assignment1 in Gradebook : {}".format(asn1_median))

#5. Plotting Aggregates

#6. Modifying Error Bars

#7. Calculating Different Aggregates

#8. Aggregating by Multiple Columns

#9. Review