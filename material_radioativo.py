#Lê a massa inicial em gramas do material radioativo
massa_inicial = float(input())

#Tempo para massa cair pela metade
tempo_meia_vida_seg = 50

#Define a massa final desejada em gramas
massa_final = 0.5

#Variável para rastrear a massa atual
massa_atual = massa_inicial

#Variável para aacumular o tempo total
tempo_total_seg = 0

#Se a massa inicial já for menor que a final, o tempo é zero
if massa_inicial < massa_final:
    tempo_total_seg = 0
else:
    #Loop para calcular o tempo até a massa ser menor que 0.5
    while massa_atual >= massa_final:
        massa_atual /= 2 #Reduz a massa pela metade
        tempo_total_seg += tempo_meia_vida_seg #Adiciona o tempo de meia vida

# Converte o tempo total de segundos para horas, minutos e segundos.
horas = tempo_total_seg // 3600
minutos = (tempo_total_seg % 3600) // 60
segundos = tempo_total_seg % 60

#Imprimi resultado final
print(f'{int(horas)}h {int(minutos)}m {int(segundos)}s')

