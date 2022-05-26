import matplotlib.pyplot as plt
import scipy.special as spesp
import numpy as np
# g é  a aceleração da gravidade em metros por segundo ao quadrado
g = 9.8
# l é  o comprimento do pêndulo simples em metros
l = 4.9
# w0 é  a frequência de oscilação do pêndulo simples
w0 = np.sqrt(g/l)
# k é  um vetor com valores entre 0.0 e 1.0
k = np.arange(0.0, 1.0, 0.0125)
# T0 é  um vetor de comprimento len(k) armazenando o período para pequenas oscilações
T0 = np.ones(len(k),dtype=float) * 2.0 * np.pi / w0
# Ka armazena o cálculo da integral elíptica completa de primeira espécie para os valores k
Ka = spesp.ellipk(k*k)
# T é  o período de oscilação para cada valor de amplitude inicial
T = 4.0 * Ka / w0
# cria o gráfico e exibe na tela do computador
plt.plot(k, T)
plt.plot(k, T0)
plt.title("Período de oscilação do pêndulo simples")
plt.xlabel(r"Seno do ângulo $\theta_0/2$")
plt.ylabel("T")
plt.show()
