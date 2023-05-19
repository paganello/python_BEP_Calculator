
# Dichiarazione var globali
#
costoDipH = 0.0
#
init = 0.0
#
costiSpedizioni_IT = [ 10.29, 11.15, 12.94, 13.12, 14.17 ]
costiSpedizioni_EU = [ 34, 39, 43, 45, 50 ]
#
ORE_IN_UN_ANNO = 259





# input + computazione costi fissi
def inputCostiFissi():
    print()
    print("*------- COSTI FISSI -------*")
    costoCapannone = float(input("Costo capannone annuo: "))
    ammortamentoMacchinario = float(input("Inserisci a quanto ammonta l'ammortamento dei macchinari per l'anno corrente: "))
    costoElettr = float(input("Costo elettricita' per Kw/h: "))
    numeroOreLavoroMac = float(input("Numero di ore al giorno di lavoro macchinario: "))
    altriCostiImm = float(input("Somma degli altri costi annui legeati all'immobile (es. Internet): "))
    nDipendenti = int(input("Numero di lavoratori assunti: "))
    costoDipH = float(input("Costo lavoro diretto per ora: "))
    numeroOreLavoroDir = float(input("Numero di ore al giorno di lavoro diretto: "))

    print()
    CF = costoCapannone + ammortamentoMacchinario + (costoElettr * (numeroOreLavoroMac * ORE_IN_UN_ANNO)) + ((numeroOreLavoroDir * ORE_IN_UN_ANNO) * costoDipH * nDipendenti)  + altriCostiImm
    return CF

# Input dati sui prodotti
nArrProd = int(input("inserisci il numero di prodotti che compongono il mix di produzione: "))
prod = [init, init, init, init, init] * nArrProd 

def inputProdotti():
    i = 0
    while i < nArrProd:

        print("*---------------------------------- " + str(i+1) + " ----------------------------------*")

        costoMagazzino = float(input("Inserisci il costo variabile del magazzino per pacchetto prodotto: "))

        svalutazioneVestiti = float(input("Inserisci a quanto ammonta la svalutazione calcolata del pacchetto: "))

        p = float(input("Inserici il prezzo di vendita del prodotto: "))

        peso = float(input("Inserici peso di spedizione del prodotto: "))

        costoMedioSpedizione = 0.0

        prod[i] = [costoMagazzino, svalutazioneVestiti, p, peso, costoMedioSpedizione]

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


# computazione delle percentuali delle vendite generali per stato + verifica degli insermenti delle percentuali 
percentualeTotPerStato = [init] * 3    #il numero di stati e' 3 e non puo variare

def computeGeneralPercentage():
    i = 0
    tot = 0.0
    while i < 3:
        tot = tot + totVenditePerStato[i]
        i = i + 1
    
    i = 0
    while i < 3:
        percentualeTotPerStato[i] = (totVenditePerStato[i]/tot)*100
        i = i + 1
 
    #i = 0
    #tot = 0.0
    #while i < 3:
    #    tot = tot + percentualeTotPerStato[i]
    #    i = i + 1
    
    #if tot != 100:
    #    print("ATTENZIONE!: Accuratezza pari a " + str(tot) + "% ")
    #    print("Probabilmente i numeri di vendita non sono stati inseriti correttamente, oppure non sono del tutto coerenti.")


# computazione delle percentuali delle vendite dei singoli prodotti per stato
percentualiVenditeProdotti = [init] * nArrProd #array che per ogni posizione contiene la percentuale di vendita di un prodotto (si basa sul n prodotti)

def computeProductPercentage():
    i = 0
    tot1 = 0.0
    while i < 3:
        j = 0
        while j < nArrProd:
            tot1 = tot1 + venditeSingProdPerStato[i][j]
            j = j + 1
        i = i + 1

    j = 0
    tot2 = [init] * nArrProd
    while j < nArrProd:
        i = 0
        while i < 3:
            tot2[j] = tot2[j] + venditeSingProdPerStato[i][j]
            i = i + 1
        j = j + 1

    i = 0
    while i < nArrProd:
        percentualiVenditeProdotti[i] = (tot2[i]/tot1)*100
        print(percentualiVenditeProdotti[i])
        i = i + 1

    print(tot1)
    print(tot2)



