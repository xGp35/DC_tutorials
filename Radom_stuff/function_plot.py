import matplotlib.pyplot as plt

x= [i for i in range(10)]
y = [max(0, i-3) for i in x]
plt.plot(x, y)
plt.title("ReLU Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()
