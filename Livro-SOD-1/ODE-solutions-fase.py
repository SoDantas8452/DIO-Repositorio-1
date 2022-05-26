# Solução de equações diferenciais ordinárias (EDO) de alta ordem utilizando Runge-Kutta

# y'' = f(t, y, y')
# Criando duas equações diferenciais
# y' = u
# u' = f(t, y, u)

# Lembrar que:
# t[n+1] = t[n] + h
# y[n+1] = y[n] + h * f(x[n], y[n])

# m[1] = u[n]
# k[1] = f(t[n], y[n], u[n])
# m[2] = m[1] + h * k[1] / 2.0
# k[2] = f(t[n] + h / 2.0, y[n] + h * m[1] / 2.0, m[1] + h * k[1] / 2.0)
# m[3] = m[1] + h * k[2] / 2.0
# k[3] = f(t[n] + h / 2.0, y[n] + h * m[2] / 2.0, m[1] + h * k[2] / 2.0)
# m[4] = m[1] + h * k[3]
# k[4] = f(t[n] + h, y[n] + h * m[3], m[1] + h * k[3])

# y[n] = y[n] + h * (m[1] + 2.0 * m[2] + 2.0 * m[3] + m[4])  6.0
# u[n] = u[n] + h * (k[1] + 2.0 * k[2] + 2.0 * k[3] + k[4]) / 6.0

# Como exemplo vamos ressolver a equação do pêndulo simples amortecido:
# y'' + b * y' / m + g * sin(y) / l = 0
# com: | m = massa pendurada na ponta do pêndulo em (kg)
#      | g = aceleração da gravidade local em (m/s^2)
#      | l = comprimiento do pêndulo em (m)
#      | b = constante de amortecimento em (kg/s)

# y'' = - b * y' / m - g * sin(y) / l ou f(t, y, y')
# u'  = - b * u / m - g * sin(y) / l ou f(t, y, u)

import matplotlib.pyplot as plt
import numpy as np

# As constantes são:
g = 9.8           # aceleração da gravidade local em (m/s^2)
l = 4.9           # comprimento do pêndulo em (m)
b = [0.05]  # constantes de amortecimento em (kg/s)
m = 0.100         # massa endurada na ponta do pênculo em (kg)

# cria o ambiente para fazer dois gráficos na mesma figura
fig, axs = plt.subplots(2)
fig.suptitle('Caso geral')

for i in range(len(b)):
    # as condições iniciais são:
    t = 0.0    # instante inicial
    tf = 30.0  # instante final de integração da EDO
    h = 0.05   # incrementodo tempo ao longo da integração da EDO
    y = 0.0    # posição inicial (radianos)
    u = 2.0    # velocidade inicial (radianos/s)
    
    # Armazena resultados para fazer gráficos:
    tx = []       # tempo (instantes)
    tx.append(t)
    theta = []    # posições angulares (radianos)
    theta.append(y)
    omega = []    # velocidades angulares (radianos/)
    omega.append(u)
    
    # Integra a EDO ao longo do tempo:
    while t < tf:
          m1 = u
          k1 = - b[i] * u / m - g * np.sin(y) / l
          m2 = m1 * h * k1 / 2.0
          t_2 = t + h / 2.0
          y_2 = y + h * m1 / 2.0
          u_2 = m2
          k2 = - b[i] * u_2 / m - g * np.sin(y_2) / l
          m3 = m1 + h * k2 / 2.0
          t_3 = t + h / 2.0
          y_3 = y + h * m2 / 2.0
          u_3 = m3
          k3 = - b[i] * u_3 / m - g * np.sin(y_3) / l
          m4 = m1 + h * k3
          t_4 = t + h
          y_4 = y + h * m3
          u_4 = m4
          k4 = - b[i] * u_4 / m - g * np.sin(y_4) / l
          t = t + h
          y = y + h * (m1 + (2.0 * m2) + (2.0 * m3) + m4) / 6.0
          u = u + h * (k1 + (2.0 * k2) + (2.0 * k3) + k4) / 6.0
          tx.append(t)
          theta.append(y)
          omega.append(u)

    # adiciona as curvas no gráfico
    axs[0].plot(tx, theta)
    axs[1].plot(theta, omega, '.')

axs[0].set_title(r"$g=9.8(m/s^2), l=4.9(m) \, \,  e \, \, m=0.100(kg)$")
axs[0].set(xlabel='t (s)', ylabel=r"$\theta(t)$")
axs[0].xaxis.set_label_coords(1.02,-0.02)
axs[1].set(xlabel=r"$\theta(t)$", ylabel=r"$\Omega(t)$")
axs[0].grid(True)
axs[1].grid(True)
plt.show()
