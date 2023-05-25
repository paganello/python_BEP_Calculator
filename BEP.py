import numpy as np
from scipy.optimize import linprog
# Dichiarazione var globali
#
costoDipH = 0.0
#
init = 0.0
#
costiSpedizioni_IT = [10.29, 11.15, 12.94, 13.12, 14.17]
costiSpedizioni_EU = [34, 39, 43, 45, 50]
#
GIORNI_IN_UN_ANNO = 259






# input + computazione costi fissi
#print()
#print("*------- COSTI FISSI -------*")
#costoCapannone = float(input("Costo capannone annuo: "))
#ammortamentoMacchinario = float(input("Inserisci a quanto ammonta l'ammortamento dei macchinari per l'anno corrente: "))
#costoElettr = float(input("Costo elettricita' per Kw/h: "))
#enerMagazzino = float(input("Energia consumata in Kw/h al netto dei macchinari: "))
#numeroOreLavoroMac = float(input("Numero di ore per giorno di lavoro: "))
#altriCostiImm = float(input("Somma degli altri costi annui legeati all'immobile (es. Internet): "))
#nDipendenti = int(input("Numero di lavoratori assunti: "))
#costoDipH = float(input("Costo lavoro diretto per ora: "))
#numeroOreLavoroDir = float(input("Numero di ore al giorno di lavoro diretto: "))

#print()
#CF = costoCapannone + ammortamentoMacchinario + (costoElettr * (enerMagazzino * numeroOreLavoroMac * GIORNI_IN_UN_ANNO)) + ((numeroOreLavoroDir * GIORNI_IN_UN_ANNO) * costoDipH * nDipendenti)  + altriCostiImm
CF = 662780
numeroOreLavoroMac = 8


# Input dati sui prodotti
#nArrProd = int(input("inserisci il numero di prodotti che compongono il mix di produzione: "))
nArrProd = 4
prod = [[0 for _ in range(6)] for _ in range(nArrProd)]


prod[0] = [30, 5, 13.333333, 110, 3, 0.0]
prod[1] = [35, 7, 17.333333, 120, 5, 0.0]
prod[2] = [50, 10, 22.666667, 160, 10, 0.0]
prod[3] = [75, 10, 29.333333, 210, 20, 0.0]
#def inputProdotti():
#    i = 0
#    while i < nArrProd:
#
#        print("*---------------------------------- " + str(i+1) + " ----------------------------------*")
#
#        minutiRealizzazione = float(input("Inserici in numero di minuti necessari per la realizzazione del prodotto: "))
#
#        peso = float(input("Inserici peso di spedizione del prodotto: "))
#
#        costoMagazzino = float(input("Inserisci il costo variabile del magazzino per pacchetto prodotto: "))
#
#        svalutazioneVestiti = float(input("Inserisci a quanto ammonta la svalutazione calcolata del pacchetto: "))

#        p = float(input("Inserici il prezzo di vendita del prodotto: "))

#        costoMedioSpedizione = 0.0

#        prod[i] = [minutiRealizzazione, costoMagazzino, svalutazioneVestiti, p, peso, costoMedioSpedizione]

#        i = i+1
#        print()


# Inserimento delle percentuali di vendita nei singoli paesi
totVenditePerStato = [init] * 3
venditeSingProdPerStato = [[0 for _ in range(nArrProd)] for _ in range(3)]

totVenditePerStato[0] = 40
totVenditePerStato[1] = 25
totVenditePerStato[2] = 35

venditeSingProdPerStato[0]= [16, 8, 4, 12]
venditeSingProdPerStato[1]= [12.5, 7.5, 1.25, 3.75]
venditeSingProdPerStato[2]= [21, 5.25, 1.75, 7]



#def inputVendite():
#    i = 0
#    while i < 3:

#        if i == 0:
#            print("*---------------------------------- ITALIA ----------------------------------*")
#        if i == 1:
#            print("*---------------------------------- CROAZIA ---------------------------------*")
#        if i == 2:
#            print("*---------------------------------- GRECIA ----------------------------------*")
#        t = float(input("Numero totale di vendite effettuate nel paese in questione: "))
#        totVenditePerStato[i] = t
    
#        j = 0
#        while j < nArrProd:
#            data = float(input("Numero totale di vendite per prodotto " + str(j+1) + ": "))
#            venditeSingProdPerStato[i][j] = data
#            j = j + 1

