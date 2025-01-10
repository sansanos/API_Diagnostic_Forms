# Proyecto Formulario de Solicitud Médica - Backend

***Elaborado por Santiago Sánchez Ospina***

Este proyecto tiene como propósito desarrollar una solución de automatización para probar la API del formulario de solicitud médica empleando la biblioteca requests en Python. El objetivo principal es validar las funcionalidades del backend, asegurando que las solicitudes y respuestas cumplan con los criterios de aceptación definidos.

Sobre la API:

La API del formulario de solicitud médica permite enviar datos como: datos personales, del médico remitente y los detalles de las pruebas solicitadas al laboratorio. Esta API implementa validaciones para garantizar la integridad y correcta estructuración de los datos antes de procesarlos.

Documentación de la API:

Puedes acceder a la documentación completa de la API en:

- URL del backend: https://dev.iqviatech.com:5005/docs

Proceso

El flujo automatizado se basa en el envío de solicitudes HTTP a el endpoint "/diagnostic_form/" validando de las respuestas recibidas. 

Para estructurar las pruebas, se sigue este proceso:

- Definir datos de prueba: Crear cuerpos de solicitud con diferentes combinaciones de datos para validar el comportamiento de la API.
- Enviar solicitudes HTTP: Utilizar la biblioteca requests para realizar peticiones POST al endpoint de creación de envio de formulario diligenciado.
- Validar respuestas: Verificar los códigos de respuesta HTTP y el contenido de las respuestas, asegurando que coincidan con los criterios esperados.

Pasos para ejecutar las pruebas

- Instalar las dependencias necesarias:
        Usando pip:

    pip install requests

    pip install pytest

Ejecutar las pruebas:

- Para correr todas las pruebas: pytest

- Para pruebas específicas: pytest test_api.py


