import sys

vettore = [0 for x in range(0, 30000)] #vettore di 30000 locazioni
locazione = 0 #locazione corrente
esegui = "" #istruzione da eseguire

#estrapola il pezzo di codice da eseguire (ciclo)
def estrapola(controlla):
   i = 0
   
   while controlla[0:i+1].count("[") != controlla[0:i+1].count("]"): 
      i += 1
   
   return controlla[1:i]

#analizza il codice e lo esegue
def run(vettore, locazione, istruzione):

   posizione = 0
   
   while posizione < len(istruzione):
      cmd=istruzione[posizione]

      if cmd == "<": 
         locazione -= 1
      
      elif cmd == ">": 
         locazione += 1
      
      elif cmd == "+": 
         vettore[locazione] += 1
      
      elif cmd == "-": 
         vettore[locazione]-=1
      
      elif cmd == ".": 
         print(chr(vettore[locazione]), end="")
      
      elif cmd == ",":
         vettore[locazione]=ord(input())
      
      elif cmd == "[":
         istr=estrapola(istruzione[posizione:])
         
         while vettore[locazione] != 0: 
            run(vettore, locazione, istr)

         posizione += len(istr)+1

      posizione += 1

#apre il file passato da riga di comando, e ne salva il contenuto in esegui
if len(sys.argv) > 1 and sys.argv[1] != "":
   f = open (sys.argv[1], "r")
   
   for i in f.readlines():
      esegui += i
   
run(vettore, locazione, esegui)
