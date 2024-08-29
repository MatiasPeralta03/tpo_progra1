#Utilizar  la  técnica  de  listas  por  comprensión  para  construir  una  lista  con  todos  los 
#números impares comprendidos entre 100 y 200.
num_impares=[n for n in range (100, 201) if n%2!=0 ]
print(num_impares)