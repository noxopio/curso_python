
import os
num_1="Primer  numero:  "
num_2="Segundo numero:  "
resultado=""
def run():
 opcion=0

def suma (num_1,num_2):
    total=int(input(num_1)) + int(input(num_2))
    return total
def resta (num_1,num_2):
    total=int(input(num_1)) - int(input(num_2))
    return total
 
menu ="""
         -----------------------------------------------------------------------------------
                                         MENU  PRINCIPAL
         -----------------------------------------------------------------------------------                                                               
         1.SUMA.
         2.RESTA.
         3.MULTIPLICACION.
         4.DIVISION.
         5.POTENCIA
         0.SALIR
         -----------------------------------------------------------------------------------
         """
    
opcion = int(input(menu))
while opcion !=1 and opcion >5:
 opcion = int(input(menu)) 
 if opcion==0:
     break
           
 elif opcion == 1:
     os.system("clear")
     print (str(opcion)+" "+ "suma")
     resultado=suma(num_1,num_2)
     print ("TOTAL:  "+str(resultado))
else opcion == 2:
     os.system("clear")
     print (str(opcion)+" "+"resta")
     resultado=resta(num_1,num_2)
     print ("TOTAL:  "+str(resultado))

      













if __name__ == "__main__" :
    run()
