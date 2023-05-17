#init
costiSpedizioni_IT = [ 10.29, 11.15, 12.94, 13.12]
costiSpedizioni_EU = [ 34, 39, 43, 45]
init = 0.0



print("Calcolo Break Eaven Point basandosi sui dati inseriti e le percentuali che compongono il mix di prodotti venduti:")

#input + computazione costi fissi
print("Inserisci di seguito i dati sui costi fissi:")
print()
costoCapannone = float(input("Inserisci costo capannone annuo: "))
costoElettr = float(input("Costo elettricita' annuo: "))
altriCostiImm = float(input("Somma degli altri costi annui legeati all'immobile (es. Internet): "))
costoDipH = float(input("Costo lavoro diretto per ora: "))
numeroOreLavoroComp = float(input("Numero complessivo di lavoro diretto: "))

CF = costoCapannone + costoElettr + altriCostiImm + (costoDipH * numeroOreLavoroComp)

#input prodotti con relativi dati e prezzi
print("inserisci il numero di prodotti che compongono il mix di produzione:")
nArrProd = int(input())

prod = [init, init, init, init] * nArrProd

i = 0
while i < nArrProd:

    print("*---------------------------------- " + str(i+1) + " ----------------------------------*")

    print("inserisci numero minuti di lavoro diretto per la realizzazione del pacchetto " + str(i+1) + ":")
    a_0 = int(input())
    print("inserisci costo lavoro diretto orario del pacchetto:")
    a_1 = costoDipH
    costoLavDiretto = a_1/60*a_0

    print("Inserisci il costo colcolato varibiale per la lavorazione del pacchetto:")
    costoMagazzino = float(input())

    print("Inserisci a quanto ammonta la svalutazione calcolata del pacchetto:")
    svalutazioneVestiti = float(input())

    print("Inserici il prezzo di vendita del prodotto")
    p = float(input())

    #print("Percentuale di vendita del prodotto " + str(i+1) + " in Italia rispetto agli altri prodotti:")
    #mIT = float(input())/100

    #print("Percentuale di vendita del prodotto " + str(i+1) + " in Croazia rispetto agli altri prodotti:")
    #mCR = float(input())/100
    
    #print("Percentuale di vendita del prodotto " + str(i+1) + " in Grecia rispetto agli altri prodotti:")
    #mGR = float(input())/100

    prod[i] = [costoLavDiretto, costoMagazzino, svalutazioneVestiti, p]

    i = i+1
    print()


# inserimento delle percentuali di vendita nei singoli paesi
totVenditePerStato = [init, init, init]
venditeSingProdPerStato = [init, init, init, init] * 3

i = 0
while i < 3:

    if i == 0:
        print("*---------------------------------- ITALIA ----------------------------------*")
    if i == 1:
        print("*---------------------------------- CROAZIA ---------------------------------*")
    if i == 2:
        print("*---------------------------------- GRECIA ----------------------------------*")
    t = int(input("Numero totale di vendite effettuate nel paese in questione: "))
    totVenditePerStato[i] = t

    a = int(input("Numero totale di vendite per prodotto A: "))
    b = int(input("Numero totale di vendite per prodotto B: "))
    c = int(input("Numero totale di vendite per prodotto C: "))
    d = int(input("Numero totale di vendite per prodotto D: "))
    venditeSingProdPerStato[i] = [a, b, c, d]

    i = i+1
    print()



# computazione delle percentuali delle vendite generali per stato + verifica degli insermenti delle percentuali 
i = 0
tot = 0.0
percentualePerStato = [init, init, init]    #il numero di satti e' 3 e non puo variare
tot = totVenditePerStato[0] + totVenditePerStato[1] + totVenditePerStato[2]
while i < 3:
    percentualePerStato[i] = (totVenditePerStato[i]/tot)*100
    i = i + 1
 
i = 0
tot = 0.0
while i < 3:
    pTot = pTot + percentualePerStato[i]
    i = i + 1
if pTot != 100:
    print("ATTENZIONE!: Accuratezza pari al " + str(tot) + "% !")
    print("Probabilmente i numeri di vendita non sono stati inseriti correttamente, oppure non sono del tutto coerenti.")



# computazione delle percentuali delle vendite dei singoli prodotti per stato + verifica degli insermenti delle percentuali
i = 0
tot = 0.0
percentualiVenditeStato[3] = [init] * nArrProd  #array che per ogni posizione contiene la percentuale di vendita di un prodotto (si basa sul n prodotti)

while i < 3:
    tot = venditeSingProdPerStato[i][0] + venditeSingProdPerStato[i][1] + venditeSingProdPerStato[i][2] + venditeSingProdPerStato[i][3]
    i = i + 1
    j = 0
    while j < 3:
        percentualiVenditeSingProdPerStato[i] = [(venditeSingProdPerStato[i][0]/tot)*100, (venditeSingProdPerStato[i][1]/tot)*100, (venditeSingProdPerStato[i][2]/tot)*100, (venditeSingProdPerStato[i][3]/tot)*100]
        j = j + 1

i = 0  
j = 0
while i < 3:
    tot = 0
    while j < 3
        tot = tot + percentualiVenditeSingProdPerStato[j][i]
        j = j + 1
        print(tot)
        
    if tot != 100 :
        print("ATTENZIONE!: Accuratezza pari al " + str(tot) + "% !")
        print("Probabilmente i numeri di vendita non sono stati inseriti correttamente, oppure non sono del tutto coerenti.")
    j = 0    
    i = i + 1


#Computo il costo per medio di spedizione per ogni prodotto
    
    
    
    
    
    
#Computo il numero di vendite sufficinenti per il raggiungimento del BEP se vendessi un prodotto singolo
i = 0
BEPSingleProd[nArrProd]
while < nArrProd:
    BEPSingleProd[i] = 
    

    
i = 0
while i < nArrProd:

    if i == 0:
        costoSpedizione_IT = (prod[i][4] * percentualiDiVenditaPerStato[i][0] * costiSpedizioni_IT[i])
        costoSpedizione_CR = (prod[i][5] * percentualiDiVenditaPerStato[i][0] * costiSpedizioni_EU[i])
        costoSpedizione_GR = (prod[i][6] * percentualiDiVenditaPerStato[i][0] * costiSpedizioni_EU[i])

        

    if i == 1:
        CostoSpedizione_IT = (mixProdotto_A_IT * mixVendita_IT * costiSpedizioni_IT[i])
        CostoSpedizione_CR = (mixProdotto_A_CR * mixVendita_CR * costiSpedizioni_EU[i])
        CostoSpedizione_GR = (mixProdotto_A_GR * mixVendita_GR * costiSpedizioni_EU[i])

    if i == 2:
        CostoSpedizione_IT = (mixProdotto_A_IT * mixVendita_IT * costiSpedizioni_IT[i])
        CostoSpedizione_CR = (mixProdotto_A_CR * mixVendita_CR * costiSpedizioni_EU[i])
        CostoSpedizione_GR = (mixProdotto_A_GR * mixVendita_GR * costiSpedizioni_EU[i])
    
    if i == 3:
        CostoSpedizione_IT = (mixProdotto_A_IT * mixVendita_IT * costiSpedizioni_IT[i])
        CostoSpedizione_CR = (mixProdotto_A_CR * mixVendita_CR * costiSpedizioni_EU[i])
        CostoSpedizione_GR = (mixProdotto_A_GR * mixVendita_GR * costiSpedizioni_EU[i])






  

