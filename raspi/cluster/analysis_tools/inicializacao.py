import matplotlib.pyplot as plt

#Inicialização
i = 0
segundos1 = []
corrente1 = [0.293, 0.294, 0.296, 0.293, 0.292, 0.292, 0.293, 0.293, 0.293, 0.292, 0.292, 
             0.292, 0.292, 0.293, 0.357, 0.331, 0.335, 0.343, 0.347, 0.354, 0.358, 
             0.360, 0.353, 0.369, 0.411, 0.397, 0.378, 0.357, 0.358, 0.358, 0.416, 
             0.404, 0.425, 0.434, 0.423, 0.485, 0.490, 0.472, 0.484, 0.465, 0.514, 
             0.516, 0.513, 0.750, 0.681, 0.713, 0.645, 0.744, 0.682, 0.767, 0.660, 
             0.761, 0.651, 0.763, 0.760, 0.457, 0.455, 0.325, 0.290, 0.293, 0.293, 
             0.288, 0.288, 0.290, 0.290, 0.293, 0.292, 0.288, 0.289, 0.290, 0.289, 
             0.289, 0.289, 0.287, 0.288, 0.290, 0.290, 0.288, 0.288, 0.287, 0.287,
             0.434, 0.543, 0.597, 0.594, 0.698, 0.581, 0.725, 0.762, 0.760, 0.693, 
             0.670, 0.677, 0.557, 0.592, 0.591, 0.598, 0.674, 0.694, 0.565, 0.441, 
             0.677, 0.671, 0.446, 0.372, 0.295, 0.295, 0.294, 0.294, 0.292, 0.292, 
             0.293, 0.293, 0.293, 0.293, 0.291, 0.290, 0.290, 0.293, 0.290, 0.295, 
             0.291, 0.291, 0.292, 0.292, 0.294, 0.294, 0.291, 0.291, 0.292, 0.292, 
             0.292, 0.292, 0.291, 0.291, 0.351, 0.479, 0.445, 0.459, 0.450, 0.392, 
             0.458, 0.451, 0.298, 0.294, 0.337, 0.290, 0.295, 0.294, 0.291, 0.290, 
             0.291, 0.290, 0.292, 0.292, 0.291, 0.290, 0.293, 0.291, 0.292, 0.291]

while(i <= 160):
     segundos1[len(segundos1):] = [i]
     i+= 1

plt.plot(segundos1, corrente1)
xlab = 'Tempo (s)'
ylab = 'Corrente (A)'
title1 = 'Consumo de Corrente na Inicialização'
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title1)