import json

with open("data_bob_no_age.json") as f:
    data = json.load(f)

resident_ages = []

apartments = data['ApartmentBuilding']['Apartments']
for apartment in apartments:
    residents = apartment['Residents']
    for resident in residents:
        age = resident.get('Age', 'N/A')
        resident_ages.append(age)
        
print(resident_ages)