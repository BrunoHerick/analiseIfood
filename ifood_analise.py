# coding: utf-8
import pandas as pd
import matplotlib.pyplot as grafico
import numpy as np

dados = pd.read_csv("/home/brunohelghast/PROFISSIONAL/PYTHON/SCIKIT_LEARN/marketingAnalytics/ifood_df.csv")
#dados = dados[dados["NumCatalogPurchases"] < 15]
matris_correlacao = dados.corr()

""" print(matris_correlacao["education_PhD"].sort_values(ascending=False))
educacaoMedio = dados.iloc[:,[0,31]]
educacaoMedio = educacaoMedio[educacaoMedio["education_2n Cycle"] == 1]
educacaoBasica = dados.iloc[:,[0,32]]
educacaoBasica = educacaoBasica[educacaoBasica["education_Basic"] == 1]
educacaoGraduacao = dados.iloc[:,[0,33]]
educacaoGraduacao = educacaoGraduacao[educacaoGraduacao["education_Graduation"] == 1]
educacaoMaster = dados.iloc[:,[0,34]]
educacaoMaster = educacaoMaster[educacaoMaster["education_Master"] == 1]
educacaoPhd = dados.iloc[:,[0,35]]
educacaoPhd = educacaoPhd[educacaoPhd["education_PhD"] == 1]
print(dados["Income"].describe())
print(educacaoMedio["Income"].describe())
print(educacaoBasica["Income"].describe())
print(educacaoGraduacao["Income"].describe())
print(educacaoMaster["Income"].describe())
print(educacaoPhd["Income"].describe()) """

""" campanha0e1 = dados.iloc[:,[4,38]]
campanha0e1 = campanha0e1[campanha0e1["AcceptedCmpOverall"] == 0]
print(len(campanha0e1)/(len(dados)*1.0))
print(matris_correlacao["AcceptedCmpOverall"].sort_values(ascending=False))
grafico.scatter(dados["AcceptedCmpOverall"],dados["MntWines"])
grafico.xlabel("AcceptedCmpOverall")
grafico.grid()
grafico.show() """

""" print(matris_correlacao["Age"].sort_values(ascending=False))
grafico.scatter(dados["Age"],dados["Kidhome"])
grafico.xlabel("Age")
grafico.grid()
kidsMediaAge = dados.iloc[:,[1,24]]
kidsMediaAge = kidsMediaAge[kidsMediaAge["Kidhome"] > 0]
print(kidsMediaAge["Age"].describe()) """

""" print(matris_correlacao["NumWebVisitsMonth"].sort_values(ascending=False))
grafico.scatter(dados["NumWebVisitsMonth"],dados["Income"])
grafico.xlabel("NumWebVisitsMonth")
grafico.grid()
grafico.show() """

""" print(matris_correlacao["NumCatalogPurchases"].sort_values(ascending=False))
crianca = dados.iloc[:,[1,12]]
tem0crianca = crianca[crianca["Kidhome"] == 0]
tem1crianca = crianca[crianca["Kidhome"] == 1]
tem2crianca = crianca[crianca["Kidhome"] == 2]
tem0crianca = tem1crianca.sample(46)
tem1crianca = tem2crianca.sample(46)
media0KidNumCatalogPurchases = np.mean(tem0crianca["NumCatalogPurchases"])
media1KidNumCatalogPurchases = np.mean(tem1crianca["NumCatalogPurchases"])
media2KidNumCatalogPurchases = np.mean(tem2crianca["NumCatalogPurchases"])
varianciaDasMediasNumCatalogPurchases = np.var([media0KidNumCatalogPurchases,media1KidNumCatalogPurchases,media2KidNumCatalogPurchases])
vari0KidNumCatalogPurchases = np.var(tem0crianca["NumCatalogPurchases"])
vari1KidNumCatalogPurchases = np.var(tem1crianca["NumCatalogPurchases"])
vari2KidNumCatalogPurchases = np.var(tem2crianca["NumCatalogPurchases"])
mediaDasVarianciasNumCatalogPurchases= np.mean([vari0KidNumCatalogPurchases,vari1KidNumCatalogPurchases,vari2KidNumCatalogPurchases])
varianciaEntreMediasNumCatalogPurchases = (varianciaDasMediasNumCatalogPurchases*46)/mediaDasVarianciasNumCatalogPurchases
razaoF_total = varianciaEntreMediasNumCatalogPurchases/mediaDasVarianciasNumCatalogPurchases
#F = 3.063 para 46      F = 3.354 para 10
print(razaoF_total)
grafico.scatter(dados["NumCatalogPurchases"],dados["Kidhome"])
grafico.xlabel("NumCatalogPurchases")
grafico.grid()
grafico.show() """

