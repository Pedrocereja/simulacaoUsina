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

t = np.linspace(0, 100, 1000)
respostaImpulso, tempo = step(Nge, t)
plt.plot(tempo, respostaImpulso)
plt.show()

bode(Nge, Hz=True)
plt.show()

rlocus(Nge)
plt.show()

Ngerealimentado = Nge/(1+Nge)
r, t = step(Ngerealimentado)
plt.plot(t, r)
plt.show()
