#!/bin/bash

mkdir -p .dynamodb
cd .dynamodb

echo "Descargando DynamoDB Local (ZIP)..."
wget https://s3.us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.zip

echo "Extrayendo..."
unzip dynamodb_local_latest.zip

echo "Limpieza..."
rm dynamodb_local_latest.zip

cd ..
echo "✅ DynamoDB Local instalado en .dynamodb/"
