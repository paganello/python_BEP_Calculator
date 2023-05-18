
# Dichiarazione var globali
#
costoDipH = 0.0
#
init = 0.0
#
costiSpedizioni_IT = [ 10.29, 11.15, 12.94, 13.12, 14.17 ]
costiSpedizioni_EU = [ 34, 39, 43, 45, 50 ]





# input + computazione costi fissi
def inputCostiFissi():
    print()
    print("Inserisci di seguito i dati sui costi fissi:")
    print()
    costoCapannone = float(input("Inserisci costo capannone annuo: "))
    costoElettr = float(input("Costo elettricita' annuo: "))
    altriCostiImm = float(input("Somma degli altri costi annui legeati all'immobile (es. Internet): "))
    costoDipH = float(input("Costo lavoro diretto per ora: "))
    numeroOreLavoroComp = float(input("Numero complessivo di lavoro diretto: "))

    CF = costoCapannone + costoElettr + altriCostiImm + (costoDipH * numeroOreLavoroComp)
    return CF

# Input dati sui prodotti
nArrProd = int(input("inserisci il numero di prodotti che compongono il mix di produzione: "))
print()
prod = [init, init, init, init, init, init] * nArrProd 

def inputProdotti():
    i = 0
    while i < nArrProd:

        print("*---------------------------------- " + str(i+1) + " ----------------------------------*")

        a_0 = int(input("inserisci numero minuti di lavoro diretto per la realizzazione del pacchetto " + str(i+1) + ": "))
        a_1 = costoDipH
        costoLavDiretto = a_1/60*a_0

        costoMagazzino = float(input("Inserisci il costo variabile del magazzino per pacchetto prodotto: "))

        svalutazioneVestiti = float(input("Inserisci a quanto ammonta la svalutazione calcolata del pacchetto: "))

        p = float(input("Inserici il prezzo di vendita del prodotto: "))

        peso = float(input("Inserici peso di spedizione del prodotto: "))

        costoMedioSpedizione = 0.0

        prod[i] = [costoLavDiretto, costoMagazzino, svalutazioneVestiti, p, peso, costoMedioSpedizione]

        i = i+1
        print()


# Inserimento delle percentuali di vendita nei singoli paesi
totVenditePerStato = [init] * 3
venditeSingProdPerStato = [[0 for _ in range(nArrProd)] for _ in range(3)]

def inputVendite():
    i = 0
    while i < 3:

        if i == 0:
            print("*---------------------------------- ITALIA ----------------------------------*")
        if i == 1:
            print("*---------------------------------- CROAZIA ---------------------------------*")
        if i == 2:
            print("*---------------------------------- GRECIA ----------------------------------*")
        t = float(input("Numero totale di vendite effettuate nel paese in questione: "))
        totVenditePerStato[i] = t
    
        j = 0
        while j < nArrProd:
            data = float(input("Numero totale di vendite per prodotto " + str(j+1) + ": "))
            venditeSingProdPerStato[i][j] = data
            j = j + 1

        i = i+1
        print()

'''
# computazione delle percentuali delle vendite generali per stato + verifica degli insermenti delle percentuali 
i = 0
tot = 0.0
percentualeTotPerStato = [init] * 3    #il numero di stati e' 3 e non puo variare
while i < 3:
    tot = tot + totVenditePerStato[i]
    i = i + 1
    
while i < 3:
    percentualeTotPerStato[i] = (totVenditePerStato[i]/tot)*100
    i = i + 1
 
i = 0
tot = 0.0
while i < 3:
    tot = tot + percentualeTotPerStato[i]
    i = i + 1
    
if tot != 100:
    print("ATTENZIONE!: Accuratezza pari a " + str(tot) + "% ")
    print("Probabilmente i numeri di vendita non sono stati inseriti correttamente, oppure non sono del tutto coerenti.")


# computazione delle percentuali delle vendite dei singoli prodotti per stato + verifica degli insermenti delle percentuali
i = 0
tot = 0.0
percentualiVenditeProdottiPerStato = [[0 for _ in range(nArrProd)] for _ in range(3)] #array che per ogni posizione contiene la percentuale di vendita di un prodotto (si basa sul n prodotti)

while i < 3:
    j = 0
    while j < nArrProd:
        tot = tot + venditeSingProdPerStato[i][j]
        j = j + 1
       
    j = 0
    while j < nArrProd:
        percentualiVenditeProdottiPerStato[i][j] = (venditeSingProdPerStato[i][j]/tot)*100
        j = j + 1
    i = i + 1

i = 0  
while i < 3:
    tot = 0
    j = 0
    while j < nArrProd:
        tot = tot + percentualiVenditeProdottiPerStato[j][i]
        j = j + 1
        print(tot)
    i = i + 1
        
if tot != 100 :
    print("ATTENZIONE!: Accuratezza pari al " + str(tot) + "% per il i prodotti venduti nella nazione " + str(i+1) + ".")
    print("Probabilmente i numeri di vendita non sono stati inseriti correttamente, oppure non sono del tutto coerenti.")  
'''

