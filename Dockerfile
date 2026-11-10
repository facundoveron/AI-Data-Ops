
# Imagen base de Python 3.10
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /workspace

# Evitar archivos .pyc y habilitar logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Actualizar paquetes del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/

# Copiar los archivos del proyecto
COPY . .

# Comando por defecto
CMD ["python"]
