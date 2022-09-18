#Ana Isabel Sanchez Heredia 
#HPC elaborar una lista con funcion .append
#EJEMPLO 1:
#lista1=[1,2,3,4]
#print(lista1)
#lista2=[1,3,14,"a",True, [4,5,6],{1,2,3},(8,"a",5,4)]
#print(lista2)
#print(len(lista2))
#print(lista2[6])
#lista__cal.append(5)
#print(lista__cal)
#lista_cal.append(6)
#---------------------------------------------------------------------------------------------------------------
#LAS LISTAS SON TIPOS DE DATOS PROPIOS DE PYTHON, UTILIZANDO SUS PROPIEDADES 
#LOS METODOS VAN EN EL PARENTESIS Y LOS METODOS TIENE LA FORMA DE FUNCION 
#LAS LISTAS SON COLECCIONES INTTEGRALES PORQUE SE PUEDEN RECORRER TODOS SUS ELEMETNTOS, TAMBIEN LAS LISTAS SON OBJETOS 
#LAS LISTAS SIN ENDEXADAS: PUEDO ACCEDER A CUALQUIER ELEMENTO MEDIANTE SU INDICE
# EN LA LISTA LOS ELEMENTOS SE AGREGAN AL FINAL DE ELLA 
#---------------------------------------------------------------------------------------------------------------
#RELLENAR UNA LISTA CON LOS NUMEROS NATURALES DEL 1 AL 10
#lista_numeros=[]
#for i in range(1,11):
 #   lista_numeros.append(i)

#print(lista_numeros)
#---------------------------------------------------------------------------------------------------------------
#EJEMPLO 2:
#SLICES (REBANADAS)
#lista1=[1,2,3,4,5,6,7,8,9,10]
#print(lista1)
#print(lista1[:])
#print(lista1[0:10])
#print(lista1[:int(len(lista1)/2):])
#print(lista1[:int(len(lista1)/2)])

#lista1=[1,"dos",3,"cuatro"]
#print(lista1)
#lista1[1]=2
#print(lista1)
#lista2=lista1[:]
#print(lista2)
#lista2[1]=2

#print("lista 1",(id)lista1)
#print("lista 2",(id)lista2)
#lista2[1]=2
#print("-----------------")#separador
#print(f"direccion:{id(lista2)},lista 1:{lista1}")
#print(f"direccion: {id(lista2)}, lista 2: {lista2}")
#print("afaorms corrects")
#lista1=[1,"dos",3,"cuatro"]
#lista2=lista1[:]
#print(f"direccion lista1:{id(lista1)}")
#print(f"direccion lista2: {id(lista2)}")
#lista2[1]=2
#lista2[3]=4
#print(f"direccion:{id(lista1)},lista1:{lista1}")
#print(f"direccion:{id(lista2)},lista2:{lista2}")


#lista1=[0,1,2,3,4]
#lista2=[5,6,7]
#lista[5:]=lista2 #[5,6,7]
#lista1[len(lista1):]=lista2
#print(lista1)

#insertarnal inicio de la lista varios elementos en una lista
#lista1[:0]=lista2
#print(lista1)


#lista1.extend(lista2)
#lista1.append(lista2)
#print(lista1)


#lista1[:0]=lista2
