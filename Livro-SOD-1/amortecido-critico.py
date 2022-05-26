import matplotlib.pyplot as plt
import numpy as np
# npontos é  o número de pontos no gráfico
npontos = 1000
# g é  a aceleração da gravidade em metros por segundo ao quadrado
g = 9.8
# l é  o comprimento do pêndulo simples em metros
l = 4.9
# w0 é  a frequência de oscilação do pêndulo simples
w0 = np.sqrt(g/l)
# valor de gama tem que ser maior que 2*w0 para ser amortecimento forte
gama = 2.0 * w0
# a raíz
lambda1 = - gama / 2.0
# posição inicial em radianos
teta0 = 0.1 
# v0 é  a velocidade inicial em 1/s
Omega0 = [0.0,0.5,-0.5]
# Tt é  o tempo total de oscilações para fazer o gráfico
Tt = 2.0 * 2.0 * np.pi / w0
# t é  um vetor com npontos valores entre 0.0 e Tt
t = np.arange(0.0, Tt, Tt / float(npontos))
# cria o ambiente para fazer dois gráficos na mesma figura
fig, axs = plt.subplots(2)
fig.suptitle('Amortecimento Crítico')
for i in range(len(Omega0)):
# constantes que definem as funções posição e velocidade
    A = teta0
    B = Omega0[i] - teta0 * lambda1
    C = A * lambda1 + B
    D = B * lambda1
# aqui avalia as posições e velocidades ao longo do tempo
    thetaT = np.exp(lambda1 * t) * (A + B * t)
    omegaT = np.exp(lambda1 * t) * (C + D * t)
# cria o gráfico e exibe na tela do computador
    axs[0].plot(t, thetaT)
    axs[1].plot(t, omegaT)
axs[0].set_title(r"$\gamma = 2.0 \omega_0$")
axs[0].set(ylabel=r"$\theta$(t)")
axs[1].set(xlabel='Intervalo de tempo (s)', ylabel=r"$\Omega$(t)")
plt.show()
