import matplotlib.pyplot as plt

env_map = []

x = [x[0]for x in env_map if x[0] > -800 and x[0] < 800]
y = [y[1]for y in env_map if y[0] > -800 and y[0] < 800]

plt.scatter(x, y)
plt.show()
