
# Sistema de Gestión de Tareas con Django y PostgreSQL

Creado por Carlos Santiago Marcelino


## API Reference

#### Listado de tareas

```http
  GET /api/tasks/
```

#### Crear tarea

```http
  POST /api/tasks/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. Titulo de la tarea |
| `email`      | `string` | **Required**. Email del autor |
| `description`      | `string` | **Required**. Descripción de la tarea |

#### Actualizar tarea

```http
  PUT /api/tasks/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. Titulo de la tarea |
| `email`      | `string` | **Required**. Email del autor |
| `description`      | `string` | **Required**. Descripción de la tarea |

#### Borrar tarea

```http
  DELETE /api/tasks/{id}
```

#### Obtener token

```http
  POST /api/tastoken/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. Usuario |
| `password`      | `string` | **Required**. Contraseña |

## Authors

- [@Carlos Santiago](https://github.com/csantiago-25)
