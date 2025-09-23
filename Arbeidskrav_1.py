"""
Arbeidskrav 1, el, eller bensinbil
Oppgaven viser beregning av totalkostnad på elbil og bensinbil 
ut i fra forhåndsdefinerte parametere

Created on Tue Sep 23 18:22:47 2025

author: Magnus Slettjord, magnusslettjord@hotmail.com
"""
km=10000  # Antall kilometer kjørt pr år
Fors_El = 5000  # Pris forsikring for el-bil pr år
Fors_B = 7500   # Pris forsikring for bensinbil pr år
TFA = 8.38 * 365  # Trafikkforsikringsavgift 8,38 kr pr dag
Drivst_El = 0.2 * 2  # Drivstoffkostnad el-bil 0.2 KWh/km * 2 kr/kWh 
Drivst_B = 1  # Drivstoffkostnad bensinbil 1.0 kr/ km
BomA_El = 0.1  # Bomavgift elbil 0.1 kr/km
BomA_B = 0.3  # Bomavgift bensinbil 0.3 kr/km 
TotalK_El = Fors_El + TFA + km*(Drivst_El + BomA_El)  # Totalkostnad elbil pr år
TotalK_B = Fors_B + TFA + km*(Drivst_B + BomA_B)  # Totalkostnad bensinbil pr år
print('Totalkostnad El-bil:', TotalK_El,)  # Viser kostnadene i konsollen
print('Totalkostnad bensinbil:', TotalK_B)  # Viser kostnadene i konsollen
print('Forskjell:', TotalK_B - TotalK_El)  # Viser forskjellen mellom de to verdiene