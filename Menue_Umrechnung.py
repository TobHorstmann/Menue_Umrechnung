#Menü-Aufbau mit While-Schleife
while True:
    print ("Was möchten Sie umrechnen?")
    print ("""\n(1) Zentimeter -> Zoll
(2) Kilometer -> Meilen
(3) Quadratkilometer -> Hektar
(4) Kilometer/Stunde -> Meter/Sekunde
(5) Kilobyte -> Gigabyte
(0) Menü beenden""")
 
 
#Auswahl der Umrechnungsmöglichkeiten
    
    auswahl = input("\nIhre Auswahl ")
    
#Umrechnung Zentimeter in Zoll    
    if auswahl == "1":
        print ("(1) Zentimeter in Zoll")
        zenti = float(input("Eingabe Zentimeter: "))
        zoll = zenti * 0.3937
        print (zenti, "cm sind " ,zoll, "Zoll")
        
#Umrechnung Kilometer in Meilen        
    elif auswahl == "2":
        print ("(2) Kilometer in Meilen")
        kilom = float(input("Eingabe Kilometer: "))
        meilen = kilom * 0.6213
        print (kilom, "Kilometer sind " ,meilen , "Meilen")
        
#Umrechnung Quadratkilometer in Hektar         
    elif auswahl == "3":
        print ("(3) Quadratkilometer in Hektar")
        quad = float(input("Eingabe Quadratkilometer: "))
        ha = quad * 100
        print (quad, "Quadratkilometer sind ", ha, "Hektar")
        
#Umrechnung Kilometer/Stunde in Meter/Sekunde        
    elif auswahl == "4":
        print ("(4) Kilometer/Stunde in Meter/Sekunde")
        kmh = float(input("Eingabe Kilometer/Stunde: "))
        ms = kmh / 3.6
        print (kmh, "Kilometer/Stunde sind " , ms, "Meter/Sekunde")
        
#Umrechnung Kilobyte in Gigabyte
    elif auswahl == "5":
        print ("(5) Kilobyte in Gigabyte")
        kilob = float(input("Eingabe Kilobyte: "))
        gigab = kilob / 1000000
        print (kilob, "Kilobyte sind" , gigab, "Gigabyte")
        
#Auswahl Menü beenden
    elif auswahl == "0":
        break
    
#Falsche Auswahl
    else:
        print ("Ungültige Auswahl.Bitte wählen Sie zwischen 1-5 oder 0 zum Beenden!")
        
#Abfrage weiterer Umrechnungen        
    weiter = input ("\nMöchten Sie eine weitere Umrechnung durchführen? (ja/nein): ").strip().lower()
    if weiter != 'ja':
        print("Programm wird beendet.")
        break        
            
        
        


                       
     
     
     
     
           
            