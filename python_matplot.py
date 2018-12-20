from matplotlib import pyplot as plt

plt.plot(['Seoul', 'Paris', 'Seattle'], [30,25,55])
plt.plot(['Seoul', 'Paris', 'Seattle'], [10,20,75])
plt.xlabel('City')
plt.ylabel('Response')
plt.legend(['Population','store'])
plt.title('Experiment Result')
plt.show()
