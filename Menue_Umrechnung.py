#Menü-Aufbau mit While-Schleife
while True:
    print ("Was möchten Sie umrechnen?")
    print (""" (1) Zentimeter in Zoll
                (2) Kilometer in Meilen
                (3) Quadratkilometer in Hektar
                (4) Kilometer/Stunde in Meter/Sekunde
                (5) Kilobyte in Gigabyte
                (0) Menü beenden""")
    
    auswahl = input("Ihre Auswahl ")
    
    if auswahl == "1":
        print ("(1) Zentimeter in Zoll")
        zenti = float(input("Eingabe Zentimeter: "))
        zoll = zenti * 0.3937
        print (zenti, "cm sind " ,zoll, "Zoll")
        
    elif auswahl == "2":
        print ("(2) Kilometer in Meilen")
        kilom = float(input("Eingabe Kilometer: "))
        meilen = kilom * 0.6213
        print (kilom, "Kilometer sind " ,meilen , "Meilen")
        
    elif auswahl == "3":
        print ("(3) Quadratkilometer in Hektar")
        quad = float(input("Eingabe Quadratkilometer: "))
        ha = quad * 100
        print (quad, "Quadratkilometer sind ", ha, "Hektar")
    
    elif auswahl == "4":
        print ("(4) Kilometer/Stunde in Meter/Sekunde")
        kmh = float(input("Eingabe Kilometer/Stunde: "))
        ms = kmh / 3.6
        print (kmh, "Kilometer/Stunde sind " , ms, "Meter/Sekunde")
    elif auswahl == "5":
        print ("(5) Kilobyte in Gigabyte")
        kilob = float(input("Eingabe Kilobyte: "))
        gigab = kilob / 1000000
        print (kilob, "Kilobyte sind" , gigab, "Gigabyte")
    elif auswahl == "0":
        break
    else:
        print ("Ungültige Auswahl")
    
                    
        
        
            
        
        


                       
     
     
     
     
           
            