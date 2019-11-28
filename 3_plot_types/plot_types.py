#1. Introduction

#2. Simple Bar Chart

from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

x_values = range(len(sales))
plt.bar(drinks, sales)

plt.show()

#3. Simple Bar Chart II

from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

ax = plt.subplot()
ax.set_xticks(range(0, len(drinks)))
ax.set_xticklabels(drinks)

plt.show()

#4. Side-By-Side Bars

from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
legend_label = ["Store1","Store2"]

n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element
             in range(d)]

plt.bar(store1_x, sales1)

n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = len(drinks) # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element
             in range(d)]

plt.bar(store2_x, sales2)
plt.legend(legend_label)

plt.show()

#5. Stacked Bars

from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
legend_labels = ["Location 1", "Location 2"]
drink_nb = list(range(6))  

plt.bar(range(len(drinks)), sales1)
plt.bar(range(len(drinks)), sales2, bottom=sales1)


plt.legend(legend_labels)

ax = plt.subplot()
ax.set_xticks(drink_nb)
ax.set_xticklabels(drinks)
plt.yticks([])

plt.show()

#6. Error Bars

from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

plt.bar(range(len(drinks)), ounces_of_milk, yerr=error, capsize=10)

plt.show()

#7. Fill Between

from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]
y_lower = [0.9*i for i in revenue]
y_upper = [1.1*i for i in revenue]

plt.fill_between(months, y_lower, y_upper, alpha=0.2, color="lightgray")
plt.plot(months, revenue, color="coral", marker='o')
plt.grid(True)

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)

plt.show()

#8. Pie Chart

from matplotlib import pyplot as plt
import numpy as np

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs)
plt.axis('equal')

plt.show()

#9. Pie Chart Labeling

from matplotlib import pyplot as plt

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]
color_pie = ["gray", "blue", "green", "red"]

plt.pie(payment_method_freqs, autopct='%0.1f%%', colors=color_pie)
plt.axis('equal')
plt.legend(payment_method_names)

plt.show()

#10. Histogram

from matplotlib import pyplot as plt
#from script import sales_times

plt.hist(sales_times, bins=20)

plt.show()

#11. Multiple Histograms

from matplotlib import pyplot as plt
#from script import sales_times1
#from script import sales_times2

plt.hist(sales_times1, bins=20, alpha=0.4, normed=True)
plt.hist(sales_times2, bins=20, alpha=0.4, normed=True)
plt.grid(True)

plt.show()



