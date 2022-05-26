import matplotlib.pyplot as plt
import scipy.special as spesp
import numpy as np
# npontos é  o número de pontos no gráfico
npontos = 1000
# theta0 é  o ângulo inicial
theta0 = 0.90 * np.pi
# m é  um dos dados iniciais para avaliar a a função elíptica de Jacobi
m = np.sin(theta0/2.0)
# K armazena o cálculo da integral elíptica completa de primeira espécie para os valores m
K = spesp.ellipk(m*m)
# g é  a aceleração da gravidade em metros por segundo ao quadrado
g = 9.8
# l é  o comprimento do pêndulo simples em metros
l = 4.9
# w0 é  a frequência de oscilação do pêndulo simples
w0 = np.sqrt(g/l)
# Tt é  o tempo total de oscilações para fazer o gráfico
Tt = 3.0 * 2.0 * np.pi / w0
# t é  um vetor com npontos valores entre 0.0 e Tt
t = np.arange(0.0, Tt, Tt / float(npontos))
# arg é  um vetor com os argumentos para avaliar em seguida as funções elípticas Jacobianas
arg = K - w0 * t
# aqui avalia as funções elípticas Jacobianas
sn, cn, dn, ph = spesp.ellipj(arg, m*m)
# thetaT é  um vetor de comprimento len(t) armazenando o ângulo como função do tempo
thetaT = 2.0 * np.arcsin(m * sn)
# T é  o período de oscilação para cada valor de amplitude inicial
theta = theta0 * np.cos(w0*t)
# cria o gráfico e exibe na tela do computador
plt.plot(t, thetaT)
plt.plot(t, theta)
plt.title("Variação do ângulo teta em função do tempo")
plt.xlabel("Intevalo de tempo (s)")
plt.ylabel(r"$\theta$(t)")
plt.show()
