import matplotlib.pyplot as plt


values1 = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]

plt.plot(range(1,11), values1, 'b-s')
#plt.plot(range(1,11), values2, 'g-*')


plt.plot(range(1, 11), values2, color='orange', marker='*',markerfacecolor='green', markeredgecolor='green')

plt.xlabel('Entries') 
plt.ylabel('Values')

plt.legend(['First', 'Second'], loc=9)
plt.annotate("Sommet", xy=(8, 10))

             
plt.show()

