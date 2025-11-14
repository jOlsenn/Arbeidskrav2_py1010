# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 18:58:57 2025

@author: Jan-Halvor Olsen
"""
# [Oppgave 1]

# [Variabel med varierende verdi, her kan du skrive inn hvilket år
# du er født i, i consolen]
alder = int(input("Hvilket år er du født?"))

# [Vi skulle finne ut hvor gammel man blir i 2024, her blir det da 2024 minus
# årstallet også blir det printet til consolen]
print("I løpet av 2024 blir du", 2024 - alder, "år gammel")






# [Oppgave 2]

# [Her importerer jeg numpy biblioteket for å få fuksjonen "np.ceil"]
import numpy as np

# [Varierende variabel for hvor mange som er i klassen]
antall_elever = int(input("Skriv antall elever:"))

# [Variabel for mengde pizza pr person]
pizza = 0.25

# [Her bruker jeg np.ceil til å runde opp svaret på hvor mye pizza som trengs 
# da det ikke vil være naturlig å si det trengs f.eks 1.25 pizzaer]
mengde_pizza = np.ceil(antall_elever * pizza)

# [Her bruker jeg int på mengden pizza slik at jeg få et svar uten desimaler
# da det ikke ville vært naturlig å si man trenger 2.0 pizzaer]
mengde = int(mengde_pizza)

# [Her printes antallet pizzaer som trengs på det gitte antallet elever]
print("Det må kjøpes inn", mengde, "pizzaer")







# [Oppgave 3] 

# [Importerer numpy for å bruke den presatte PI funksjonen]
import numpy as np

#[Varierende variabel for grader]
v_grad = float(input("Skriv inn gradtallet:"))

#[Dette er en satt variabel som regner ut radianen basert på
# gradene som blir satt i v_grad * numpy sin presatte pi / 180]
v_rad = v_grad * np.pi / 180 

# [Skriver ut resultatet og runder av til 2 desimaler]
print("Radianen er:", round (v_rad, 2))





# [Oppgave 4]

# [Dette er Dictionary slik som oppgitt i oppgaven]
land = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873],
        }

# [while true løkken brukes for at programmet skal loope slik at man får
# brukt den nye informasjonen som blir lagt inn]
while True: 
    land_input = input("Skriv inn land du vil ha informasjon om:")

# [Dette er for å stoppe programmet og skrives inn i stede for et land]
    if land_input == "stopp":
        break

# [Sjekke om landet finnes i listen]
    if land_input in land: 
        
# [Henter hovedstad fra plass 0 i dictionaryen til det aktuelle landet]
        hovedstad = land[land_input][0]
# [Henter innbyggere fra plass 1 i dictionaryen til det aktuelle landet]
        innbyggere = land[land_input][1]
        
# [Om landet er i Dictionaryen blir informasjonen printet til bruker]
        print(hovedstad, "er hovedstaden i", land_input, "og det er", innbyggere, "mill inbyggere der")
    
    else:
# [Om landet ikke eksisterer får brukeren spørsmål om de ønsker å legge det til]
        nytt_land = input("Dette landet eksisterer ikke i databasen, vil du legge det til?")

# [Ønsker brukeren å legge til landet skriver dem Ja, så begynner prosessen]
        if nytt_land == "Ja": 
# [Bruker får spørsmål om hvilken hovedstad som tilhører det nye landet]
            hovedstad = input("Skriv inn hovedstaden i " + land_input + ":")
# [Bruker får spørsmål om hvor mange som bor i den hovedstanden de skriver inn]
            innbyggere = float(input("Hvor mange mill innbyggere er det i " + hovedstad + "?"  ))
     
# [Dataen for det nye landet blir lagt til i dictionaryen]
            land[land_input] = [hovedstad, innbyggere]
        
# [Bekreftelse på at nytt land er lagt til i databasen]
            print("Landet er lagt til i databasen!")
# [Hele dictionaryen blir printet slik at man kan se informasjonen den inneholder]
            print(land)

# [Skulle noe annet enn "Ja" blir svar på spørsmålet om de vil legge til nytt
# land så blir det printet en beskjed om at landet ikke er lagt til]
        else:
            print("Landet ble ikke lagt til.")
 
# [Dette er for å få et mellomrom mellom databasen og spørmålet blir stilt igjen]
    print( ) 
    
    
 
    
 
    
# [Oppgave 5]

# [Importerer numpy for å kunne bruke presatte matte funksjoner]
import numpy as np 
    
a = float(input("Skriv inn a (Diameter på halvsirkel)"))
b = float(input("Skriv inn b (Høyde på trekant)"))


# [Her defineres funksjonen med de nødvendige argumentene]
def areal_omkrets (a, b):
        
# [Her regnes arealet på sirkelen ut ved Pi*(Diameter/2)^2 før den blir delt
# på 2 for å få arealet til halvsirkelen]
    halvsirkel_areal = (np.pi * (a/2)**2) / 2 
  
# [Her blir omkretsen til halvsirkelen regnet ut ved Pi*(Diameter/2)] 
    halvsirkel_omkrets = np.pi * (a/2)
    
# [I denne variabelen blir arealet på trekanten regnet ut med
# katet*katet / 2 altså a*b / 2]   
    trekant_areal = (a * b) / 2    
    
# [Her blir hypotenusen av trekanten regnet ut ved med 
# roten av katet^2 + katet^2 altså roten av a^2+b^2]
    trekant_hypotenus = np.sqrt (a**2 + b**2)
    
# [Her trenger vi ikke hele omkretsen på trekanten så her blir omkretsen
# Hypotenus + b]
    trekant_omkrets = b + trekant_hypotenus
    
# [Her lager vi variabler for den totale omkretsen og arealet for halvsirkelen
# og for trekanten]
    areal_total = trekant_areal + halvsirkel_areal
    omkrets_total = trekant_omkrets + halvsirkel_omkrets
    
# [Her printer jeg ut arealet av figuren også den ytre omkretsen av figuren
# også bruker jeg round til å korte det ned til 2 desimaler]
    print("Arealet av denne figuren er:", round(areal_total, 2),"cm^2")  
    print("Den ytre omkretsen for denne figuren er:", round(omkrets_total, 2), "cm")
  
# [Her blir funksjonen kalt på med verdien fra input, slik at alle beregningene
# blir utført]
areal_omkrets (a, b)    
  





# [Oppgave 6]

# [Importerer Numpy for å få linspace til jevntfordele mellom -10 og 10 ]
import numpy as np

# [Importerer matplotlib til å lage grafen]
import matplotlib.pyplot as plt

# [linespace lager her 200 punkter jevnt fordelt mellom -10 og 10 slik at 
# jeg får en jevn kurve]
x = np.linspace(-10,10,200)    

# [Her blir funksjonen f(x) = -x^2 - 5 regnet ut for alle punktene i X]
f = -x**2 - 5 

# [Denne plottet x verdien mot det som har blitt regnet ut i f og gir 
# ut grafen i consolen]
plt.plot(x, f)
    
    

    
    
    
    
    
    
    
    
    