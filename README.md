# Creacion de una API web de ASP.NET Core para gestionar pizzas

¡API web de ASP.NET Core para gestionar pizzas! En este proyecto, sea desarrollado una API que te permitirá realizar operaciones CRUD (crear, leer, actualizar y eliminar) sobre pizzas almacenadas en una caché en memoria. 

## Tecnologías utilizadas

La API web está desarrollada en ASP.NET Core, un framework de desarrollo de aplicaciones web de alto rendimiento y escalabilidad, basado en .NET. Aprovechamos las características y ventajas que ofrece .NET para brindarte una experiencia de desarrollo eficiente y confiable.

## Funcionalidades principales

La API web de ASP.NET Core para gestionar pizzas te permite realizar las siguientes operaciones:

- **Crear una pizza**: Puedes enviar una solicitud HTTP POST para crear una nueva pizza en la caché. Proporciona los detalles de la pizza, como el nombre y si contiene gluten.

- **Leer una pizza**: Puedes realizar una solicitud HTTP GET para obtener información sobre una pizza específica. Simplemente proporciona el identificador único de la pizza y recibirás todos los detalles almacenados en la caché.

- **Actualizar una pizza**: Si necesitas realizar cambios en una pizza existente, puedes enviar una solicitud HTTP PUT con los nuevos datos. La API actualizará los detalles de la pizza en la caché.

- **Eliminar una pizza**: Si una pizza ya no es necesaria, puedes eliminarla enviando una solicitud HTTP DELETE con el identificador único de la pizza. La API eliminará la pizza correspondiente de la caché.

## Configuración del proyecto

Si deseas probar nuestra API web de gestión de pizzas, sigue los pasos a continuación para configurar el proyecto en tu entorno de desarrollo:

1. Asegúrate de tener instalado .NET Core SDK en tu máquina. Puedes descargarlo desde el sitio web oficial de .NET.

2. Clona este repositorio en tu máquina local o descárgalo como archivo ZIP.

3. Abre una terminal y navega hasta el directorio raíz del proyecto.

4. Ejecuta el comando `dotnet restore` para restaurar las dependencias del proyecto.

5. Ejecuta el comando `dotnet run` para compilar y ejecutar la aplicación.

6. La API web estará disponible en `http://localhost:5252/pizza/`. Puedes utilizar herramientas como Postman o cURL para interactuar con los endpoints.

## Ejecución de pruebas
Para ejecutar las pruebas en la API web, sigue los siguientes pasos:
1. Abre una terminal y navega hasta el directorio raíz del proyecto.
2. Ejecuta el comando `dotnet test` para ejecutar las pruebas.


