Listenpreis = 159
Rabatt = 5
Mehrwertsteuer = 19

NeuerPreis = Listenpreis*((100-Rabatt)/100)
NeuerPreis = NeuerPreis*((100+Mehrwertsteuer)/100)

print(round(NeuerPreis, 2))
