import matplotlib.pyplot as plt 

input_value = [1, 2, 3, 4, 5, 6, 7]
output_value = [1, 4, 9, 16, 25, 36, 49]

plt.plot(input_value, output_value, linewidth = 2)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()