print("calcolo BEQ basandosi sui dati inseriti e le percentuali che compongono il mix di prodotti vendut:")

#input + computazione costi fissi
print("Inserisci di seguito i dati sui costi fissi:")
print()
costoCapannone = float(input("inserisci costo capannone annuo: "))
costoElettr = float(input("Costo elettricita' annuo: "))
costoInternet = float(input("altri costi annui: "))
costoDipH = float(input("Costo lavoro diretto orario: "))
numeroOreLavoroComp = float(input("Numero complessive di lavoro diretto: "))

CF = costoCapannone + costoElettr + costoInternet + (costoDipH * numeroOreLavoroComp)

#input prodotti con relativi dati e prezzi
print("inserisci il numero di prodotti che compongono il mix di produzione:")
nArrProd = int(input())

costoLavDiretto = 0.0
costoMagazzino = 0.0
svalutazioneVestiti = 0.0
p = 0.0 
mIT = 0.0
mCR = 0.0
mGR = 0.0

prod = [costoLavDiretto, costoMagazzino, svalutazioneVestiti, p, mIT, mCR, mGR] * nArrProd

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

    print("Percentuale di vendita del prodotto in Italia:")
    mIT = float(input())/100

    print("Percentuale di vendita del prodotto in Croazia:")
    mCR = float(input())/100
    
    print("Percentuale di vendita del prodotto in Grecia:")
    mGR = float(input())/100

    prod[i] = [costoLavDiretto, costoMagazzino, svalutazioneVestiti, p, mIT, mCR, mGR]

    i = i+1
    print()

#costi di spedizione che consideriamo costanti
costiSpedizioni_IT = [ 10.29, 11.15, 12.94, 13.12]
costiSpedizioni_EU = [ 34, 39, 43, 45]

i = 0
while i < nArrProd:

    if i == 0:
        costoSpedizione_IT = (prod[i][4] * 40 * costiSpedizioni_IT[i])
        costoSpedizione_CR = (prod[i][5] * 25 * costiSpedizioni_EU[i])
        costoSpedizione_GR = (prod[i][6] * 35 * costiSpedizioni_EU[i])

        

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






  

