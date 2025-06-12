def conteggio_parole_uniche(text):
    word_counts = {}
    
    punteggiatura = ".,!?;:()[]{}'\"…-"

    tokens = text.split()

    for parola in tokens:
        

        parola_normale = parola.lower()
        
        parola_normale = parola_normale.strip(punteggiatura)

        
        if parola_normale:
            word_counts[parola_normale] = word_counts.get(parola_normale, 0) + 1

    return word_counts



