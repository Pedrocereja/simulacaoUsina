from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np

# Variáveis a 100%
Tn = 5.71
Th = 0.71
tau = 4.29

# Função tranferência
a = tf(1, [Tn, 0])
b = tf(1, [tau, 1])
c = tf(1, [Th, 1])
Nge = a*b*c
print(Nge)

timeinSeconds = np.linspace(0, 100, 1000)

respostaDegrau, tempo = step(Nge, timeinSeconds)
plt.plot(tempo, respostaDegrau)
plt.savefig("results/respostaDegrau.png")
plt.show()

bode(Nge, Hz=True)
plt.savefig("results/bodePlot.png")
plt.show()

rlocus(Nge)
plt.savefig("results/rootLocus.png")
plt.show()

Ngerealimentado = Nge/(1+Nge)
respostaDegrauRealimentado, tempo = step(Ngerealimentado)
plt.plot(tempo, respostaDegrauRealimentado)
plt.savefig("results/respostaDegrauRealimentado.png")
plt.show()