""" print(matris_correlacao["MntWines"].sort_values(ascending=False))
grafico.scatter(dados["MntWines"],dados["MntRegularProds"])
grafico.xlabel("MntWines")
grafico.grid()
grafico.show() """

""" print(matris_correlacao["MntTotal"].sort_values(ascending=False))
grafico.scatter(dados["MntTotal"],dados["Income"])
grafico.xlabel("MntTotal")
grafico.grid()
grafico.show() """

""" print(matris_correlacao["MntFishProducts"].sort_values(ascending=False))
grafico.scatter(dados["MntFishProducts"],dados["Income"])
grafico.xlabel("MntFishProducts")
grafico.grid()
grafico.show() """

""" print(matris_correlacao["MntMeatProducts"].sort_values(ascending=False))
dados = dados[dados["MntMeatProducts"] <= 1000]
grafico.subplot(2,1,1)
grafico.scatter(dados["MntMeatProducts"],dados["NumCatalogPurchases"])
grafico.xlabel("MntMeatProducts")
grafico.grid()
grafico.subplot(2,1,2)
grafico.scatter(dados["MntMeatProducts"],dados["NumStorePurchases"])
grafico.xlabel("MntMeatProducts")
grafico.grid()
grafico.show() """

""" print(matris_correlacao["MntWines"].sort_values(ascending=False))
crianca = dados.iloc[:,[1,4]]
tem0crianca = crianca[crianca["Kidhome"] == 0]
tem1crianca = crianca[crianca["Kidhome"] == 1]
tem2crianca = crianca[crianca["Kidhome"] == 2]
tem0crianca = tem1crianca.sample(46)
tem1crianca = tem2crianca.sample(46)
media0KidMntWines = np.mean(tem0crianca["MntWines"])
media1KidMntWines = np.mean(tem1crianca["MntWines"])
media2KidMntWines = np.mean(tem2crianca["MntWines"])
varianciaDasMediasMntWines = np.var([media0KidMntWines,media1KidMntWines,media2KidMntWines])
vari0KidMntWines = np.var(tem0crianca["MntWines"])
vari1KidMntWines = np.var(tem1crianca["MntWines"])
vari2KidMntWines = np.var(tem2crianca["MntWines"])
mediaDasVarianciasMntWines= np.mean([vari0KidMntWines,vari1KidMntWines,vari2KidMntWines])
varianciaEntreMediasMntWines = (varianciaDasMediasMntWines*46)/mediaDasVarianciasMntWines
razaoF_total = varianciaEntreMediasMntWines/mediaDasVarianciasMntWines
#F = 3.063
print(razaoF_total)
grafico.scatter(dados["MntWines"],dados["Kidhome"])
grafico.xlabel("MntWines")
grafico.grid()
grafico.show() """

