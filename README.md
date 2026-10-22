# POS Cafetería — Grupo 2

Base de trabajo del equipo para construir un punto de venta de cafetería con Python, TDD y colaboración mediante ramas y Pull Requests.

**Estado:** estructura inicial. La aplicación, base de datos, interfaz y Docker todavía no están implementados. El alcance de los PBI se acuerda con el Product Owner antes de desarrollar.

## Equipo y ramas

| Integrante | Rol | Rama de trabajo inicial |
|---|---|---|
| Marcelo | Product Owner / Scrum Master: backlog, tablero y coordinación de ramas | `docs/product-owner` |
| Brayan | Lead Backend Engineer: dominio y lógica con TDD | `feature/backend-tdd` |
| Alexander | Database & ORM Specialist: modelo de datos y persistencia | `feature/database-orm` |
| Pedro Gonzalo | Frontend & UX/UI Engineer: wireframes y requerimientos de usuario | `feature/frontend-ux` |
| Cesar David | DevOps & QA Engineer: CI/CD, Ruff y Docker | `chore/devops-qa` |

- `main`: base estable del proyecto.
- `develop`: integración del trabajo revisado del equipo.
- Ramas de rol: punto de partida para las primeras tareas; después se recomienda crear ramas por PBI desde `develop`.

Estas son convenciones de trabajo. Las restricciones de push, revisiones obligatorias y permisos de merge deben configurarse por separado en GitHub.

## Estructura inicial

```text
POS-CAFETERIA-GRUPO-2/
├── .github/
│   ├── pull_request_template.md
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── __init__.py
│   └── dominio/
│       ├── __init__.py
│       └── regla_negocio.py
├── tests/
│   ├── __init__.py
│   └── test_regla_negocio.py
├── docs/
│   ├── BACKLOG.md
│   └── EQUIPO_Y_FLUJO.md
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

`src/dominio/` contiene reglas puras: no debe importar un ORM, una base de datos ni una interfaz gráfica. La estructura inicial respeta los nombres de la imagen del laboratorio.

## Preparación local en Windows

Requiere Python 3.10 o superior y Git.

```powershell
git clone https://github.com/MW7068/POS-CAFETERIA-GRUPO-2.git
cd POS-CAFETERIA-GRUPO-2
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

En VS Code, abrir la carpeta del proyecto y seleccionar `.venv\Scripts\python.exe` con **Python: Select Interpreter**.

## Calidad y pruebas

```powershell
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m pytest -v
```

La plantilla aún **no contiene casos de prueba**: Pytest devuelve `no tests ran` y código de salida 5. No significa que haya pruebas aprobadas. El flujo inicial de CI informa esta situación y permite publicar el esqueleto, pero rechaza cualquier fallo real de pruebas o de Ruff. Cuando Backend incorpore los casos del primer PBI, QA debe quitar la excepción temporal del código 5 para exigir una suite no vacía.

## Flujo del equipo

1. Marcelo define y prioriza los PBI y sus criterios de aceptación en [`docs/BACKLOG.md`](docs/BACKLOG.md).
2. Cada integrante trabaja en su rama o en una rama de tarea desde `develop`.
3. Backend registra RED → GREEN → REFACTOR para las reglas de negocio.
4. Se ejecutan Pytest y Ruff y se abre un PR hacia `develop` con evidencia.
5. Otro integrante revisa y el Product Owner valida el resultado funcional.
6. Una entrega integrada y verificada se propone por PR de `develop` hacia `main`.

Instrucciones de ramas y tablero: [`docs/EQUIPO_Y_FLUJO.md`](docs/EQUIPO_Y_FLUJO.md).

## Próximo paso

Acordar el PBI-01 con el equipo antes de escribir su implementación. Las propuestas del backlog no representan funcionalidades terminadas ni decisiones de negocio aprobadas.
