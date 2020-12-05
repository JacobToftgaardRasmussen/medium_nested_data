import json

with open("data.json") as f:
    data = json.load(f)

resident_names = []

apartments = data['ApartmentBuilding']['Apartments']
for apartment in apartments:
    residents = apartment['Residents']
    for resident in residents:
        name = resident['Name']
        resident_names.append(name)
        
print(resident_names)