#        i = i+1
#        print()


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
        i = i + 1



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
                if(prod[j][4] <= 3):
                    tmpSpedizioni = costiSpedizioni_IT[0]
                elif(prod[j][4] <= 5):
                    tmpSpedizioni = costiSpedizioni_IT[1]
                elif(prod[j][4] <= 10):
                    tmpSpedizioni = costiSpedizioni_IT[2]
                elif(prod[j][4] <= 20):
                    tmpSpedizioni = costiSpedizioni_IT[3]
                elif(prod[j][4] <= 30):
                    tmpSpedizioni = costiSpedizioni_IT[4]                
            else :
                if(prod[j][4] <= 3):
                    tmpSpedizioni = costiSpedizioni_EU[0]
                elif(prod[j][4] <= 5):
                    tmpSpedizioni = costiSpedizioni_EU[1]
                elif(prod[j][4] <= 10):
                    tmpSpedizioni = costiSpedizioni_EU[2]
                elif(prod[j][4] <= 20):
                    tmpSpedizioni = costiSpedizioni_EU[3]
                elif(prod[j][4] <= 30):
                    tmpSpedizioni = costiSpedizioni_EU[4]

            prod[j][5] = prod[j][5] + (venditeSingProdPerStato[i][j] * tmpSpedizioni)
            #print(prod[j][5])
            #print(venditeSingProdPerStato[i][j])
            #print(tmpSpedizioni)
            totProdVenduto[j] = totProdVenduto[j] + venditeSingProdPerStato[i][j]
            #print("costo medio sped parz: " + str(prod[j][5]))
            #print("vendidte sing prod per stato: " + str(venditeSingProdPerStato[i][j]))
            #print("costo spedizione spedizione: " + str(tmpSpedizioni))
            #print("tot prod venduto: " + str(totProdVenduto[j]))
            i = i + 1 

        prod[j][5] = prod[j][5] / totProdVenduto[j]

        #print("final: " + str(prod[j][5]))
        j = j + 1


# Computo il numero di vendite sufficinenti per il raggiungimento del BEP se vendessi un prodotto singolo
# prod[i] = [costoLavDiretto, costoMagazzino, svalutazioneVestiti, p, peso, costoMedioSpedizione]
#costoMedioSpedizioneNonPesatoPerProdotto = [init] * nArrProd
BEPSingleProd = [init] * nArrProd
MdC = [init] * nArrProd

def computeSingleProdBEPs():
    #i = 0
    #while i < nArrProd:
    #    costoMedioSpedizioneNonPesatoPerProdotto[i] = 0.0
    #    MdC[i] = 0.0
    #    i = i + 1

    #j = 0
    #while j < nArrProd:
    #    i = 0
    #    while i < 3:
    #        if i == 0:
    #            if(prod[j][4] <= 3):
    #                tmpSpedizioni = costiSpedizioni_IT[0]
    #            if(prod[j][4] <= 5):
    #                tmpSpedizioni = costiSpedizioni_IT[1]
    #            if(prod[j][4] <= 10):
    #                tmpSpedizioni = costiSpedizioni_IT[2]
    #            if(prod[j][4] <= 20):
    #                tmpSpedizioni = costiSpedizioni_IT[3]
    #            if(prod[j][4] <= 30):
    #                tmpSpedizioni = costiSpedizioni_IT[4]                
    #        else :
    #            if(prod[j][4] <= 3):
    #                tmpSpedizioni = costiSpedizioni_EU[0]
    #            if(prod[j][4] <= 5):
    #                tmpSpedizioni = costiSpedizioni_EU[1]
    #            if(prod[j][4] <= 10):
    #                tmpSpedizioni = costiSpedizioni_EU[2]
    #            if(prod[j][4] <= 20):
    #                tmpSpedizioni = costiSpedizioni_EU[3]
    #            if(prod[j][4] <= 30):
    #                tmpSpedizioni = costiSpedizioni_EU[4]

    #        costoMedioSpedizioneNonPesatoPerProdotto[j] = costoMedioSpedizioneNonPesatoPerProdotto[j] + (tmpSpedizioni * (percentualeTotPerStato[i] / 100))
    #        i = i + 1
    #    j = j + 1

    i = 0
    while i < nArrProd:
        MdC[i] = prod[i][3] - ( prod[i][1] + prod[i][2] + prod[i][5])
        BEPSingleProd[i] = CF / MdC[i]
        i = i + 1


