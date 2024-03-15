import random
import os.path

def existeFichero(nombre):
    return os.path.exists(nombre)

def generar_codigos(lista):
    codigo=""
    letra1="bcdfghjkmnprstv"
    letra2="aeiou"
    
    for i in range (20):
        global f
        codigo+=random.choice(letra1) 
        codigo+=random.choice(letra2) 
        codigo+=chr(random.randint(ord("a"), ord("z"))) 
        for j in range (3): 
            codigo+=str(random.randint(2,8))
        lista.append(codigo)
        codigo=""
    if existeFichero("generador/codigos.txt"):
        f=open("generador/codigos.txt","r")
        if f.read()!="":
            opcion=str(input("El fichero ya tiene contenido, desea sobreescribirlo con los nuevos codigos?"))
            if opcion=="si" or opcion=="Si":
                f=open("generador/codigos.txt",'w')
                f.write("")
                for x in lista:
                    f.write(x + "\r\n")
                f.close()
        else:
            f=open("generador/codigos.txt",'w')
            for x in lista:
                f.write(x + "\r\n")
            f.close()
    

lista_codigos=[]           
print("-" * 28)
print("-"*3, "Generador de códigos","-"*3)
print("-"*28)
generar_codigos(lista_codigos)
print(f"Gracias por usar el programa.")