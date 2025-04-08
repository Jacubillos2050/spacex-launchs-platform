# SpaceX Launch Platform Frontend 🚀

## Descripción

Este repositorio contiene el frontend de la plataforma de lanzamiento de SpaceX. Proporciona una interfaz de usuario moderna y receptiva que permite a los usuarios interactuar con datos relacionados con lanzamientos espaciales, como detalles de misiones, fechas y estadísticas clave.

Características principales:
- Interfaz intuitiva y amigable.
- Datos obtenidos desde un backend conectado a AWS.
- Compatible con múltiples navegadores.

## Requisitos Previos

Asegúrate de tener instalado lo siguiente:

- Node.js (v18+)
- npm o yarn
- Docker 
- Cuenta de AWS configurada

Enlace al repositorio del backend: https://fqt3vp3zx3.execute-api.us-east-1.amazonaws.com/dev/launches
Front react y bootstrap:      http://spacex-frontend-alb-575070819.us-east-1.elb.amazonaws.com/ 

## Instalación

1. Clona este repositorio:

   git clone https://github.com/Jacubillos2050/spacex-launchs-platform.git

   cd spacex-launch-platform-frontend

1. Estar dentro de tu entorno virtual 
  python3 -m venv venv

2.  luego activarlo
  source venv/bin/activate

3. Instal dependencias
pip install -r requirements-dev.txt

4. PYTHONPATH=. coverage run -m pytest lambdafn/tests
coverage report -m

## Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

Email: jcubillosvillamil@gmail.com.co
GitHub: @Jacubillos2050
LinkedIn: www.linkedin.com/in/jairo-cubillos