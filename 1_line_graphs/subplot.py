from matplotlib import pyplot as plt
from random import randrange

### FUNCTIONS ###

def mod_temperature(list_temp, bool_mod):
    # Modify temperature from list_temp and return list_new_temp
    # If bool_mod = True, add some random degrees Else, remove some random degrees
    list_new_temp = []
    if bool_mod:
        for i in range (0, len(list_temp)):
            list_new_temp.append(list_temp[i])
            list_new_temp[i] += randrange(1,5)
    else:
        for i in range (0, len(list_temp)):
            list_new_temp.append(list_temp[i])
            list_new_temp[i] -= randrange(1,5)
    return list_new_temp

### LIST ###

temperature_chengdu = [5, 7, 8, 9, 12, 16, 28, 32, 35, 25, 22, 12]
temperature_lyon = mod_temperature(temperature_chengdu, True)
temperature_alaska = mod_temperature(temperature_chengdu, False)
month = list(range(12))   
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

plt.plot(month, temperature_chengdu, color="purple", marker="o")
plt.plot(month, temperature_lyon, color="violet", marker="o")
plt.plot(month, temperature_alaska, color="deeppink", marker="o")

plt.title("TEMPERATURE IN CITIES 2019")
plt.xlabel("months")
plt.ylabel("temperature °C")
legend_labels = ["Chengdu", "Lyon", "Alaska"]
plt.legend(legend_labels, loc=2)

ax = plt.subplot()
ax.set_xticks(month)
ax.set_xticklabels(month_names)

plt.axis([-1, 12, min(temperature_alaska)-2, max(temperature_lyon)+2])

plt.show()


