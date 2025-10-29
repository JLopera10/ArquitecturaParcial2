# Tasks API – Arquitectura de Software Parcial Practico #2

- API desarrollada con **FastAPI** dedicada a la gestion sencilla de tareas, esta completamente integrada con docker para permitir que sea compatible en cualquier
entorno y que su ejecucion sea lo mas sencilla posible.  
Incluye algunos test unitarios con *pytest* para probar el funcionamiento de los endpoints y verificar que la logica funcione correctamente. 

---

## Requisitos previos
- Python | 3.11+
- Docker | 24+
- Docker Compose | 2.20+
- pip | 24+
- Archivo de Requisitos | requirements.txt
 
---

## Ejecución con Docker
- Construccion de la imagen
´´docker build -t tasks-api .´´
- Ejecucion del contenedor
´´docker run --rm -p 8000:8000 tasks-api´´

---

## Ejecución de los Tests
Esta app tiene tests con pytest, para verificar la API y la lógica, estos son los pasos para poder realizar ejecutar el test correctamente.
- Crear un ambiente virtual de python
´´python -m venv .venv´´
- Activar el ambiente virtual
´´source .venv/bin/activate´´
- Instalar las dependencias de la aplicacion
´´pip install -r requirements.txt´´
- Ejecutar el test
´´pytest -q´´

---

## Estructura de Capas de la Aplicacion
- Domain | Contiene los modelos y entidades del negocio (Pydantic models).
- Application | Define la lógica de negocio (servicios, casos de uso).
- Adapters | Contiene la API (controladores HTTP en FastAPI).

---

## Endpoints principales
- GET | /tasks | Obtiene todas las tareas
- POST | /tasks | Crea una nueva tarea
- GET | /tasks/{id} | Obtiene una tarea específica
- PUT | /tasks/{id} | Actualiza una tarea existente
- DELETE | /tasks/{id} | Elimina una tarea

---

## Ejemplo de Uso con Curl 
- Verificar funcionamiento de la API
  
  *curl -X GET http://127.0.0.1:8000/health*
  
- Crear una tarea
  
  *curl -X POST http://127.0.0.1:8000/tasks -H "Content-Type: application/json" -d '{"title": "Sesion Parcial #2", "description": "Estudiar para el segundo parcial de arquitectura", "status": "pending"}'*
  
- Listar todas las tareas
  
  *curl -X GET http://127.0.0.1:8000/tasks*
  
- Consultar una tarea por ID
  
  *curl -X GET http://127.0.0.1:8000/tasks/ID*

  (Reemplazar ID con el id de la tarea)
  
- Modificar el titulo/estado de una tarea
  
  *curl -X PUT http://127.0.0.1:8000/tasks/ID -H "Content-Type: application/json" -d '{"title": "Sesion Parcial #2", "status": "done"}'*

  (Reemplazar ID con el id de la tarea)
  
- Eliminar una tarea
  
  *curl -X DELETE http://127.0.0.1:8000/tasks/ID*

  (Reemplazar ID con el id de la tarea)
