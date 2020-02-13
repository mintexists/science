import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
from numpy.random import rand

net = NetworkReader.readFrom('/Users/mac/weights.xml') 
data = open("/Users/mac/data.json", "r").read()
data = json.loads(data)

x = random.randrange(0, 1000)
print("expected: " + str(data[x+1]["main"]["temp"]))


ax.scatter(data(x, ["temp"]))
ax.scatter(x+1, ["temp"])
ax.scatter(x+2, ["temp'])
ax.scatter(x+3, ["temp'])
ax.scatter(x+4, ["temp"])                
ax.scatter(x+5, ["temp"])
ax.scatter(x+6, ["temp"])
                 
ax.set_xlabel('Days', fontsize=15)
ax.set_ylabel('Temperature', fontsize=15)
ax.set_title('Temperature Chart in Degrees Farenhite')

fig, ax = plt.subplots()
ax.grid(True)
plt.show()


