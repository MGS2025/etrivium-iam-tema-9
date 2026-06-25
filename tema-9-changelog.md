# Tema 9 — Changelog

> **Título oficial**: Ley 31/1995 (LPRL): Delegados de Prevención. Comités de Seguridad y Salud. PRL en el Acuerdo-Convenio del Ayuntamiento de Madrid. Representación de los empleados públicos.

---

## v1.0 — 2026-06-25 — Generación inicial completa

**Estado**: Pendiente de validación por María / Ana (IAM).

### Alcance y decisiones

- **Fuentes nucleares**: **LPRL (Ley 31/1995)**, **TREBEP (RDLeg 5/2015)**, **ET (RDLeg 2/2015)** y **Acuerdo-Convenio 2019-2022** del Ayuntamiento de Madrid (versiones consolidadas / texto oficial).
- **Material del cliente**: `TEMA_09.docx` (índice oficial del tema, 7 bloques).
- **Verificación previa en fuente oficial**: antes de redactar se verificaron los datos del Acuerdo-Convenio (art. 48) en `transparencia.madrid.es`.

### Datos del Acuerdo-Convenio verificados (fuente oficial)

1. **83 Delegados de Prevención** en el conjunto del Ayuntamiento y sus Organismos Autónomos: Ayuntamiento 56, Agencia para el Empleo 4, Agencia Tributaria Madrid 7, **IAM 6**, Madrid Salud 7, Agencia de Actividades 3 [AC1922, art. 48].
2. **Comité de Seguridad y Salud único y paritario**: 15 Delegados de Prevención + 15 representantes de la Administración.
3. **Crédito horario de 40 horas mensuales** retribuidas por delegado, adicional al crédito sindical general; el tiempo de reuniones del Comité y de visitas computa como trabajo efectivo.
4. **Estructura del Capítulo IX** (arts. 45-52): 45 salud laboral, 46 servicio de prevención, 47 recursos económicos, 48 representación del personal municipal, 49 adaptaciones de puesto, 50 edificios e instalaciones, 51 planes de autoprotección, 52 medio ambiente.
5. **Plan de Prevención de Riesgos Laborales** del Ayuntamiento aprobado por **Acuerdo de 26/11/2020** (BOAM 8783).

### Discrepancia detectada con el índice del cliente

- El punto **5.3** del índice (`TEMA_09.docx`) cita una **"Comisión Paritaria de Seguridad y Salud"** como órgano de seguimiento del Acuerdo-Convenio en materia de PRL. **El Acuerdo-Convenio no contempla un órgano con ese nombre específico**: el órgano de participación en PRL es el **Comité de Seguridad y Salud único (art. 48)**, y el seguimiento general del Acuerdo-Convenio corresponde a la **Comisión de Seguimiento/Paritaria del propio Acuerdo-Convenio** (no específica de PRL). Se ha desarrollado el **Comité de Seguridad y Salud único** como órgano real y se ha anotado la discrepancia para confirmación con Jesús / María (ver `tema-9-fuentes.md` y `tema-9-validacion.md`).

### Precisiones jurídicas aplicadas

1. **Designación de los Delegados de Prevención**: subrayado que son **designados por y entre** los representantes del personal (representación de segundo grado), no elegidos directamente [art. 35.1].
2. **Escala del art. 35.2**: reproducida íntegra (hasta 30 → Delegado de Personal; 31-49 → 1; …; 4.001 en adelante → 8), que el índice solo enunciaba como "escala según número de trabajadores".
3. **Competencias vs. facultades** (art. 36): separadas expresamente para evitar la confusión clásica de examen.
4. **Crédito horario** (art. 37.1): precisado que el tiempo de las reuniones del Comité y de las visitas de acompañamiento **no se imputa** al crédito.
5. **Comité de Seguridad y Salud**: fijados el umbral de **50** (art. 38.2), la **paridad** y las reuniones **trimestrales** (art. 38.3).
6. **Representación TREBEP/ET**: añadidos los tramos concretos (Delegados de Personal 1/3; Junta de Personal ≥50; Comité de Empresa ≥50) y el detalle del **derecho de reunión** (40 % y 48 h, art. 46), que el índice mencionaba de forma genérica.

### Entregables generados

| Fichero | Contenido |
|---|---|
| `tema-9-indice.md` | Índice de 11 secciones + tablas de datos clave |
| `tema-9-fuentes.md` | Registro Tier 1/2/3 + datos verificados en fuente oficial |
| `tema-9-contenido.md` | Contenido teórico (11 secciones, callouts) |
| `tema-9-diagramas.md` | 12 diagramas SVG accesibles |
| `tema-9-test.md` | 150 preguntas + 20 pedagógicas |
| `tema-9-caso-practico.md` | 6 casos prácticos (Ayto de Madrid / IAM), 10 pts c/u |
| `tema-9-validacion.md` | Checklist de validación |
| `index.html` | Web autosuficiente, pestañas, motor test 1/3 |

### QA aplicado

- Datos del Acuerdo-Convenio contrastados con fuente oficial (transparencia.madrid.es) antes de la redacción.
- Diagramas con CSS **scoped** por SVG (evita el bug sistémico de colisión de estilos entre los 12 SVG) y verificados por render del `index.html` real.
- Balanceo automático A/B/C de las respuestas del test.
- Refs cruzadas verificadas vs BOAM 10.032 (T1, T2-T4, T5).

### Pendiente

- Validación de contenido por María / Ana (IAM).
- Confirmar el tratamiento del punto 5.3 (Comité único vs. "Comisión Paritaria de Seguridad y Salud").
- Confirmar la vigencia del Acuerdo-Convenio 2019-2022 (prorrogado) en la fecha de la convocatoria.
