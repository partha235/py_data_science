import numpy as n

patient_name=n.array([])
patient_diseases=n.array([])
patient_age=n.array([])

def patient_details(name:str,diseases:str,age:int):
    global patient_name, patient_diseases, patient_age
    patient_name=n.append(patient_name,name)
    patient_diseases=n.append(patient_diseases,diseases)
    patient_age=n.append(patient_age,age)

patient_details("a","sugar",49)
patient_details("b","heart",52)
print(patient_age)
