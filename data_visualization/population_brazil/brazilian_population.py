# brazilian population growth 1980-2016
import matplotlib.pyplot as plt

data = open("population_br.csv").readlines()

x = []  # years
y = []  # population

for i in range(len(data)):
    if i != 0:
        row = data[i].split(";")
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.bar(x, y, color="#e4e4e4")
plt.plot(x, y, color="k", linestyle="--")

plt.title("brazilian population growth 1980-2016")
plt.xlabel("year")
plt.ylabel("population 1 * 10e8")

plt.savefig("population_br_out.pdf")
