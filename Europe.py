from City import City 
    
def search(init, final_values,methode):
    frontiere = [init]
    history = []
    while frontiere:
        print("Frontiere=" + str(frontiere))
        print("History=" + str(history))
        etat = frontiere.pop()
        history.append(etat.name)
        if etat.final(final_values):
            return (etat, len(history))
        ops = etat.applicable_operators()
        for op in ops:
            new = etat.apply(op)
            if (new.name not in history) and (new not in frontiere) and new.legal():
                frontiere.insert(0,new)
            if (new in frontiere) and (frontiere[frontiere.index(new)].g > new.g):
                    frontiere[frontiere.index(new)] = new
        frontiere.sort(key=lambda etat: etat.distance(final_values,methode), reverse=True)
       
       
    return None

def printResult(result,visited):
    if result is not None:
        print("\n---Chemin Trouve---")
        print("\n---"+ str(visited)+" Ville Visite---")
        villes = []
        while result.parent is not None:
            villes.append(result)
            result = result.parent
            
        villes.append(result)
        villes.reverse()
        for ville in villes:
            print("" + str(ville) + " (" + str(ville.g) + " km) ")
    else:
        print('solution not found')
    print("\n--------------------")
  
if __name__ == '__main__':
    City.parsePosition();
    City.parseConnection();
    
    depart = "Warsaw"
    arriver = "Lisbon"
    
    for i in range(1,6):
        print(i)
        result = search(City(depart,0),arriver,i)
        printResult(result[0],result[1])
   


    
    
    