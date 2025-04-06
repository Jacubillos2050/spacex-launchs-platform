# Construcción de la app
FROM node:18-alpine AS builder

# Establece el directorio de trabajo 
WORKDIR /app

# Copiar dependencias e instalar
COPY package*.json ./
RUN npm install

# Copiar el resto del código fuente y construir la app
COPY . .
RUN npm run build

# Etapa 2: Crear la imagen final que sirve el frontend con NGINX
FROM nginx:alpine

# Copiar los archivos estáticos del build a la carpeta pública de NGINX
COPY --from=builder /app/build /usr/share/nginx/html

# redirigir a index.html
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exponer el puerto 80 para que ECS/ALB puedan acceder
EXPOSE 80

# Iniciar NGINX en modo "foreground"
CMD ["nginx", "-g", "daemon off;"]
