import json
import os

import random
#add random number to the variable lote

def generaAspirina():
    lote = "X"+ str(random.randint(0, 9))+str(random.randint(0, 9))+"AU" + str(random.randint(0, 9))
    aspirina = {   "id": 1,
        "nombre": "aspirina",
        "descripcion": "Medicamento para el dolor de cabeza",
        "lote": lote
    }
    return aspirina

def generaParacetamol():
    lote = "X"+ str(random.randint(0, 9))+str(random.randint(0, 9))+"AU" + str(random.randint(0, 9))
    paracetamol = {   "id": 2,
        "nombre": "paracetamol",
        "descripcion": "Medicamento para el dolor de cabeza",
        "lote": lote
    }
    return paracetamol

def generaIbuprofeno():
    lote = "X"+ str(random.randint(0, 9))+str(random.randint(0, 9))+"AU" + str(random.randint(0, 9))
    ibuprofeno = {   "id": 3,
        "nombre": "ibuprofeno",
        "descripcion": "Medicamento para el dolor de cabeza",
        "lote": lote
    }
    return ibuprofeno

aList = []

for i in range(100):
    num = random.randint(0, 2)
    if num == 0:
        aList.append(generaAspirina())
    elif num == 1:
        aList.append(generaParacetamol())
    elif num == 2:
        aList.append(generaIbuprofeno())
    
    


jsonString = json.dumps(aList)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()