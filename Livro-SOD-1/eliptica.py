import matplotlib.pyplot as plt
import scipy.special as spesp
import numpy as np
# k é   um vetor com valores entre 0.0 e 1.0 com incremento 0.0125
k = np.arange(0.0, 1.0, 0.0125)
# Ka armazena o cálculo da integral elíptica completa de primeira espécie para os valores de k
Ka = spesp.ellipk(k*k)
# cria o gráfico e exibe na tela do computador
plt.plot(k, Ka)
plt.title("Integral elíptica completa de primeira espécie")
plt.xlabel("k")
plt.ylabel("K(k)")
plt.show()
