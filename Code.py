import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("tem.csv")
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.xlabel('Days')
plt.ylabel('Temperature (Celsius)')
plt.ylim(-10, 35)  # Set the y-axis limits
plt.yticks(range(-10, 31, 10))  # Set the major y-tick marks every 10 units
plt.xticks(range(1, 370, 28))  # Set the major x-tick marks every 28 units
plt.show()
