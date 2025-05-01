# 💱 Conversor de Monedas 💱

Un programa simple en Python para convertir entre diferentes monedas utilizando tasas de cambio.

## 📋 Descripción

Este proyecto implementa un conversor de monedas que permite realizar conversiones entre USD, EUR, ARS y BRL utilizando el dólar estadounidense (USD) como moneda base intermediaria. El programa guarda un historial de las conversiones realizadas en un archivo de texto.

## 🚀 Características

- ✅ Conversión entre 4 monedas (USD, EUR, ARS, BRL)
- ✅ Interfaz de usuario por consola
- ✅ Historial de conversiones guardado en archivo de texto
- ✅ Cálculos precisos usando el dólar como moneda intermediaria

## 🛠️ Tecnologías

- Python

## 📊 Tasas de Cambio

Las siguientes tasas de cambio están configuradas en el programa:

| Moneda | Abreviatura | Tasa respecto al USD |
|--------|-------------|----------------------|
| Dólar Estadounidense | USD | 1.0 |
| Euro | EUR | 0.91 |
| Peso Argentino | ARS | 1185.0 |
| Real Brasileño | BRL | 5.0 |

## 📝 Uso

1. Ejecuta el programa principal
2. Selecciona la moneda de origen
3. Selecciona la moneda de destino
4. Ingresa el monto a convertir
5. El programa calculará la conversión y la guardará en el historial

## 📂 Estructura de Archivos

```
├── Actividad8.py      # Archivo principal con la lógica del conversor
├── historial.txt      # Archivo de historial de conversiones
└── README.md          # Este archivo
```

## 🧮 Metodología de Conversión

El programa utiliza el USD como moneda intermediaria para todas las conversiones. Por ejemplo:
- Para convertir de ARS a BRL:
  1. Primero se convierten los ARS a USD
  2. Luego se convierten los USD a BRL

## ⚙️ Funciones Principales

### `cotizaciones_monedas()`
Retorna un diccionario con las tasas de cambio respecto al USD.

### `convertir_monedas(monto, moneda_origen, moneda_destino, cotizaciones)`
Realiza la conversión del monto desde la moneda de origen a la moneda de destino.

### `guardar_en_historial_txt(monto, moneda_origen, moneda_destino, resultado)`
Guarda la conversión en el archivo historial.txt.

### `moneda_operaciones()`
Maneja la interfaz de usuario para seleccionar monedas y realizar conversiones.

## 📝 Ejemplo de Uso

```python
# Importar el módulo
from Actividad8 import moneda_operaciones

# Ejecutar el conversor
moneda_operaciones()
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:
1. Haz un fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`)
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva característica'`)
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT.