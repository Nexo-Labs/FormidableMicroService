FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app


# Instala las dependencias necesarias
RUN pip install flask requests

# Copia el script Python al contenedor
COPY notion_flask_app.py .

# Expone el puerto 5000 para acceder a la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "notion_flask_app.py"]