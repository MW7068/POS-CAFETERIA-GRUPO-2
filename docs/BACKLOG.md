# Product Backlog — POS Cafetería

**Product Owner:** Marcelo. **Estado:** propuesta inicial para acordar con el equipo.

## Objetivo propuesto

Permitir al personal de una cafetería registrar una venta y conocer su total de forma clara y verificable. Impuestos, descuentos, moneda, medios de pago e inventario requieren definición del Product Owner; no se asumen reglas numéricas.

## PBI propuestos

| ID | Historia / resultado propuesto | Responsable principal | Prioridad propuesta | Estado |
|---|---|---|---|---|
| PBI-01 | Como cajero, quiero calcular el total de los productos de una venta para informar el importe al cliente. | Brayan — Backend | Alta | Por refinar y aprobar |
| PBI-02 | Como responsable de la cafetería, quiero persistir productos y precios para disponer de un catálogo. | Alexander — DB/ORM | Alta | Por refinar y aprobar |
| PBI-03 | Como cajero, quiero una pantalla para seleccionar productos y visualizar el total de la venta. | Pedro Gonzalo — Frontend/UX | Alta | Por refinar y aprobar |
| PBI-04 | Como equipo, queremos pruebas y análisis estático en cada PR para detectar regresiones. | Cesar David — DevOps/QA | Alta | CI base preparado; completar política de calidad |
| PBI-05 | Como equipo, queremos una ejecución reproducible con Docker para facilitar la integración. | Cesar David — DevOps/QA | Media | Por refinar y aprobar |

## Refinamiento pendiente del PBI-01

- Precisar la entrada, salida y firma pública de la regla.
- Acordar qué ocurre con una venta vacía.
- Definir validaciones de cantidades y precios, tratamiento de decimales y errores.
- Acordar si descuentos e impuestos están fuera o dentro del primer incremento.
- Escribir ejemplos de aceptación con resultados esperados antes del código.
- Elegir la primera prueba RED con Backend y QA.

## Definition of Ready propuesta

- Historia y resultado comprensibles.
- Criterios de aceptación acordados por el PO.
- Datos de ejemplo y resultado esperado.
- Dependencias, responsable y alcance identificados.

## Definition of Done propuesta

- Criterios de aceptación comprobados por el Product Owner.
- Regla de negocio implementada con evidencia de RED/GREEN/REFACTOR.
- Pruebas de negocio presentes y aprobadas; Ruff sin errores.
- Revisión del PR y CI correctos; sin entornos, secretos o datos locales.
- Documentación de uso y pendientes actualizada.

Las definiciones se aprueban con el equipo. La estructura inicial no completa ningún PBI funcional.
