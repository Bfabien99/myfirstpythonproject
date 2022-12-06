# LISTES - ALGO : VALEUR LA PLUS PETITE

distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 0.1, 0.6]
nom_chauffeur = ["aa", "zz", "aaa", "aaaaad", "zeaze", "adzc", "qdq"]

"""
def mymin(collection: list | tuple):
    _start = collection[0]
    for data in collection:
        if data < _start:
            _start = data
    print("Le plus petit est:", _start)

mymin(distance_chauffeur_km)
"""
index_min = 0
distance_min = distance_chauffeur_km[0]

# for distance in distance_chauffeur_km:
for i in range(len(distance_chauffeur_km)):
    distance = distance_chauffeur_km[i]
    if distance < distance_min:
        distance_min = distance
        index_min = i
        # index_min = distance_chauffeur_km.index(distance)

print("Distance min :", distance_min)
print("Son index:", index_min)
print("Son chauffeur:", nom_chauffeur[index_min])
