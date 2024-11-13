#Importaciones de los mòdulos-librerìas:
import datetime#Importaciòn de la librerìa datetime para conf fechas,hs
import hashlib#Mòdulo que permite darle un hash a los datos, haciendo que estos tengan una integridad y generen identificadores 
import json#Convierte los datos en un fromato JSON comprensible para las màquinas y las personas
from flask import flask#Herramienta para crear apps webs


class blockchain:#Creacion de la clase blockchain

    #Constructor de la clase sin paràmetros-propiedades
    def __init__(self):
        self.chain = []#Creaciòn de una lista vacìa
        self.create_block(proof=1,previous_hash = '0')#Uso del mètodo create....(que està abajo) el cùal le pasamos dos args un valor de prueba en este caso inicializado con 1 y un previous hash el cùal en este caso le mandamos 0 pq estamos poniendo el 1ero bloque-bloque gènesis y al no haber un bloque anterior se usa 0 

    
    #CReaciòn del mètodo create_block con dos paràmetros
    def create_block(self,proof,previous_hash):
        #Estructura que tendrà el bloque(hashes previos,tiempo del bloque,prueba de trabajo del bloque(para la validaciòn) e ìndice del bloque(nùmero-posiciòn de este)) toda esta metida en un diccionario:
        block = {"index":len(self.chain)+1#,
                 'timeramp':str(datetime.datetime.now()),
                 'proof':proof,
                 'previous_hash'previous_hash}
        
        #Metemos los bloques estos dentro de la lista vacìa creada en el cosntructor
        self.chain.append(block)
        #Retornamos el bloque
        return block


    
    #Mètodo para retornar el ùltimo bloque de la lista
    def get_return_block(self):
        return self.chain[-1]#Con -1 en py se accede al ùlt elemento   

        


    #Mètodo para encontrar un nuevo valor para la prueba de trabajo
    def proo_of_work(self,previous_proof):
        new_proof = 1#Inicializa en 1,lo que hace que inicie a buscar desde 1 el valor de prueba, este mismo se incremnetarà hasta encontrar el val correcto que cumple con los requisistos especìficos que aplique esa prueba de trab
        check_proof = False#Inicializa con False, para que a la hr de encontrar la prueba de trab varìe a True
        
        #Este bucle while lo que hace es que mientras el check_proof sea falso que se ejecuten varias cosas dentro de èl para tratar de encontar ese proof-prueba de trabajo
        while check_proof is False:
            #Este hash de operacion(con el cùal se trabajarà) lo que guarda es bàsicamente es un haash con el SHA-256.En pocas palabras lo que ocurre acà es que 1ero sel calc el cuadrado de new_proof y el de previous_proof y de ahì se calcula la diferencia(con el -),lo 2do que pasa es que este resultado primero se transfora en str y dps lo pasa a bytes con el mètodo .encode()(es necesarios pasarlo a bytes pq lo requiere el hash) y lo 3ero que pasa es que se aplica el algoritmo SHA-256 a esa cadena codificada en bytes y devuelve el hash como cadena hexadècimal 
            hash_operation  = hashlib.sha256(str(new_proof**2-previous_proof**2)encode()).hexdigest()
            
            #SI el hash oparacional sus primero 4 nùmeros son cuatro ceros, està bien y por ende....
            if hash_operation[:4]=='0000':
                #Cambia el estado de check_proof a True
                check_proof == True
            
            
            #DE LO CONTRARIO si no hay cuatro ceros en los primeros 4 nùmeros...
            else:
                #Se sigue en el intento de bùsqueda de la prueba de trabajo y se incrementa una oportunidad mas siempre y cuando aùn no se haya encontrado esa prueba
                new_proof +=1
            
            
            
            #Siempre retornarà los hashes, es decir a pesar que haya encontrado o no el proof, siempre nos retornarà el hash 
            return new_proof
        
        
       #Creaciòn de la funcion hash para verificar que el previous hash de cada bloque es igual que el del anterior, tiene un paràmetro llamado block que funciona como input
       def hash(self,block):
           
           #Conv el bloque en una cadena JSON y dps la codifica a bytes para que pueda ser pasa a hash
           encoded_block = json.dumps(block,sort_keys =  True).encoded()
           
           #Càlcula el hash sha-256 para que pueda ser pasado en formato de bytes y lo conv en una cadena hexadecimal
           return hashlib.sha256(encoded_block()).hexdigest()
    