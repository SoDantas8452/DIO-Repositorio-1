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
gama = 3.0 * w0
beta = np.sqrt(gama**2/4.0 - w0**2)
# as raízes
lambda1 = - gama/2.0 - beta
lambda2 = - gama/2.0 + beta
# posição inicial em radianos
teta0 = 0.0 
# v0 é  a velocidade inicial em 1/s
Omega0 = [0.5]
# Tt é  o tempo total de oscilações para fazer o gráfico
Tt = 2.0 * 2.0 * np.pi / w0
# t é  um vetor com npontos valores entre 0.0 e Tt
t = np.arange(0.0, Tt, Tt / float(npontos))
# cria o ambiente para fazer dois gráficos na mesma figura
fig, axs = plt.subplots(2)
fig.suptitle('Amortecimento Forte')
for i in range(len(Omega0)):
# constantes que definem as funções posição e velocidade
    A = (teta0 * lambda2 - Omega0[i]) / (lambda2 - lambda1)
    B = (Omega0[i] - teta0 * lambda1) / (lambda2 - lambda1)
# aqui avalia as posições e velocidades ao longo do tempo
    thetaT = A * np.exp(lambda1 * t) + B * np.exp(lambda2 * t)
    omegaT = A * lambda1 * np.exp(lambda1 * t) + B * lambda2 * np.exp(lambda2 * t)
# cria o gráfico e exibe na tela do computador
    axs[0].plot(t, thetaT)
    axs[1].plot(thetaT, omegaT, '.')
axs[0].set_title(r"$\gamma = 3.0 \omega_0$")
axs[0].set(xlabel='t (s)', ylabel=r"$\theta(t)$")
axs[0].xaxis.set_label_coords(1.02,-0.02)
axs[1].set(xlabel=r"$\theta(t)$", ylabel=r"$\Omega(t)$")
axs[1].grid(True)
plt.show()
