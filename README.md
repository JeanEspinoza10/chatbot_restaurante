# Proyecto Chatbot para Restaurante

Este proyecto tiene como objetivo implementar un Producto Mínimo Viable (MVP) para un chatbot destinado a un restaurante. El chatbot permitirá a los clientes interactuar con el restaurante a través de WhatsApp utilizando la API oficial de WhatsApp. La aplicación estará desarrollada utilizando la librería Flask de Python y almacenará la información en una base de datos PostgreSQL.

## Funcionalidades principales

1. **Interacción con clientes:** Los clientes podrán enviar mensajes al número de WhatsApp del restaurante para realizar consultas, hacer pedidos o reservar mesas.

2. **Menú del restaurante:** El chatbot proporcionará información sobre el menú del restaurante, los precios y las opciones disponibles.

3. **Realización de pedidos:** Los clientes podrán realizar pedidos a través del chatbot y recibir confirmaciones sobre el estado del pedido.

4. **Reserva de mesas:** Los clientes podrán reservar mesas para una fecha y hora específica.

5. **Información de contacto:** El chatbot proporcionará información de contacto del restaurante, como dirección, número de teléfono y horario de atención.

6. **Respuestas automáticas:** El chatbot responderá automáticamente a ciertas consultas comunes, como horarios de atención, ubicación y preguntas frecuentes.

## Tecnologías utilizadas

- Python: Lenguaje de programación principal para el desarrollo del chatbot.
- Flask: Framework web de Python para crear la aplicación y definir las rutas de la API.
- API de WhatsApp: Interfaz oficial proporcionada por WhatsApp para enviar y recibir mensajes.
- PostgreSQL: Sistema de gestión de bases de datos para almacenar la información relevante del chatbot.


## Procedimiento del Chatbot

El flujo del chatbot consta de los siguientes pasos:

1. El usuario inicia la conversación enviando un mensaje al número de WhatsApp integrado.
2. El bot responde con un mensaje de bienvenida y solicita al usuario que proporcione sus datos, como nombre, dirección y correo.
3. Después de recopilar los datos, el bot instruye al usuario a escribir una palabra clave para obtener la lista de menú.
4. El bot envía al usuario la lista de menú en forma de botones interactivos, aprovechando la funcionalidad de la API de WhatsApp.
5. Cuando el usuario selecciona un elemento del menú, el bot registra esa elección y verifica si el usuario confirma el pedido.
6. Si se confirma el pedido, el bot finaliza el proceso y proporciona una confirmación al usuario.

## Implementaciones Futuras

Además de las funcionalidades actuales, se considerarán las siguientes mejoras en el futuro:

- Modelado de la base de datos: Se explorará la posibilidad de almacenar y registrar el contexto de una conversación para una experiencia más personalizada.
- Método de Pago en Línea: Se implementará la opción de pago en línea para facilitar la finalización de los pedidos.
- Derivación a Operador Humano: Se añadirá una característica para derivar la conversación a un operador humano en situaciones específicas que requieran atención especializada.
