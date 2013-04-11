# questa funzione prende in ingresso una lista di path di file di testo e restituisce in 
#uscita un dizionario con le frequenze dei soli caratteri
# se il testo è 'aaaaaacccckklllllllllll' restituisce il diz 'a': 6, 'c': 4, 'k': 2, 'l': 11,


def freq_distr(txtfilenamelist):

    #creo un unica stringa contenente tutti i file di testo
    txt=''
    for i in txtfilenamelist:
        input=open(i,'r')
        txt=txt+input.read()
    
    txt=txt.lower()  
    DizAscii={}    
    #ciclo che conta le occorrenze di ogni carattere ascii allinterno del testo
    for let in txt:
	if ((ord(let)>96) & (ord(let)<123)):
        	DizAscii[let]= DizAscii.get(let, 0) + 1

    return DizAscii
        
	
    #restituiamo una lista di caratteri ordinati in base alle frequenze
#    items=DizAscii.items()
#    backitems=[ [v[1],v[0]] for v in items]
#    backitems.sort()
#    list=[ backitems[i][1] for i in range(0,len(backitems))]
#    list.reverse()
#    return list
