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

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv("gradebook.csv")
sns.barplot(data=gradebook, x="assignment_name", y="grade")
plt.show()

#6. Modifying Error Bars

import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv("gradebook.csv")

sns.barplot(data=gradebook, x="name", y="grade", ci="sd")
plt.show()

#7. Calculating Different Aggregates

import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("survey.csv")

print(df)

#sns.barplot(data=df, x="Gender", y="Response", estimator=len)
sns.barplot(data=df, x="Gender", y="Response", estimator=np.median)
plt.show()

#8. Aggregating by Multiple Columns

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("survey.csv")

print(df)
#sns.barplot(data=df, x="Gender", y="Response", hue="Age Range")
sns.barplot(data=df, x="Age Range", y="Response", hue="Gender")
plt.show()

#9. Review

#To review the seaborn workflow:
#1. Ingest data from a CSV file to Pandas DataFrame.
df = pd.read_csv('file_name.csv')
#2. Set sns.barplot() with desired values for x, y, and set data equal to your DataFrame.
sns.barplot(data=df, x='X-Values', y='Y-Values')
#3. Set desired values for estimator and hue parameters.
sns.barplot(data=df, x='X-Values', y='Y-Values', estimator=len, hue='Value')
#4. Render the plot using plt.show().
plt.show()