%matplotlib inline
import matplotlib.pyplot as plt
import statistics

Set x & y axis to a list of strings (months) and floats (dollars per month)
x_axis = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]

# Create Line Chart plot
plt.plot(x_axis, y_axis)

# Create the plot with ax.plt() - switch from MATLAB to 
# the object-oriented interface method

fig, ax = plt.subplots() # Create figure
ax.plot(x_axis, y_axis) # Define axes

# Create the plot with ax.plt() - METHOD 2 (METHOD 1 ABOVE)
fig = plt.figure() # Change attributes - axis labels, title, legend, save figure as image
ax = fig.add_subplot()
ax.plot(x_axis, y_axis)

# Create the plot with ax.plt()
ax = plt.axes()
ax.plot(x_axis, y_axis)

# Create the plot using 'plt.show()'
# Looks for all the active figure objects and opens a window
# that displays them if you have two or more sets of data to plot.
plt.plot(x_axis, y_axis)
plt.show()
# CAN ONLY BE USED ONCE PER SESSION OR NEED TO RESTARD KERNEL AND CLEAR OUTPUT

# Annotating a CHART
# Create the plot and add a label for the legend.
plt.plot(x_axis, y_axis, label='Boston')
# Create labels for the x and y axes.
plt.xlabel("Date")
plt.ylabel("Fare($)")
# Set the y limit between 0 and 45.
plt.ylim(0, 45)
# Create a title.
plt.title("PyBer Fare by Month")
# Add the legend.
plt.legend()

# Declare parameters for line color, width and marker by setting
# parameters in plt.plot()

plt.plot(x_axis, y_axis, marker="*", color="blue", linewidth=2, label='Boston')
plt.xlabel("Date")
plt.ylabel("Fare($)")
plt.ylim(0, 45)
plt.title("PyBer Fare by Month")
plt.grid()
plt.legend()

# Module 5.1.5 Create and annotate vertical and horizontal bar charts - MATLAB APPROACH
# Create the vertical bar chart with plt.bar
plt.bar(x_axis, y_axis)

# Annotate the bar chart - MATLAB APPROACH
plt.bar(x_axis, y_axis, color="green", label='Boston')
plt.xlabel("Date")
plt.ylabel("Fare($)")
plt.title("PyBer Fare by Month")
plt.legend()

# Create the horizontal bar chart - MATLAB APPROACH
plt.barh(x_axis, y_axis)

# Switch Axis - MATLAB APPROACH
plt.barh(y_axis, x_axis)

# Create the plot using gca() method (Get Current Value) - 
# invert the y-axis to have the months in ascending order - MATLAB APPROACH
plt.barh(x_axis, y_axis)
plt.gca().invert_yaxis()

# Module 5.1.5 Create and annotate vertical and horizontal bar charts - OBJECT-ORIENTED APPROACH
# Create the vertical bar chart with ax.plt() - OBJECT-ORIENTED APPROACH
fig, ax = plt.subplots()
ax.bar(x_axis, y_axis)

# Create the horizontal bar chart with ax.plt() - OBJECT-ORIENTED APPROACH
fig, ax = plt.subplots()
ax.barh(x_axis, y_axis)

# Switch Axis - OBJECT-ORIENTED APPROACH
# Create the plot with ax.plt()
fig, ax = plt.subplots()
ax.barh(y_axis, x_axis)

# Module 5.1.7 - Create Scatter Plots and Bubble Charts - MATLAB METHOD
# plt.plot() METHOD
plt.plot(x_axis, y_axis, 'o') # 'o' is for scatter plot

# plt.scatter() METHOD - MATLAB METHOD
plt.scatter(x_axis, y_axis)

# BUBBLE CHART - MATLAB METHOD
plt.scatter(x_axis, y_axis, s=y_axis)

# Multiply the size of the bubble dots by 3 - METHOD 1 - MATLAB METHOD
y_axis_larger = []
for data in y_axis:
  y_axis_larger.append(data*3)

# Then use new y-axis for 's' - METHOD 1 - MATLAB METHOD
plt.scatter(x_axis, y_axis, s=y_axis_larger)

# List Comprehension - replace for and while loops - METHOD 2 - MATLAB METHOD
plt.scatter(x_axis, y_axis, s = [i * 3 for i in y_axis])

# Create scatter plot - OBJECT-ORIENTED METHOD
fig, ax = plt.subplots()
ax.scatter(x_axis, y_axis)

# Bubble chart - OBJECT-ORIENTED
fig, ax = plt.subplots()
ax.scatter(x_axis, y_axis, s=y_axis)

# Module 5.1.8 - Pie Charts - MATLAB METHOD
# - NOTE - Pie requires values and labels that are in an array
plt.pie(y_axis, labels=x_axis)
plt.show()

# Add percentages and "explode" largest percentage (july) using "0.2"
plt.subplots(figsize=(8, 8)) # uncrowds the labels
explode_values = (0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0)
plt.pie(y_axis, explode=explode_values, labels=x_axis, autopct='%.1f%%')

# Assign 12 colors, one for each month.
colors = ["slateblue", "magenta", "lightblue", "green", "yellowgreen", "greenyellow", "yellow", "orange", "gold", "indianred", "tomato", "mistyrose"]
explode_values = (0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0)
plt.subplots(figsize=(8, 8))
plt.pie(y_axis,
    explode=explode_values,
    colors=colors,
    labels=x_axis,
    autopct='%.1f%%')

plt.show()

# Module 5.1.8 - Pie Charts - OBJECT-ORIENTED METHOD
fig, ax = plt.subplots()
ax.pie(y_axis,labels=x_axis)
plt.show()

# Get Standard Dev
stdev = statistics.stdev(y_axis)
stdev

# Add error bar
plt.errorbar(x_axis, y_axis, yerr=stdev)

# Add "cap" to lines
plt.errorbar(x_axis, y_axis, yerr=stdev, capsize=3)

# Add Error bars and a capsize - Object-Oriented
fig, ax = plt.subplots()
ax.errorbar(x_axis, y_axis, yerr=stdev, capsize=3)
plt.show()

# Add error bars to a bar chart - Pyplot
plt.bar(x_axis, y_axis, yerr=stdev, capsize=3)

# Add error bars to a bar chart - Object-Oriented
fig, ax = plt.subplots()
ax.bar(x_axis, y_axis, yerr=stdev, capsize=3)
plt.show()

# Adjust 'major x-axis ticks' on horizontal bar chart - Pyplot
import numpy as np
plt.barh(x_axis, y_axis)
plt.xticks(np.arange(0, 51, step=5.0)) # step=5.0 makes intervals of 5
plt.gca().invert_yaxis()

# arange function - zero to fifty in increments of 5
np.arange(0, 51, step=5.0)

# Adjust 'major x-axis ticks' on horizontal bar chart - Object-Oriented
fig, ax = plt.subplots()
ax.barh(x_axis, y_axis)
ax.set_xticks(np.arange(0, 51, step=5.0))
plt.show()

# Add Minor ticks to bar chart
from matplotlib.ticker import MultipleLocator # multiplelocator method pass how often we want our minor ticks
# Increase the size of the plot figure.
fig, ax = plt.subplots(figsize=(8, 8))
ax.barh(x_axis, y_axis)
ax.set_xticks(np.arange(0, 51, step=5.0))

# Create minor ticks at an increment of 1.
ax.xaxis.set_minor_locator(MultipleLocator(1))
plt.show()