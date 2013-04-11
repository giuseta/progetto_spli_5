# Questa funzione dato in ingresso il path di un file restituisci una stringa contenente il testo cifrato
# e crea un file di testo nel path col il testo cifrato

def encryption_function(txtfilename):

    #apertura del file e inserimento in una stringa
    input = open(txtfilename,'r')
    txt = input.read()
    

    #ciclo di rimpiazzamento per le lettere (le lettere maiuscole
    #corrispondenti vengono sostituite dallo stesso simbolo di quelle minuscole)
    list=range(97,123)
    txt=txt.lower()
    for i in list:
        txt=txt.replace(chr(i),chr(i-96))        

    #creo il file di testo 
    out=open(txtfilename+'_crip', 'w')
    out.write(txt)
    out.close()
    
    
    #ritorno il testo cifrato
    
    return txt