""" print(matris_correlacao["Kidhome"].sort_values(ascending=False))
crianca = dados.iloc[:,[1,14,36]]
tem0crianca = crianca[crianca["Kidhome"] == 0]
tem1crianca = crianca[crianca["Kidhome"] == 1]
tem2crianca = crianca[crianca["Kidhome"] == 2]
tem0crianca = tem1crianca.sample(46)
tem1crianca = tem2crianca.sample(46)
media0KidMntTotal = np.mean(tem0crianca["MntTotal"])
media1KidMntTotal = np.mean(tem1crianca["MntTotal"])
media2KidMntTotal = np.mean(tem2crianca["MntTotal"])
media0KidVisitaWeb = np.mean(tem0crianca["NumWebVisitsMonth"])
media1KidVisitaWeb = np.mean(tem1crianca["NumWebVisitsMonth"])
media2KidVisitaWeb = np.mean(tem2crianca["NumWebVisitsMonth"])
varianciaDasMediasMntTotal = np.var([media0KidMntTotal,media1KidMntTotal,media2KidMntTotal])
varianciaDasMediasVisWeb = np.var([media0KidVisitaWeb,media1KidVisitaWeb,media2KidVisitaWeb])
vari0KidMntTotal = np.var(tem0crianca["MntTotal"])
vari1KidMntTotal = np.var(tem1crianca["MntTotal"])
vari2KidMntTotal = np.var(tem2crianca["MntTotal"])
vari0KidVisitaWeb = np.var(tem0crianca["NumWebVisitsMonth"])
vari1KidVisitaWeb = np.var(tem1crianca["NumWebVisitsMonth"])
vari2KidVisitaWeb = np.var(tem2crianca["NumWebVisitsMonth"])
mediaDasVarianciasMntTotal= np.mean([vari0KidMntTotal,vari1KidMntTotal,vari2KidMntTotal])
mediaDasVarianciasVisitaWeb = np.mean([vari0KidVisitaWeb,vari1KidVisitaWeb,vari2KidVisitaWeb])
varianciaEntreMediasMntTotal = (varianciaDasMediasMntTotal*46)/mediaDasVarianciasMntTotal
varianciaEntreMediasWebVisited = (varianciaDasMediasVisWeb*46)/mediaDasVarianciasVisitaWeb
razaoF_web = varianciaEntreMediasWebVisited/mediaDasVarianciasVisitaWeb
razaoF_total = varianciaEntreMediasMntTotal/mediaDasVarianciasMntTotal
#F = 3.063
print(razaoF_total, razaoF_web)
grafico.subplot(2,1,1)
grafico.scatter(dados["Kidhome"],dados["MntTotal"])
grafico.grid()
grafico.ylabel("TotalSpent")
grafico.subplot(2,1,2)
grafico.scatter(dados["Kidhome"],dados["NumWebVisitsMonth"])
grafico.grid()
grafico.ylabel("NumWebVisitsMonth")
grafico.show() """

""" 
'Income'

'Kidhome'
'Teenhome'

'Recency'

'MntWines'
'MntFruits'
'MntMeatProducts'
'MntFishProducts'
'MntSweetProducts'
'MntGoldProds'
'MntTotal'
'MntRegularProds'

'NumDealsPurchases'
'NumWebPurchases'
'NumCatalogPurchases'
'NumStorePurchases'
'NumWebVisitsMonth'

'AcceptedCmp3'
'AcceptedCmp4'
'AcceptedCmp5'
'AcceptedCmp1'
'AcceptedCmp2'
'Complain'

'Z_CostContact'
'Z_Revenue'
'Response'
'Age'
'Customer_Days'

'marital_Divorced'
'marital_Married'
'marital_Single'
'marital_Together'
'marital_Widow'

'education_2n Cycle'
'education_Basic'
'education_Graduation'
'education_Master'
'education_PhD'

'AcceptedCmpOverall'
"""

# A renda está abaixo da média para quem tem apenas educação básica
# A maioria (79%) compraram vinhos fora das ofertas de campanha.
# 28 é a idade mínima de quem tem crianças em casa.
# Quanto maior a renda, menor a quantidade de visitas á internet.
# Quem gasta mais com vinhos, tende a fazer mais compras na loja.
# Quanto maior a quantidade de crianças, menor a quantidade ce compras por catálogo.
# Quem gasta mais com carnes, tende a fazer mais compras por catálogo.
# Quem gasta mais com vinhos, tende a fazer mais compras na web.
# Vinhos mais baratos são mais escolhidos do que os vinhos de marca premium.
# Pessoas com rendas maiores, no geral, gastam mais com produtos.
# Pessoas com rendas maiores gastam mais com peixes (fish products).
# Quanto maior o gasto com carnes, maior o número de compras na loja ou por catálogo.
# Quanto maior a quantidade de crianças, menor os gastos em totais de produtos nos últimos 2 anos (considerando amostra de tamanho = 46).
# Quanto maior a quantidade de crianças, menor os gastos com vinhos (considerando amostra de tamanho = 46).
# A quantidade de crianças não influencia na quantidade de visitas por mês à internet (considerando uma amostra de tamanho = 46).