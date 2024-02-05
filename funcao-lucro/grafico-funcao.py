import matplotlib.pyplot as plt

def lucro(x):
    return (x * (600 - x) - 2 * (600 - x))

x = range(0, 600)

lucro = [lucro(i) for i in x]

plt.plot(x, lucro)
plt.scatter(301, lucro[301], color='red', marker='o')
plt.show()