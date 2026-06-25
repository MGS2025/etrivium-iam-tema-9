# Tema 9 — Checklist de Validación

> **Título oficial**: Ley 31/1995 (LPRL): Delegados de Prevención. Comités de Seguridad y Salud. PRL en el Acuerdo-Convenio del Ayuntamiento de Madrid. Representación de los empleados públicos.
> **Versión**: 1.0 — Generación inicial
> **Fecha**: 2026-06-25
> **Revisoras**: María + Ana (IAM)

---

## Cómo usar este checklist

- **OK** → el criterio se cumple sin cambios.
- **REVISAR** → necesita ajuste o aclaración (indicar qué).
- **NO** → no se cumple o es incorrecto. Justificar.

---

## 1. Fuentes y trazabilidad

- [ ] La fuente nuclear es la **LPRL (Ley 31/1995)** en su versión consolidada.
- [ ] Los datos del **Acuerdo-Convenio 2019-2022** se han verificado en fuente oficial (transparencia.madrid.es, art. 48).
- [ ] Cada afirmación que reproduce el articulado está referenciada (`[LPRL, art. X]`, `[TREBEP, art. X]`, `[ET, art. X]`, `[AC1922, art. X]`).
- [ ] Cada pregunta del banco y de los casos puede reconducirse a un artículo concreto.

## 2. Estructura del contenido

- [ ] El `tema-9-indice.md` refleja fielmente la estructura de `tema-9-contenido.md` (11 secciones).
- [ ] Las secciones cubren: LPRL (marco/principios), Delegados de Prevención (designación, competencias, garantías), Comité de Seguridad y Salud, servicios de prevención, PRL en el Acuerdo-Convenio y representación de los empleados públicos (TREBEP/ET).
- [ ] Los conceptos memorizables aparecen como `[DATO CLAVE EXAMEN]`.
- [ ] Las reproducciones del articulado aparecen como `[CITA NORMATIVA]` / `[CITA CONSTITUCIONAL]`.
- [ ] Los datos del Ayto de Madrid / IAM están marcados como `[EJEMPLO AYTO MADRID]`.

## 3. Rigor jurídico (datos sensibles)

- [ ] Fundamento constitucional: **art. 40.2 CE** (no confundir con el art. 43 —salud— ni el 35.1 —derecho al trabajo—).
- [ ] Origen comunitario: **Directiva 89/391/CEE** (Directiva Marco).
- [ ] Delegados de Prevención: **designados por y entre** los representantes del personal (art. 35.1); representación de segundo grado.
- [ ] Escala del art. 35.2: **hasta 30 → Delegado de Personal; 31-49 → 1; 50-100 → 2; … 4.001 en adelante → 8** (máximo).
- [ ] Competencias (art. 36.1) vs. facultades (art. 36.2): no intercambiarlas. Plazo de informe en consulta: **15 días** (art. 36.3).
- [ ] Garantías: **art. 68 ET** (remisión del art. 37.1); **sigilo profesional** (art. 37.3). El tiempo de reuniones del Comité y visitas de acompañamiento **no se imputa** al crédito (art. 37.1).
- [ ] Comité de Seguridad y Salud: **paritario y colegiado** (art. 38.1); umbral **50** (art. 38.2); **trimestral** (art. 38.3); competencias del art. 39.
- [ ] Servicios de prevención: asunción por el empresario, trabajador designado, propio, ajeno y mancomunado (arts. 30-31).
- [ ] **Acuerdo-Convenio**: **83 Delegados de Prevención** (Ayto 56, Empleo 4, Tributaria 7, **IAM 6**, Madrid Salud 7, Actividades 3); **Comité único 15+15**; **crédito 40 h/mes** adicional [art. 48]. Plan de PRL: **Acuerdo de 26/11/2020** (BOAM 8783).
- [ ] **TREBEP**: Delegados de Personal (**1** hasta 30, **3** de 31 a 49) y Junta de Personal (≥50) [art. 39]; garantías [art. 41]; reunión: **40 %** y **48 h** [art. 46].
- [ ] **ET**: Delegados de Personal (6-49) y Comité de Empresa (≥50) [arts. 62-63].

## 4. Diagramas SVG

