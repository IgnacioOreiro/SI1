#Una inmobiliaria paga a sus vendedores un salario de $50000, más una
#comisión de $5000 por cada venta realizada, más el 5% del valor de las
#ventas. Realizar un programa que imprima el número del vendedor y el
#salario que le corresponde en un determinado mes. Se leen el número
#del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.


# Asignas valores
salarioMensual = 50000
comusionXVenta = 5000
# Ingresas el valor de la propeidad en una variable
venta = int(input("Valor de la propiedad = "))
# Multiplcias el valor de la propiedad por el 0.5 obteniendo el 5% de lo que vale
ventas = venta*0.05
# Sumas el salario la comision y el numero de ventas
total = salarioMensual + comusionXVenta + ventas
# Imprimis el total del salario
print(total)