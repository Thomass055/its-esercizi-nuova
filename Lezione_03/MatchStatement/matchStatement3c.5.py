a:dict[str,int] = {"Nome":str(input("Inserisci il nome: ")), "Età":int(input("inserisci l'età: ")), "Ruolo":str(input("inserisci il ruolo: "))}

match a:
    case  {"Ruolo" : "Admin"}:
       print("Accesso completo a tutte le funzionalità")
    case  {"Ruolo" : "Moderatore"}:
       print("Può gestire i contenuti ma non modificare le impostazioni")
    case {"Ruolo" : "Ospite"}:
            print("Accesso ristretto! Solo visualizzazione dei contenuti")
    case {"Ruolo" : "Utente Adulto" , "Età" : età } if età >= 18: 
            print("Accesso standard a tutti i servizi")
    case {"Ruolo": "Utente Minorenne" , "Età" : età} if età < 18:
            print("Accesso limitato! Alcune funzionalità sono bloccate")
    case _ :
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")
 