# Computa il BEP multiprodotto
def computeMultiProdBEP():
    tmpMdC = [init] * nArrProd
    totTmpMdC = 0.0
    
    i = 0
    while i < nArrProd:
        tmpMdC[i] = prod[i][3] - (prod[i][1] + prod[i][2] + prod[i][5])
        i = i + 1

    i = 0
    while i < nArrProd:
        totTmpMdC = totTmpMdC + (tmpMdC[i] * (percentualiVenditeProdotti[i]/100))
        i = i + 1

    BEPMultiProd = CF / totTmpMdC

    return BEPMultiProd
    


def MixOttimo():
    c = [-65.34, -67.81, -96.20, -138.42]
    A = [[30, 35, 50, 75]]
    b = [497280]

    opt = linprog(c, A_ub=A, b_ub=b, method='highs')
    
    print("\n*--------- Analisi di Mix Ottimale ---------*")
    print("Mix per la massimizzazione del profitto: ")
    print("1: " + str(opt.lower.residual[0]))
    print("2: " + str(opt.lower.residual[1]))
    print("3: " + str(opt.lower.residual[2]))
    print("4: " + str(opt.lower.residual[3]))
    print()

# Compute mix ottimo
maxProduzioneProdotti = [init] * nArrProd
ricavoSingeProd = [init] * nArrProd

def computeMixOttimo():

    i = 0
    while i < nArrProd:
        maxProduzioneProdotti[i] = ((GIORNI_IN_UN_ANNO * numeroOreLavoroMac * 60) / prod[i][0]) * 4     #abbaimo 4 macchinari
        #print("max prod: " + str(maxProduzioneProdotti[i]))
        i = i + 1

    tmpRicavoSingeProd = [init] * nArrProd
    i = 0
    while i < nArrProd:
        tmpRicavoSingeProd[i] = ((percentualiVenditeProdotti[i] / 100) * maxProduzioneProdotti[i]) * MdC[i]
        #print("tmpRic: " + str(tmpRicavoSingeProd[i]))
        i = i + 1

    i = 0
    ricavoMixVendita = 0.0
    while i < nArrProd:
        ricavoMixVendita = ricavoMixVendita + tmpRicavoSingeProd[i]
        #print("ricavoMixVendita: " + str(ricavoMixVendita))
        i = i + 1

    i = 0
    while i < nArrProd:
        ricavoSingeProd[i] = maxProduzioneProdotti[i] * MdC[i]
        #print("ricSingProd: " + str(ricavoSingeProd[i]))
        i = i + 1

    return ricavoMixVendita





# Stampa risultati
def printStatistics():
    print("*------------------- STATISTICHE -------------------*\n")
    
    print("Totale costi fissi: " + str(CF) + "\n")

    print("*------- Dati Di Vendita -------*")

    print("Percentuale di vendite in Italia sul totale: " +  str(percentualeTotPerStato[0]))
    print("Percentuale di vendite in Croazia sul totale: " +  str(percentualeTotPerStato[1]))
    print("Percentuale di vendite in Grecia sul totale: " +  str(percentualeTotPerStato[2]) + "\n")

    i = 0
    while i < nArrProd:
        print("Vendite del prodotto " + str(i+1) +" sul totale: " +  str(percentualiVenditeProdotti[i]))
        i = i+1  
    print()

    i = 0
    while i < nArrProd:
        print("Costo di spedizione pesato del prodotto " + str(i+1) +" : " +  str(prod[i][5]))
        i = i+1  
    print()

    i = 0
    while i < nArrProd:
        print("Margine di contribuzione del prodotto " + str(i+1) +" : " +  str(MdC[i]))
        i = i+1
        
    print("\nMON basato sulle percentuali di vendita calcolate sui dati inseriti: " + str(r - CF))


    print("\n*--------- Break Eaven Points ---------*")
    i = 0
    while i < nArrProd:
        print("BEP prodotto "+ str(i+1) +": " + str(BEPSingleProd[i]))
        i = i+1
    print("BEP multiprodotto: " + str(computeMultiProdBEP()))

    MixOttimo()
    i = 0
    while i < nArrProd:
        print("Produzione di solo prodotto "+ str(i+1) +" => MON: " + str(ricavoSingeProd[i] - CF))
        i = i+1
    print()





# MAIN:

#inputProdotti()
#inputVendite()

computeGeneralPercentage()
computeProductPercentage()

computeCostoSpedizioneMedio()
computeSingleProdBEPs()
r = computeMixOttimo()

printStatistics()

  

