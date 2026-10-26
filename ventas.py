#pip install pandas
#pip install openpyxl
import pandas as pd 
import matplotlib.pyplot as plt
nombre_planilla=input("Ingrese el nombre de la planilla")
ventas=pd.read_excel(nombre_planilla,sheet_name="Ventas")
#print(ventas)
#print(ventas.describe())
#print(ventas["Precio_Unitario"])
ventas["Facturacion"]=ventas["Precio_Unitario"]*ventas["Unidades"]
#print(ventas["Facturacion"])
print(f"Unidades Vendidas: {ventas["Unidades"].sum()}")
print(f"Total :${ventas["Precio_Unitario"].sum()}")
print(f"Total vendido: ${ventas["Facturacion"].sum()}")
negocios=pd.read_excel(nombre_planilla,sheet_name="Negocios")
ventas=ventas.merge(negocios,on="Negocio", how="left")
# print(ventas)
print("\n=== Facturación por barrio ===")
por_barrio=ventas.groupby("Barrio")["Facturacion"].sum()
print(por_barrio.to_frame())
plt.pie(por_barrio,labels=por_barrio.index,autopct="%1.1f%%")
plt.show()