# Computo il costo medio di spedizione per ogni prodotto in base al peso e alla percentuale di vendita per stato (media pesata)
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
                if(prod[j][3] <= 3):
                    tmpSpedizioni = costiSpedizioni_IT[0]
                if(prod[j][3] <= 5):
                    tmpSpedizioni = costiSpedizioni_IT[1]
                if(prod[j][3] <= 10):
                    tmpSpedizioni = costiSpedizioni_IT[2]
                if(prod[j][3] <= 20):
                    tmpSpedizioni = costiSpedizioni_IT[3]
                if(prod[j][3] <= 30):
                    tmpSpedizioni = costiSpedizioni_IT[4]                
            else :
                if(prod[j][3] <= 3):
                    tmpSpedizioni = costiSpedizioni_EU[0]
                if(prod[j][3] <= 5):
                    tmpSpedizioni = costiSpedizioni_EU[1]
                if(prod[j][3] <= 10):
                    tmpSpedizioni = costiSpedizioni_EU[2]
                if(prod[j][3] <= 20):
                    tmpSpedizioni = costiSpedizioni_EU[3]
                if(prod[j][3] <= 30):
                    tmpSpedizioni = costiSpedizioni_EU[4]

            prod[j][4] = prod[j][4] + (venditeSingProdPerStato[i][j] * tmpSpedizioni)
            totProdVenduto[j] = totProdVenduto[j] + venditeSingProdPerStato[i][j]
            i = i + 1 

        prod[j][4] = prod[j][4] / totProdVenduto[j]
        j = j + 1


# Computo il numero di vendite sufficinenti per il raggiungimento del BEP se vendessi un prodotto singolo
# prod[i] = [costoLavDiretto, costoMagazzino, svalutazioneVestiti, p, peso, costoMedioSpedizione]
costoMedioSpedizioneNonPesatoPerProdotto = [init] * nArrProd
BEPSingleProd = [init] * nArrProd

def computeSingleProdBEPs():
    i = 0
    while i < nArrProd:
        costoMedioSpedizioneNonPesatoPerProdotto[i] = 0.0
        i = i + 1

    j = 0
    while j < nArrProd:
        i = 0
        while i < 3:
            if i == 0:
                if(prod[j][3] <= 3):
                    tmpSpedizioni = costiSpedizioni_IT[0]
                if(prod[j][3] <= 5):
                    tmpSpedizioni = costiSpedizioni_IT[1]
                if(prod[j][3] <= 10):
                    tmpSpedizioni = costiSpedizioni_IT[2]
                if(prod[j][3] <= 20):
                    tmpSpedizioni = costiSpedizioni_IT[3]
                if(prod[j][3] <= 30):
                    tmpSpedizioni = costiSpedizioni_IT[4]                
            else :
                if(prod[j][3] <= 3):
                    tmpSpedizioni = costiSpedizioni_EU[0]
                if(prod[j][3] <= 5):
                    tmpSpedizioni = costiSpedizioni_EU[1]
                if(prod[j][3] <= 10):
                    tmpSpedizioni = costiSpedizioni_EU[2]
                if(prod[j][3] <= 20):
                    tmpSpedizioni = costiSpedizioni_EU[3]
                if(prod[j][3] <= 30):
                    tmpSpedizioni = costiSpedizioni_EU[4]

            costoMedioSpedizioneNonPesatoPerProdotto[j] = costoMedioSpedizioneNonPesatoPerProdotto[j] + (tmpSpedizioni * (percentualeTotPerStato[i] / 100))
            i = i + 1
        j = j + 1

    i = 0
    while i < nArrProd:
        tmpMdC = 0.0
        tmpMdC = prod[i][2] - (+ prod[i][0] + prod[i][1] + costoMedioSpedizioneNonPesatoPerProdotto[i])
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
def computeMultiProdBEP():
    tmpMdC = [init] * nArrProd
    totTmpMdC = 0.0
    
    i = 0
    while i < nArrProd:
        tmpMdC[i] = prod[i][2] - (prod[i][0] + prod[i][1] + prod[i][4])
        i = i + 1
 
    i = 0
    while i < nArrProd:
        totTmpMdC = totTmpMdC + (tmpMdC[i] * (percentualiVenditeProdotti[i]/100))
        i = i + 1

    BEPMultiProd = CF / totTmpMdC

    return BEPMultiProd
    


# MAIN:
CF = inputCostiFissi()

inputProdotti()
inputVendite()

computeGeneralPercentage()
computeProductPercentage()

computeCostoSpedizioneMedio()
computeSingleProdBEPs()

printSingleProdBEPs()

print()
print("COSTI FISSI: " + str(CF))
print("il Break eaven point multiprodotto e': " + str(computeMultiProdBEP()))



  

