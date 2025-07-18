import pandas as pd
import matplotlib.pyplot as plt

# Estilo de gráficos
plt.style.use('ggplot')

# Ruta al archivo CSV (ajustala si está en otro lugar)
archivo = r"D:\Analisis de datos 1\DATA\data\archive (1)\100000 Sales Records.csv"

# Cargar el archivo CSV
df = pd.read_csv(archivo)
df.columns = df.columns.str.strip()  # Limpiar espacios en los nombres de columnas

# Convertir fechas
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# ----------------------------------------------------------------------------
# 1. Ventas Totales por Región
# ----------------------------------------------------------------------------
ventas_region = df.groupby('Region')['Total Revenue'].sum().sort_values()
ventas_region.plot(kind='barh', color='skyblue')
plt.title('Ventas Totales por Región')
plt.xlabel('Total Revenue')
plt.ylabel('Región')
plt.tight_layout()
plt.show()
input("Presioná Enter para continuar al siguiente gráfico...")

# ----------------------------------------------------------------------------
# 2. Ventas Totales por Canal de Venta
# ----------------------------------------------------------------------------
ventas_canal = df.groupby('Sales Channel')['Total Revenue'].sum().sort_values()
ventas_canal.plot(kind='bar', color='lightgreen')
plt.title('Ventas Totales por Canal de Venta')
plt.ylabel('Total Revenue')
plt.xlabel('Canal de Venta')
plt.tight_layout()
plt.show()
input("Presioná Enter para continuar al siguiente gráfico...")

# ----------------------------------------------------------------------------
# 3. Unidades Vendidas por Tipo de Producto (Top 10)
# ----------------------------------------------------------------------------
top_items = df.groupby('Item Type')['Units Sold'].sum().sort_values(ascending=False).head(10)
top_items.plot(kind='bar', color='coral')
plt.title('Top 10 Productos por Unidades Vendidas')
plt.ylabel('Unidades Vendidas')
plt.xlabel('Tipo de Producto')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
input("Presioná Enter para finalizar...")