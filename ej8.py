

# Ingresas la altura en metros 
prompt = int(input("Ingrese su medida en metros = "))
# Asignacion de valores en var
pulgada = 2.54
metro = 100
pie =  pulgada*12
yarda = pie*3
# Utilizando la variable de ingreso lo multiplcias por el valor convirtiendo de metros a cm
print("Su medida es = ",prompt," En cm = " ,prompt*metro,"cm")
# Utilizando la variable de ingreso lo multiplcias por el valor convirtiendo de metros a cm y despues dividiendolo por el valor de la pulgada
print("Su medida es = ",prompt," En pulgadas = ",(prompt*metro)/pulgada,"pulgadas")
# Utilizando la variable de ingreso lo multiplcias por el valor convirtiendo de metros a cm y despues dividiendolo por el valor de la pulgada y nuevamente por el valor del pie
print("Su medida es = ",prompt, " En pies= ",((prompt*metro)/pulgada)/pie,"Pies")
# Utilizando la variable de ingreso lo multiplcias por el valor convirtiendo de metros a cm y despues dividiendolo por el valor de la pulgada y nuevamente por el valor del pie y ahora de la yarda
print("Su medida es = ",prompt, " En yardas= ",((prompt*metro)/pulgada)/yarda,"Yardas")