# Computo il costo per medio di spedizione per ogni prodotto in base al peso
# Ovvero: costoMedioPesatoProd= (%venditeNazione * (%venditeSingProdNazione / 100) * costanteSpedizioneProdotto) + stessa cosa fatta per per le altre nazioni
#
totProdVenduto = [init] * nArrProd

def computeCostoSpedizioneMedio():
    i = 0
    while i < nArrProd:
        totProdVenduto[i] = 0.0
        i = i + 1

    j = 0
    while j < nArrProd:
        i = 0
        while i < 3:
            if i == 0:
                if(prod[j][4] <= 3):
                    tmpSpedizioni = costiSpedizioni_IT[0]
                if(prod[j][4] <= 5):
                    tmpSpedizioni = costiSpedizioni_IT[1]
                if(prod[j][4] <= 10):
                    tmpSpedizioni = costiSpedizioni_IT[2]
                if(prod[j][4] <= 20):
                    tmpSpedizioni = costiSpedizioni_IT[3]
                if(prod[j][4] <= 30):
                    tmpSpedizioni = costiSpedizioni_IT[4]                
            else :
                if(prod[j][4] <= 3):
                    tmpSpedizioni = costiSpedizioni_EU[0]
                if(prod[j][4] <= 5):
                    tmpSpedizioni = costiSpedizioni_EU[1]
                if(prod[j][4] <= 10):
                    tmpSpedizioni = costiSpedizioni_EU[2]
                if(prod[j][4] <= 20):
                    tmpSpedizioni = costiSpedizioni_EU[3]
                if(prod[j][4] <= 30):
                    tmpSpedizioni = costiSpedizioni_EU[4]

            prod[j][5] = prod[j][5] + (venditeSingProdPerStato[i][j] * tmpSpedizioni)
            totProdVenduto[j] = totProdVenduto[j] + venditeSingProdPerStato[i][j]
            print(totProdVenduto[j])
            i = i + 1 

        prod[j][5] = prod[j][5] / totProdVenduto[j]
        j = j + 1


#Computo il numero di vendite sufficinenti per il raggiungimento del BEP se vendessi un prodotto singolo
# prod[i] = [costoLavDiretto, costoMagazzino, svalutazioneVestiti, p, peso, costoMedioSpedizione]
def computeSingleProdBEPs(CF):
    i = 0
    BEPSingleProd = [init] * nArrProd
    while i < nArrProd:
        tmpMdC = 0.0
        tmpMdC = prod[i][3] - (prod[i][0] + prod[i][1] + prod[i][2] + prod[i][5])
        BEPSingleProd[i] = CF / tmpMdC
        i = i + 1

        
# Print i BEP prodotti singoli
#
BEPSingleProd = [init] * nArrProd

def printSingleProdBEPs():
    i = 0
    while i < nArrProd:
        print("Break eaven point del prodotto " + str(i+1) + ": " + str(BEPSingleProd[i]))
        i = i + 1

        
# Computa il BEP multiprodotto
def computeMultiProdBEP(CF):
    i = 0
    BEPMultiProd = init
    BEPMultiProd = CF / (%A * BEPSingleProd[0]) + (%B * BEPSingleProd[1]) + (%C * BEPSingleProd[2]) + (%D * BEPSingleProd[4]) 
    return BEPMultiProd
    


# MAIN:
CF = inputCostiFissi()

inputProdotti()
inputVendite()
computeCostoSpedizioneMedio()
computeSingleProdBEPs(CF)

printSingleProdBEPs()
print("il Break eaven point multiprodotto e': " + str(computeBEPMultiProd(CF)))



  

