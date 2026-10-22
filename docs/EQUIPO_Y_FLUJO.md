# Organización del equipo y flujo Git

## Ramas iniciales

| Rama | Propósito / responsable |
|---|---|
| `main` | Entregas estables |
| `develop` | Integración del equipo |
| `docs/product-owner` | Marcelo: backlog, tablero y coordinación |
| `feature/backend-tdd` | Brayan: dominio y lógica con TDD |
| `feature/database-orm` | Alexander: modelos de datos y persistencia |
| `feature/frontend-ux` | Pedro Gonzalo: requerimientos, wireframes e interfaz |
| `chore/devops-qa` | Cesar David: CI, calidad y futura configuración Docker |

Al crearse, todas parten del mismo commit de estructura inicial. Los nombres identifican responsabilidades, pero no restringen automáticamente quién puede escribir en cada rama.

## Incorporarse a una rama desde VS Code

1. Clonar el repositorio y abrir su carpeta.
2. Ejecutar `git fetch origin`.
3. Seleccionar la rama remota asignada en el selector de ramas de VS Code; Git creará su seguimiento local.

Ejemplo para Backend:

```powershell
git switch --track origin/feature/backend-tdd
```

Si la rama local ya existe:

```powershell
git switch feature/backend-tdd
git pull --ff-only
```

## Trabajar por PBI

Después de las tareas iniciales, crear una rama por PBI desde `develop` actualizado. Ejemplo de nombre: `feature/pbi-01-total-venta`. Acordar primero la firma de las reglas para evitar incompatibilidades entre Backend, DB e interfaz.

Mensajes sugeridos:

```text
test: (RED) describir el comportamiento pendiente
feat: (GREEN) implementar el minimo para pasar la prueba
refactor: (REFACTOR) mejorar diseño sin cambiar comportamiento
docs: precisar criterios de aceptacion del PBI-01
ci: verificar pruebas y ruff en los pull requests
```

Cada PR de tarea se dirige a `develop`, incluye evidencia y recibe revisión. Las entregas verificadas pasan de `develop` a `main` por un PR independiente.

## Trabajo del Product Owner

- Completar y aprobar las historias de `BACKLOG.md`.
- Acordar con cada integrante el primer PBI y sus criterios de aceptación.
- Mantener prioridades y dependencias y validar demostraciones funcionales.
- Proponer en GitHub Projects un tablero con columnas: Backlog, Ready, In Progress, Review y Done.
- Crear o vincular una Issue por PBI y asignar responsable y prioridad.

El tablero, las Issues, las invitaciones a colaboradores y las reglas de protección todavía requieren configuración en GitHub. No quedan creados por publicar estas ramas.

## Revisión y permisos

El propietario del repositorio debe invitar a los colaboradores y acordar quién está autorizado a fusionar PR. Para aplicar el flujo, configurar reglas de protección de `main` y `develop` que exijan revisión y el check de CI. La creación de ramas por sí sola no activa esa protección.
