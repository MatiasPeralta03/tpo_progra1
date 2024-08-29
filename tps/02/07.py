#Intercalar los  elementos de  una lista entre los elementos de  otra.  La intercalación 
#deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará 
#una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3] 
#y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden 
#tener distintas longitudes.

lista1=[8,1,3]
lista2=[5,9,7,4,5,2,3]
index = 1
for i in range(0,len(lista1)):
    lista1[index:index] = [lista2[i]]
    index = index + 2

print(lista1)