- [ ] Los 12 diagramas están presentes en `tema-9-diagramas.md`.
- [ ] Cada diagrama incluye `role="img"` y `aria-label` descriptivo.
- [ ] Paleta coherente: Ayto Madrid #0055a0 + #d13c3c + #2d8659 + #e89822.
- [ ] Ningún diagrama depende de CDN, fuentes externas ni scripts.
- [ ] Verificado por render del `index.html` real (los 12 SVG juntos): 0 textos fuera de caja (CSS scoped).

## 5. Banco de 150 preguntas

- [ ] Las 150 preguntas tienen 3 opciones y una única respuesta correcta verificable.
- [ ] La distribución A/B/C está equilibrada (~50/50/50) tras el balanceo automático.
- [ ] No hay preguntas ambiguas.
- [ ] La sección pedagógica de 20 preguntas incluye explicación y referencia.

## 6. Casos prácticos

- [ ] Los 6 casos mantienen escenario del Ayto de Madrid / IAM.
- [ ] Las cuestiones de cada caso suman 10 puntos.
- [ ] Cada caso tiene solución orientativa y criterios de evaluación.

## 7. Nivel y adecuación al C1

- [ ] Nivel de profundidad adecuado para C1.
- [ ] Se priorizan los datos memorísticos (escalas, umbrales, plazos, crédito horario).

## 8. Entregables HTML

- [ ] `index.html` autosuficiente (offline), con pestañas y motor de test con penalización 1/3.
- [ ] Imprimible a PDF.
- [ ] Branding Ayuntamiento de Madrid (#0055a0).

## 9. Consistencia inter-temas

- [ ] Referencia cruzada al **Tema 5** (TREBEP, derechos colectivos y negociación) coherente.
- [ ] Referencia al **Tema 1** (art. 40.2 CE y libertad sindical) coherente.
- [ ] Referencia a los **Temas 2-4** (organización del Ayto y Organismos Autónomos) coherente.

---

## Observaciones generales

### Decisiones conscientes que conviene confirmar

1. **Punto 5.3 del índice del cliente — "Comisión Paritaria de Seguridad y Salud"**: el texto del Acuerdo-Convenio **no contempla un órgano con ese nombre específico**. El órgano real de participación en PRL es el **Comité de Seguridad y Salud único y paritario (15+15)** del art. 48, y el seguimiento general del Acuerdo-Convenio corresponde a la **Comisión de Seguimiento/Paritaria del propio Acuerdo-Convenio** (no específica de PRL). → Confirmar con Jesús / María si se mantiene el desarrollo del Comité único como órgano central (recomendado) o se desea un epígrafe específico sobre la Comisión de Seguimiento.
2. **Datos del Acuerdo-Convenio verificados en fuente oficial** (art. 48, transparencia.madrid.es): 83 delegados, reparto por organismo (IAM 6), Comité único 15+15 y crédito de 40 h/mes. → Confirmar que el texto en vigor sigue siendo el 2019-2022 prorrogado en la fecha de la convocatoria.
3. **Estructura del Capítulo IX** (arts. 45-52) tomada del sumario oficial. → Confirmar que el enunciado del examen no exige el detalle literal de los arts. 49-52 (adaptaciones, edificios, autoprotección, medio ambiente), aquí tratados como referencia.
4. **150 preguntas + 20 pedagógicas + 6 casos + 12 diagramas + 8 pestañas**, replicando el formato de los Temas 1-8.

### Puntos a vigilar (datos volátiles)

- El **número de delegados por organismo**, el **crédito horario** y la **composición del Comité** proceden del Acuerdo-Convenio 2019-2022. Un **nuevo Acuerdo-Convenio** podría modificarlos: reverificar antes de cada convocatoria.
- La **escala del art. 35.2 LPRL** y los **umbrales del TREBEP/ET** son estables (norma estatal), pero conviene confirmar que no ha habido reforma puntual.

---

## Decisión de cierre

- [ ] Aprobado sin cambios.
- [ ] Aprobado con cambios menores (listarlos).
- [ ] Requiere v2 (listar cambios sustanciales).

**Firmas**:

- María: _______________________________ Fecha: _____________
- Ana: _______________________________ Fecha: _____________
