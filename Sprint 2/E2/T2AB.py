#!/usr/bin/python3
from threading import Thread,Semaphore
import time
 
semaforo = Semaphore(1); #Crear variable semáforo
 
#Definicion de Funciones
#Funcion de region critica, accede solo 1 hilo a la vez
#El hilo al entrar accede con su id y mascota
def region_critica(id, Mascota):
     #Se define global la variable que simula el patio
     global EnPatio;
     #Si en el patio no se encuentra la mascota anterior entra
     if(EnPatio==""):
        print(Mascota+": Salió al patio");
        EnPatio=Mascota;
        print(Mascota+": Hace sus necesitades");
        time.sleep(1.0)
     elif (Mascota==EnPatio):
        print(Mascota+": Entró a la casa");
        EnPatio="";
    
#Definicion de Clase Alicia
class Alicia(Thread):
    def __init__(self,id): #Constructor de la clase Alicia
         Thread.__init__(self);
         self.id=id;
 
    def run(self): #Metodo que se ejecutara con la llamada start en Programa Principal
          semaforo.acquire();
          MiMascota="Gato"; #La mascota que tiene Alicia
          region_critica(self.id, MiMascota); #Llamada a la region critica
          semaforo.release();

#Definicion de Clase Bernardo
class Bernardo(Thread):
    def __init__(self,id): #Constructor de la clase Bernardo
         Thread.__init__(self);
         self.id=id;
    def run(self): #Metodo que se ejecutara con la llamada start en Programa Principal
          semaforo.acquire();
          MiMascota="Perro"; #La mascota que tiene Bernardo
          region_critica(self.id, MiMascota); #Llamada a la region critica
          semaforo.release();          
  
#Programa Principal
while True:
     EnPatio=""; #Variable que simula ser el patio
     hilos = [Alicia(1),Bernardo(2)]; #Creacion de objetos Hilos
     for h in hilos:
          h.start(); #Ejecutar todos los hilos
