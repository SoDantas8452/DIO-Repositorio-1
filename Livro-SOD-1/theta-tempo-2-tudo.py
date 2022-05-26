import matplotlib.pyplot as plt
import scipy.special as spesp
import numpy as np
# npontos é  o número de pontos no gráfico
npontos = 1000
# g é  a aceleração da gravidade em metros por segundo ao quadrado
g = 9.8
# l é  o comprimento do pêndulo simples em metros
l = 4.9
# w0 é  a frequência de oscilação do pêndulo simples
w0 = np.sqrt(g/l)
# v0 é  a velocidade inicial em m/s
v0 = [1.0*w0*l/(2.0*w0*l), 1.5*w0*l/(2.0*w0*l), 1.9*w0*l/(2.0*w0*l), 1.999*w0*l/(2.0*w0*l)]
# determina o valor theta_max por conservação de energia
theta_max = np.arcsin(v0)
# m é  um dos dados iniciais para avaliar a a função elíptica de Jacobi
m = np.sin(theta_max)
# Tt é  o tempo total de oscilações para fazer o gráfico
Tt = 6.0 * 2.0 * np.pi / w0
# t é  um vetor com npontos valores entre 0.0 e Tt
t = np.arange(0.0, Tt, Tt / float(npontos))
# arg é  um vetor com os argumentos para avaliar em seguida as funções elípticas Jacobianas
arg = w0 * t
for i in range(len(v0)):
# aqui avalia as funções elípticas Jacobianas
    sn, cn, dn, ph = spesp.ellipj(arg, m[i]*m[i])
# thetaT é  um vetor de comprimento len(t) armazenando o ângulo como função do tempo
    thetaT = 2.0 * np.arcsin(m[i] * sn)
# cria o gráfico e exibe na tela do computador
    plt.plot(t, thetaT)
plt.title("Variação do ângulo teta em função do tempo")
plt.xlabel("Intevalo de tempo (s)")
plt.ylabel(r"$\theta$(t)")
plt.show()
