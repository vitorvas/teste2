#!/usr/bin/env python3

# Extração de dados milonga para
# entrada do internalField para Q

f = open('saida.dat','r')
dados = f.readlines()

# Lista vazia para saida
Q = []

# loop para iterar por linhas
for line in dados:
    l = line.split()
    Q.append(float(l[3]))

# Remove os zeros da lista
Q[:] = (value for value in Q if value != 0)
print("Tamanho da lista: ", len(Q))

q = open('Qfuel.txt','w')
q.write('internalField\tnonuniform List<scalar>\n')
q.write(str(len(Q))+'\n')
q.write('(\n')
for i in Q:
    q.write(str(i)+'\n')
q.write(');\n')


