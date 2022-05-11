## Matheus Rique 
## Buscador de hotel barato 

# Importando bibliotecas 

from datetime import date

#Definições

# hotel = [classificação, tx_semana_padrao, tx_semana_prime,tx_fds_padrao, tx_fds_prime ]
Lakewood = [3, 110,  80, 90, 80]
Bridewood = [4, 160, 110, 60, 50]
Ridgewood = [5, 220, 100, 150, 40]    
d1 = d2 = d3 = d4 = d5 = d6 = 0
repeticao = True 


# Funções 


def periodo (d1 , d2):
    print ("Informe a data (dd/mm/aaaa)")
    entrada = input()
    dia = entrada.split("/")
    dd = int ( dia[0])
    mm = int (dia [1] )
    aaaa = int (dia [2] )
    d0=  date(aaaa, mm, dd).isoweekday()
    
    if (d0>5):
        d2+=1
        
    else:
        d1+=1
        
    return d1 , d2
    
    
def localiza(n, d1 , d2 , d3 , d4, d5, d6):
    
    valor_L = d1*Lakewood[n+1] + d2*Lakewood[n+3] + d3*Lakewood[n+1] + d4*Lakewood[n+3] + d5*Lakewood[n+1] + d6*Lakewood[n+3]
    valor_B = d1*Bridewood[n+1] + d2*Bridewood[n+3] + d3*Bridewood[n+1] + d4*Bridewood[n+3] + d5*Bridewood[n+1] + d6*Bridewood[n+3]
    valor_R = d1*Ridgewood[n+1] + d2*Ridgewood[n+3] + d3*Ridgewood[n+1] + d4*Ridgewood[n+3] + d5*Ridgewood[n+1] + d6*Ridgewood[n+3]
    menor = min(valor_L , valor_B , valor_R)
    
    
    if ( (valor_L != valor_B) & (valor_B != valor_R) & (valor_L != valor_R)):
        if (menor == valor_L):
            print("lakewood")
        elif(menor == valor_B):
            print("Bridgewood")
        else: 
            print("Ridgewood")
    else:
        if (menor == valor_R):
            print("Ridgewood")
        else: 
            print("lakewood")
        
        
#Menu principal

while repeticao == True :
    
# Categoria do cliente 
    print ("Olá, bem vindo ao nosso hotel \n ")
    print (" Porfavor informe sua categoria  \n")

    categoria =  input()

#Menu
    
    if (categoria == 'Regular'):
        categoria=0
        d1 , d2 = periodo(d1, d2)
        d3 , d4 = periodo(d3, d4)
        d5 , d6 = periodo(d5, d6)
        print ("O melhor hotel é ")
        localiza(categoria, d1 , d2 , d3 , d4, d5, d6)
        repeticao = False
        
    
    elif (categoria == 'Reward'):
        categoria=1
        d1 , d2 = periodo(d1 , d2)
        d3 , d4 = periodo(d3, d4)
        d5 , d6 = periodo(d5, d6)
        print ("O melhor hotel é ")
        localiza(categoria, d1 , d2 , d3 , d4, d5, d6)
        repeticao = False
        
    else :
        print ("categoria não encontrada")


