FROM python:3.9-slim

WORKDIR /opt/python

# Instalar las dependencias en /opt/python
RUN pip install requests boto3 -t .

# Copiar el contenido de /opt a la carpeta /out
CMD ["bash", "-c", "mkdir -p /out/python && cp -r . /out/python"]
