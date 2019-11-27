from matplotlib import pyplot as plt

#x_values = [0, 1, 2, 3, 4]
#y_values = [0, 1, 4, 9, 16]

#plt.plot(x_values, y_values)

#plt.show()

# Example

#days = list(range(0,7))
#money_spent = [10, 12, 12, 10, 14, 22, 24]

#plt.plot(days, money_spent)

#plt.show()

# Example 2

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]
costs2 = [300, 1000, 1100, 1100, 1020]

# Alpha opacity : 0.5
# LineStyle : -- o
# Color : https://matplotlib.org/3.1.0/gallery/color/named_colors.html
# Marker o s *
plt.plot(time, revenue, color='gold', linestyle=':', marker='s', alpha=0.5)
plt.plot(time, costs, color='fuchsia', linestyle='--', marker='*')
plt.plot(time, costs2, color='chocolate', marker='o', alpha=0.5)

plt.show()

# Change Axis (Zoom)

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)

# [x_min, x_max, y_min, y_max]
plt.axis([0, 12, 2900, 3100])
plt.show()

# Title, Label x, Label y 
# plt.xlabel("string") plt.ylabel("string") plt.title("string")

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])
plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')
plt.title('My Last Twelve Years of Coffee Drinking')
plt.show()

# Subplot

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.subplot(2, 3, 1)
plt.plot(months, temperature, color='grey', marker="o")
plt.title("Subplot1")
plt.xlabel("months")
plt.ylabel("temperature")

plt.subplot(2, 3, 3)
plt.plot(flights_to_hawaii, temperature, color="black", marker="o")
plt.title("Subplot2")
plt.xlabel("flights_to_hawaii")
plt.ylabel("temperature")

plt.subplot(2, 3, 5)
plt.plot(months, temperature, color='darkorange', marker="o")
plt.title("Subplot3")
plt.xlabel("months")
plt.ylabel("temperature")

plt.show()

# Subplot 2

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.subplot(2,1,1)
plt.plot(x, straight_line)

plt.subplot(2,2,3)
plt.plot(x, parabola)

plt.subplots_adjust(wspace=0.35)
plt.subplots_adjust(bottom=0.2)

plt.subplot(2,2,4)
plt.plot(x, cubic)

plt.show()

# Legends (loc from 0 to 10)

months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

#create your legend here
legend_labels = ["Hyrule", "Kakariko", "Gerudo Valley"]

plt.legend(legend_labels, loc=8)

plt.show()

# Modify Ticks (pas)

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

# Your work here
ax = plt.subplot()

ax.set_xticks(months)
ax.set_xticklabels(month_names)

ax.set_yticks([0.25, 0.5, 0.75])
ax.set_yticklabels(['25%', '50%', '75%'])

plt.show()

# Figures

word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

# Close existing plot
plt.close('all')

plt.figure()
plt.plot(years, word_length)
plt.savefig('winning_word_lengths.png')
plt.show()

plt.figure(figsize=(7,3))
plt.plot(years, power_generated)
plt.savefig('power_generated.png')
plt.show()

# Review

x = [63, 65, 68, 70, 72, 73, 76, 78, 81, 90, 98, 104]
y1 = [52, 52, 53, 68, 73, 74, 74, 76, 81, 82, 88, 94]
y2 = [98, 99, 99, 100, 110, 111, 115, 117, 118, 120, 150, 140]

legend_labels = ["Pink Line", "Grey Line"]

plt.legend(legend_labels, loc=8)

plt.plot(x, y1, color="pink", marker="o")
plt.plot(x, y2, color="gray", marker="o")
plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")
plt.legend(legend_labels, loc=4)
plt.show()


