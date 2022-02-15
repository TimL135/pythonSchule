# This will import math module
import math
arbeitsDauer = 5.1
arbeitsDauer = math.floor(arbeitsDauer)
belohnung = 0

if arbeitsDauer < 1:
    belohnung = 0
elif arbeitsDauer < 2:
    belohnung = 50
elif arbeitsDauer < 4:
    belohnung = 100
else:
    belohnung = 150+(arbeitsDauer-4)*10
print('{}€ bonus'.format(belohnung))
