#questa funzione prende in ingresso una lista di lettere che rappresentano le frequenze di riferimento,
# il path del testo cifrato 
# e restituisce una stringa contenente il testo decifrato e produce un file col testo decifrato
import freq_distr

def decryption_function(pathcifrato, frequenze):
    
    #apertura del file e inserimento del testo cifrato in  una stringa
    input = open(pathcifrato,'r')
    txt = input.read()
    
    #creo la lista delle frequenze dei simboli del testo cifrato in ordine crescente
    list = freq_distr(pathcifrato)
    
    #ciclo di decifratura
    j=0
    for i in list:
        txt=txt.replace(i,frequenze[j])
        j=j+1
        
    #creazione del file di testo 
    
    out=open(pathcifrato+'_decrip', 'w')
    out.write(txt)
    out.close()
    
    #restituisco la stringa
    return txt
