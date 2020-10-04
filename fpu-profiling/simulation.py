import os
import time
import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
N = [10** i for i in range(3,7)]
lista = []
for i in range(100):
	for n in N:
		time_i = time.time()
		os.system("./teste_soma %d > out.txt" % (n))
		time_f = time.time()
		time_soma = time_f - time_i

		time_i = time.time()
		os.system("./teste_soma_d %d > out.txt" % (n))
		time_f = time.time()
		time_soma_d = time_f - time_i

		time_i = time.time()
		os.system("./teste_mult %d > out.txt" % (n))
		time_f = time.time()
		time_mult = time_f - time_i

		time_i = time.time()
		os.system("./teste_mult_d %d > out.txt" % (n))
		time_f = time.time()
		time_mult_d = time_f - time_i

		lista.append([n,"fp add", time_soma])
		lista.append([n,"fp mult", time_mult])
		lista.append([n,"double add", time_soma_d])
		lista.append([n,"double mult", time_mult_d])

df = pd.DataFrame(lista, columns = "N,op,time(s)".split(","))
sns.barplot(x="N",y="time(s)", hue="op", data = df)
plt.show()
pickle.dump( df, open("data.pkl","wb"))
