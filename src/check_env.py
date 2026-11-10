
import sys
import os

# Mostrar la versión de Python instalada
print("Versión de Python:")
print(sys.version)

# Mostrar la versión de forma resumida
print("\nVersión resumida:")
print(sys.version_info)

# Verificar acceso a variables de entorno
print("\nAcceso a variables de entorno:")

# Obtener una variable de entorno
python_path = os.environ.get("PATH")

if python_path:
    print("PATH:", python_path)
    print("Acceso a variables de entorno: CORRECTO")
else:
    print("No se pudo acceder a PATH")
