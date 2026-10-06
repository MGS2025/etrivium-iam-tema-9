# Tema 9 — Catálogo de Diagramas

> **Título oficial**: Ley 31/1995 (LPRL): Delegados de Prevención, Comités de Seguridad y Salud, PRL en el Acuerdo-Convenio del Ayuntamiento de Madrid y representación de los empleados públicos.
>
> **Versión**: 1.0 — generación inicial
> **Fecha**: 2026-06-25
> **Formato**: SVG inline (zero-dependencias, escalable, imprimible)
> **Paleta**: Ayuntamiento de Madrid #0055a0 (primario) + #d13c3c (alertas) + #2d8659 (ventajas) + #e89822 (callouts)

---

## Índice de diagramas

| ID  | Título                                                  | Sección | Tipo |
|-----|---------------------------------------------------------|---------|------|
| D1  | El marco de la prevención de riesgos laborales         | § 1     | Esquema |
| D2  | Los principios de la acción preventiva (art. 15)       | § 2     | Lista |
| D3  | Escala de Delegados de Prevención (art. 35.2)          | § 3     | Tabla |
| D4  | Delegados de Prevención: competencias y facultades     | § 4     | Comparativa |
| D5  | Garantías y sigilo del Delegado de Prevención (art. 37)| § 5     | Esquema |
| D6  | El Comité de Seguridad y Salud (arts. 38-39)           | § 6     | Esquema |
| D7  | Modalidades de servicio de prevención (arts. 30-31)    | § 7     | Árbol |
| D8  | Capítulo IX del Acuerdo-Convenio (arts. 45-52)         | § 8     | Esquema |
| D9  | Los 83 Delegados de Prevención del Ayto de Madrid      | § 8     | Barras |
| D10 | Representación: funcionarios vs. laborales (umbral 50) | § 9     | Comparativa |
| D11 | El derecho de reunión (art. 46 TREBEP)                 | § 10    | Flujo |
| D12 | Mapa de integración del Tema 9                          | § 11    | Mapa conceptual |

---

## D1 · El marco de la prevención de riesgos laborales

**Sección**: § 1 — Introducción
**Propósito**: Situar la LPRL bajo su fundamento constitucional (art. 40.2 CE) y su origen comunitario (Directiva Marco).

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 330" role="img" aria-label="El artículo 40.2 de la Constitución y la Directiva 89/391 CEE fundamentan la Ley 31/1995 de Prevención de Riesgos Laborales, que se aplica también a las Administraciones Públicas">
  <style>
    .h{font:700 14px system-ui,sans-serif;fill:#fff;text-anchor:middle}
    .t{font:13px system-ui,sans-serif;fill:#1a1a1a;text-anchor:middle}
    .s{font:11px system-ui,sans-serif;fill:#555;text-anchor:middle}
  </style>
  <rect x="60" y="20" width="270" height="60" rx="8" fill="#003d75"/>
  <text x="195" y="45" class="h">Art. 40.2 CE</text>
  <text x="195" y="65" class="h" style="font-weight:400;font-size:11px">velar por la seguridad e higiene</text>
  <rect x="370" y="20" width="270" height="60" rx="8" fill="#003d75"/>
  <text x="505" y="45" class="h">Directiva 89/391/CEE</text>
  <text x="505" y="65" class="h" style="font-weight:400;font-size:11px">Directiva Marco (UE)</text>
  <line x1="195" y1="80" x2="350" y2="105" stroke="#0055a0" stroke-width="1.5"/>
  <line x1="505" y1="80" x2="350" y2="105" stroke="#0055a0" stroke-width="1.5"/>
  <rect x="190" y="108" width="320" height="62" rx="8" fill="#0055a0"/>
  <text x="350" y="133" class="h">LPRL · Ley 31/1995, de 8 de noviembre</text>
  <text x="350" y="155" class="h" style="font-weight:400;font-size:11px">norma básica de seguridad y salud en el trabajo</text>
  <line x1="350" y1="170" x2="350" y2="185" stroke="#0055a0" stroke-width="1.5"/>
  <rect x="120" y="186" width="220" height="56" rx="8" fill="#e8f5ee" stroke="#2d8659"/>
  <text x="230" y="208" class="t" style="font-weight:700">Relaciones laborales</text>
  <text x="230" y="227" class="s">Estatuto de los Trabajadores</text>
  <rect x="360" y="186" width="220" height="56" rx="8" fill="#e8f5ee" stroke="#2d8659"/>
  <text x="470" y="208" class="t" style="font-weight:700">Administraciones Públicas</text>
  <text x="470" y="227" class="s">art. 3.1: también funcionarios</text>
  <rect x="160" y="262" width="380" height="50" rx="8" fill="#fff5e6" stroke="#e89822"/>
  <text x="350" y="284" class="s" style="font-weight:700;fill:#b5740f">Objeto: promover la seguridad y la salud</text>
  <text x="350" y="301" class="s">prevención de los riesgos derivados del trabajo (art. 2.1)</text>
</svg>
```

---

## D2 · Los principios de la acción preventiva (art. 15)

**Sección**: § 2 — Principios de la acción preventiva
**Propósito**: Enumerar los nueve principios del art. 15.1 LPRL en su orden legal.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 380" role="img" aria-label="Los nueve principios de la acción preventiva del artículo 15: evitar riesgos, evaluar los no evitables, combatir en origen, adaptar el trabajo a la persona, evolución técnica, sustituir lo peligroso, planificar, anteponer la protección colectiva a la individual y dar instrucciones">
  <style>
    .ti{font:700 15px system-ui,sans-serif;fill:#0055a0;text-anchor:middle}
    .t{font:12px system-ui,sans-serif;fill:#1a1a1a}
    .n{font:700 12px system-ui,sans-serif;fill:#fff;text-anchor:middle}
  </style>
  <text x="350" y="28" class="ti">Principios de la acción preventiva — art. 15.1 LPRL</text>
  <g>
    <circle cx="40" cy="58" r="13" fill="#2d8659"/><text x="40" y="62" class="n">a</text>
    <text x="62" y="62" class="t" style="font-weight:700">Evitar los riesgos</text>
    <circle cx="40" cy="92" r="13" fill="#0055a0"/><text x="40" y="96" class="n">b</text>
    <text x="62" y="96" class="t">Evaluar los riesgos que no se puedan evitar</text>
    <circle cx="40" cy="126" r="13" fill="#0055a0"/><text x="40" y="130" class="n">c</text>
    <text x="62" y="130" class="t">Combatir los riesgos en su origen</text>
    <circle cx="40" cy="160" r="13" fill="#0055a0"/><text x="40" y="164" class="n">d</text>
    <text x="62" y="164" class="t">Adaptar el trabajo a la persona</text>
    <circle cx="40" cy="194" r="13" fill="#0055a0"/><text x="40" y="198" class="n">e</text>
    <text x="62" y="198" class="t">Tener en cuenta la evolución de la técnica</text>
    <circle cx="40" cy="228" r="13" fill="#0055a0"/><text x="40" y="232" class="n">f</text>
    <text x="62" y="232" class="t">Sustituir lo peligroso por lo de poco o ningún peligro</text>
    <circle cx="40" cy="262" r="13" fill="#0055a0"/><text x="40" y="266" class="n">g</text>
    <text x="62" y="266" class="t">Planificar la prevención</text>
    <circle cx="40" cy="296" r="13" fill="#2d8659"/><text x="40" y="300" class="n">h</text>
    <text x="62" y="300" class="t" style="font-weight:700">Anteponer la protección colectiva a la individual</text>
    <circle cx="40" cy="330" r="13" fill="#0055a0"/><text x="40" y="334" class="n">i</text>
    <text x="62" y="334" class="t">Dar las debidas instrucciones a los trabajadores</text>
  </g>
  <rect x="30" y="352" width="640" height="22" rx="6" fill="#fff5e6" stroke="#e89822"/>
  <text x="40" y="368" class="t" style="fill:#b5740f;font-weight:700">Clave: «evitar» es el primero · solo se evalúa lo que no se ha podido evitar · colectiva &gt; individual</text>
</svg>
```

---

## D3 · Escala de Delegados de Prevención (art. 35.2)

**Sección**: § 3 — Delegados de Prevención: designación
**Propósito**: Escala que relaciona el número de trabajadores con el de Delegados de Prevención.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 380" role="img" aria-label="Escala del artículo 35.2: hasta 30 trabajadores el Delegado de Personal; de 31 a 49 uno; de 50 a 100 dos; de 101 a 500 tres; de 501 a 1000 cuatro; de 1001 a 2000 cinco; de 2001 a 3000 seis; de 3001 a 4000 siete; de 4001 en adelante ocho">
  <style>
    .ti{font:700 15px system-ui,sans-serif;fill:#0055a0;text-anchor:middle}
    .t{font:12px system-ui,sans-serif;fill:#1a1a1a}
    .h{font:700 12px system-ui,sans-serif;fill:#fff;text-anchor:middle}
    .n{font:700 14px system-ui,sans-serif;fill:#0055a0;text-anchor:middle}
  </style>
  <text x="350" y="26" class="ti">Escala de Delegados de Prevención (art. 35.2 LPRL)</text>
  <rect x="60" y="42" width="430" height="26" fill="#0055a0"/>
  <text x="275" y="60" class="h">Número de trabajadores</text>
  <rect x="490" y="42" width="150" height="26" fill="#0055a0"/>
  <text x="565" y="60" class="h">Delegados</text>
  <g class="t">
    <rect x="60" y="68" width="430" height="30" fill="#e8f5ee" stroke="#cfe6da"/><text x="72" y="88">Hasta 30 (el Delegado de Personal)</text>
    <rect x="490" y="68" width="150" height="30" fill="#e8f5ee" stroke="#cfe6da"/><text x="565" y="88" class="n" style="fill:#2d8659">DP</text>
    <rect x="60" y="98" width="430" height="30" fill="#fff" stroke="#e3e8ef"/><text x="72" y="118">De 31 a 49</text>
    <rect x="490" y="98" width="150" height="30" fill="#fff" stroke="#e3e8ef"/><text x="565" y="118" class="n">1</text>
    <rect x="60" y="128" width="430" height="30" fill="#f5f8fc" stroke="#e3e8ef"/><text x="72" y="148">De 50 a 100</text>
    <rect x="490" y="128" width="150" height="30" fill="#f5f8fc" stroke="#e3e8ef"/><text x="565" y="148" class="n">2</text>
    <rect x="60" y="158" width="430" height="30" fill="#fff" stroke="#e3e8ef"/><text x="72" y="178">De 101 a 500</text>
    <rect x="490" y="158" width="150" height="30" fill="#fff" stroke="#e3e8ef"/><text x="565" y="178" class="n">3</text>
    <rect x="60" y="188" width="430" height="30" fill="#f5f8fc" stroke="#e3e8ef"/><text x="72" y="208">De 501 a 1.000</text>
    <rect x="490" y="188" width="150" height="30" fill="#f5f8fc" stroke="#e3e8ef"/><text x="565" y="208" class="n">4</text>
    <rect x="60" y="218" width="430" height="30" fill="#fff" stroke="#e3e8ef"/><text x="72" y="238">De 1.001 a 2.000</text>
    <rect x="490" y="218" width="150" height="30" fill="#fff" stroke="#e3e8ef"/><text x="565" y="238" class="n">5</text>
    <rect x="60" y="248" width="430" height="30" fill="#f5f8fc" stroke="#e3e8ef"/><text x="72" y="268">De 2.001 a 3.000</text>
    <rect x="490" y="248" width="150" height="30" fill="#f5f8fc" stroke="#e3e8ef"/><text x="565" y="268" class="n">6</text>
    <rect x="60" y="278" width="430" height="30" fill="#fff" stroke="#e3e8ef"/><text x="72" y="298">De 3.001 a 4.000</text>
    <rect x="490" y="278" width="150" height="30" fill="#fff" stroke="#e3e8ef"/><text x="565" y="298" class="n">7</text>
    <rect x="60" y="308" width="430" height="30" fill="#fdeaea" stroke="#f3cccc"/><text x="72" y="328" style="font-weight:700">De 4.001 en adelante (máximo)</text>
    <rect x="490" y="308" width="150" height="30" fill="#fdeaea" stroke="#f3cccc"/><text x="565" y="328" class="n" style="fill:#d13c3c">8</text>
  </g>
  <text x="350" y="360" class="t" style="text-anchor:middle;fill:#555">Designados por y entre los representantes del personal (art. 35.2)</text>
</svg>
```

---

## D4 · Delegados de Prevención: competencias y facultades

**Sección**: § 4 — Competencias y facultades (art. 36)
**Propósito**: Separar las competencias (qué hacen) de las facultades (con qué medios).

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 340" role="img" aria-label="Competencias del artículo 36.1: colaborar, promover, ser consultados y vigilar. Facultades del 36.2: acompañar, acceder a información, ser informados, recibir información, realizar visitas, recabar medidas y proponer la paralización">
  <style>
    .h{font:700 14px system-ui,sans-serif;fill:#fff;text-anchor:middle}
    .t{font:12px system-ui,sans-serif;fill:#1a1a1a}
    .cap{font:700 12px system-ui,sans-serif;fill:#0055a0;text-anchor:middle}
  </style>
  <rect x="30" y="22" width="310" height="288" rx="10" fill="#f5f8fc" stroke="#0055a0"/>
  <rect x="30" y="22" width="310" height="34" rx="10" fill="#0055a0"/>
  <text x="185" y="44" class="h">COMPETENCIAS (art. 36.1)</text>
  <text x="48" y="84" class="t">• Colaborar en la mejora de la acción preventiva</text>
  <text x="48" y="124" class="t">• Promover la cooperación de los trabajadores</text>
  <text x="48" y="164" class="t" style="font-weight:700">• Ser consultados (previo a la decisión)</text>
  <text x="48" y="204" class="t">• Vigilar y controlar el cumplimiento</text>
  <rect x="48" y="232" width="274" height="60" rx="8" fill="#fff5e6" stroke="#e89822"/>
  <text x="185" y="256" class="cap" style="fill:#b5740f">Sin Comité (&lt; 50 trab.)</text>
  <text x="185" y="276" class="t" style="text-anchor:middle">asumen las funciones del Comité</text>
  <rect x="360" y="22" width="310" height="288" rx="10" fill="#e8f5ee" stroke="#2d8659"/>
  <rect x="360" y="22" width="310" height="34" rx="10" fill="#2d8659"/>
  <text x="515" y="44" class="h">FACULTADES (art. 36.2)</text>
  <text x="378" y="80" class="t">• Acompañar a técnicos e Inspección</text>
  <text x="378" y="106" class="t">• Acceder a información y documentación</text>
  <text x="378" y="132" class="t">• Ser informados de los daños en la salud</text>
  <text x="378" y="158" class="t">• Recibir información de organismos</text>
  <text x="378" y="184" class="t">• Realizar visitas a los lugares de trabajo</text>
  <text x="378" y="210" class="t">• Recabar medidas preventivas</text>
  <text x="378" y="236" class="t">• Proponer la paralización (art. 21.3)</text>
  <text x="515" y="278" class="t" style="text-anchor:middle;fill:#555">Plazo de informe en consulta: 15 días (art. 36.3)</text>
</svg>
```

---

## D5 · Garantías y sigilo del Delegado de Prevención (art. 37)

**Sección**: § 5 — Garantías y sigilo
**Propósito**: Mostrar las dos caras del estatuto: protección (art. 68 ET) y deber de sigilo.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 300" role="img" aria-label="El artículo 37 remite a las garantías del artículo 68 del Estatuto de los Trabajadores e impone el deber de sigilo profesional; el tiempo de reuniones y visitas no se imputa al crédito horario y la formación es tiempo de trabajo">
  <style>
    .h{font:700 14px system-ui,sans-serif;fill:#fff;text-anchor:middle}
    .t{font:12px system-ui,sans-serif;fill:#1a1a1a}
    .ti{font:700 15px system-ui,sans-serif;fill:#0055a0;text-anchor:middle}
  </style>
  <text x="350" y="26" class="ti">Estatuto del Delegado de Prevención (art. 37 LPRL)</text>
  <rect x="40" y="44" width="290" height="150" rx="10" fill="#e8f5ee" stroke="#2d8659"/>
  <rect x="40" y="44" width="290" height="32" rx="10" fill="#2d8659"/>
  <text x="185" y="65" class="h">GARANTÍAS (art. 68 ET)</text>
  <text x="56" y="100" class="t">• Expediente contradictorio si sanción</text>
  <text x="56" y="126" class="t">• Prioridad de permanencia</text>
  <text x="56" y="152" class="t">• No discriminación / libertad de expresión</text>
  <text x="56" y="178" class="t">• Crédito horario de representante</text>
  <rect x="370" y="44" width="290" height="150" rx="10" fill="#fdeaea" stroke="#d13c3c"/>
  <rect x="370" y="44" width="290" height="32" rx="10" fill="#d13c3c"/>
  <text x="515" y="65" class="h">DEBER (art. 37.3)</text>
  <text x="386" y="104" class="t" style="font-weight:700">Sigilo profesional</text>
  <text x="386" y="128" class="t">sobre las informaciones reservadas</text>
  <text x="386" y="152" class="t">a las que acceda (art. 65.2 ET);</text>
  <text x="386" y="176" class="t">(art. 37.3 LPRL)</text>
  <rect x="40" y="208" width="620" height="68" rx="8" fill="#fff5e6" stroke="#e89822"/>
  <text x="350" y="232" class="t" style="text-anchor:middle;font-weight:700;fill:#b5740f">NO se imputan al crédito horario:</text>
  <text x="350" y="254" class="t" style="text-anchor:middle">reuniones del Comité + visitas de acompañamiento (art. 36.2.a y c)</text>
  <text x="350" y="270" class="t" style="text-anchor:middle;fill:#555">La formación preventiva es tiempo de trabajo (art. 37.2)</text>
</svg>
```

---

## D6 · El Comité de Seguridad y Salud (arts. 38-39)

**Sección**: § 6 — El Comité de Seguridad y Salud
**Propósito**: Fijar el umbral de 50, la paridad, las reuniones trimestrales y las competencias.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 330" role="img" aria-label="El Comité de Seguridad y Salud es paritario y colegiado, se constituye con 50 o más trabajadores, se reúne trimestralmente, lo integran los Delegados de Prevención y un número igual de representantes del empresario, y participa en los planes de prevención">
  <style>
    .h{font:700 14px system-ui,sans-serif;fill:#fff;text-anchor:middle}
    .t{font:12px system-ui,sans-serif;fill:#1a1a1a;text-anchor:middle}
    .s{font:11px system-ui,sans-serif;fill:#555;text-anchor:middle}
  </style>
  <rect x="200" y="18" width="300" height="54" rx="8" fill="#0055a0"/>
  <text x="350" y="40" class="h">Comité de Seguridad y Salud</text>
  <text x="350" y="60" class="h" style="font-weight:400;font-size:11px">órgano paritario y colegiado (art. 38.1)</text>
  <rect x="60" y="92" width="270" height="58" rx="8" fill="#fdeaea" stroke="#d13c3c"/>
  <text x="195" y="116" class="t" style="font-weight:700">Umbral: 50 o más trabajadores</text>
  <text x="195" y="136" class="s">(&lt; 50 → lo asumen los Delegados de Prevención)</text>
  <rect x="370" y="92" width="270" height="58" rx="8" fill="#e8f5ee" stroke="#2d8659"/>
  <text x="505" y="116" class="t" style="font-weight:700">Se reúne trimestralmente</text>
  <text x="505" y="136" class="s">y cuando lo pida una representación (art. 38.3)</text>
  <rect x="120" y="166" width="220" height="60" rx="8" fill="#e8f0f8" stroke="#0055a0"/>
  <text x="230" y="190" class="t" style="font-weight:700">Delegados de Prevención</text>
  <text x="230" y="210" class="s">(parte social)</text>
  <rect x="360" y="166" width="220" height="60" rx="8" fill="#e8f0f8" stroke="#0055a0"/>
  <text x="470" y="190" class="t" style="font-weight:700">Representantes del empresario</text>
  <text x="470" y="210" class="s">en igual número (paridad)</text>
  <rect x="120" y="242" width="460" height="68" rx="8" fill="#fff5e6" stroke="#e89822"/>
  <text x="350" y="266" class="t" style="font-weight:700;fill:#b5740f">Competencias (art. 39)</text>
  <text x="350" y="286" class="s">participar en planes y programas · promover iniciativas</text>
  <text x="350" y="302" class="s">conocer la situación de PRL e informar la memoria anual</text>
</svg>
```

---

## D7 · Modalidades de servicio de prevención (arts. 30-31)

**Sección**: § 7 — Los servicios de prevención
**Propósito**: Mostrar las modalidades de organización preventiva y el caso del Ayuntamiento.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 300" role="img" aria-label="Modalidades de organización de la prevención: asunción por el empresario, trabajador designado, servicio de prevención propio, ajeno y mancomunado; el Ayuntamiento de Madrid tiene servicio propio">
  <style>
    .h{font:700 13px system-ui,sans-serif;fill:#fff;text-anchor:middle}
    .t{font:12px system-ui,sans-serif;fill:#1a1a1a;text-anchor:middle}
    .s{font:10px system-ui,sans-serif;fill:#555;text-anchor:middle}
  </style>
  <rect x="240" y="18" width="220" height="46" rx="8" fill="#003d75"/>
  <text x="350" y="46" class="h">Organización de la prevención</text>
  <line x1="350" y1="64" x2="350" y2="78" stroke="#0055a0"/>
  <line x1="95" y1="78" x2="605" y2="78" stroke="#0055a0"/>
  <g>
    <line x1="95" y1="78" x2="95" y2="92" stroke="#0055a0"/>
    <rect x="20" y="92" width="150" height="62" rx="7" fill="#e8f0f8" stroke="#0055a0"/>
    <text x="95" y="116" class="t" style="font-weight:700">Empresario</text>
    <text x="95" y="134" class="s">asunción personal</text>
    <text x="95" y="148" class="s">(empresa pequeña)</text>
    <line x1="222" y1="78" x2="222" y2="92" stroke="#0055a0"/>
    <rect x="180" y="92" width="150" height="62" rx="7" fill="#e8f0f8" stroke="#0055a0"/>
    <text x="255" y="116" class="t" style="font-weight:700">Trabajador</text>
    <text x="255" y="134" class="s">designado</text>
    <line x1="350" y1="78" x2="350" y2="92" stroke="#0055a0"/>
    <rect x="340" y="92" width="150" height="62" rx="7" fill="#e8f5ee" stroke="#2d8659"/>
    <text x="415" y="116" class="t" style="font-weight:700">Servicio propio</text>
    <text x="415" y="134" class="s">unidad interna</text>
    <line x1="478" y1="78" x2="478" y2="92" stroke="#0055a0"/>
    <rect x="500" y="92" width="150" height="62" rx="7" fill="#e8f0f8" stroke="#0055a0"/>
    <text x="575" y="116" class="t" style="font-weight:700">Servicio ajeno</text>
    <text x="575" y="134" class="s">entidad externa</text>
  </g>
  <rect x="180" y="168" width="340" height="44" rx="7" fill="#e8f0f8" stroke="#0055a0"/>
  <text x="350" y="195" class="t">Servicio de prevención mancomunado (varias entidades)</text>
  <rect x="120" y="226" width="460" height="56" rx="8" fill="#fff5e6" stroke="#e89822"/>
  <text x="350" y="250" class="t" style="font-weight:700;fill:#b5740f">Ayuntamiento de Madrid: Servicio de Prevención PROPIO</text>
  <text x="350" y="270" class="s">da cobertura al Ayuntamiento y a sus Organismos Autónomos (art. 46 AC)</text>
</svg>
```

---

## D8 · Capítulo IX del Acuerdo-Convenio (arts. 45-52)

**Sección**: § 8 — La PRL en el Acuerdo-Convenio
**Propósito**: Recorrer los ocho artículos del Capítulo IX del Acuerdo-Convenio 2019-2022.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 340" role="img" aria-label="Capítulo IX del Acuerdo-Convenio: artículo 45 salud laboral, 46 servicio de prevención, 47 recursos económicos, 48 representación del personal municipal, 49 adaptaciones de puesto, 50 edificios e instalaciones, 51 planes de autoprotección y 52 medio ambiente">
  <style>
    .ti{font:700 15px system-ui,sans-serif;fill:#0055a0;text-anchor:middle}
    .n{font:700 13px system-ui,sans-serif;fill:#fff;text-anchor:middle}
    .t{font:12px system-ui,sans-serif;fill:#1a1a1a}
  </style>
  <text x="350" y="26" class="ti">Acuerdo-Convenio 2019-2022 · Capítulo IX (arts. 45-52)</text>
  <g>
    <rect x="40" y="46" width="40" height="34" rx="6" fill="#0055a0"/><text x="60" y="69" class="n">45</text>
    <text x="92" y="69" class="t">Salud laboral</text>
    <rect x="40" y="86" width="40" height="34" rx="6" fill="#0055a0"/><text x="60" y="109" class="n">46</text>
    <text x="92" y="109" class="t">Servicio de prevención (propio del Ayuntamiento)</text>
    <rect x="40" y="126" width="40" height="34" rx="6" fill="#0055a0"/><text x="60" y="149" class="n">47</text>
    <text x="92" y="149" class="t">Recursos económicos destinados a la PRL</text>
    <rect x="40" y="166" width="40" height="34" rx="6" fill="#2d8659"/><text x="60" y="189" class="n">48</text>
    <text x="92" y="189" class="t" style="font-weight:700">Representación: Delegados de Prevención y Comité de S. y S.</text>
    <rect x="40" y="206" width="40" height="34" rx="6" fill="#0055a0"/><text x="60" y="229" class="n">49</text>
    <text x="92" y="229" class="t">Adaptaciones de puesto y movilidad por salud</text>
    <rect x="40" y="246" width="40" height="34" rx="6" fill="#0055a0"/><text x="60" y="269" class="n">50</text>
    <text x="92" y="269" class="t">Edificios e instalaciones de los centros de trabajo</text>
    <rect x="40" y="286" width="40" height="34" rx="6" fill="#0055a0"/><text x="60" y="309" class="n">51</text>
    <text x="92" y="309" class="t">Planes de autoprotección</text>
  </g>
  <rect x="470" y="286" width="190" height="34" rx="6" fill="#e8f0f8" stroke="#0055a0"/>
  <text x="565" y="308" class="t" style="text-anchor:middle">art. 52 · Medio ambiente</text>
</svg>
```

---

## D9 · Los 83 Delegados de Prevención del Ayto de Madrid

**Sección**: § 8 — La PRL en el Acuerdo-Convenio
**Propósito**: Visualizar el reparto del art. 48 entre el Ayuntamiento y sus Organismos Autónomos (el IAM, 6).

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 320" role="img" aria-label="Reparto de los 83 Delegados de Prevención: Ayuntamiento de Madrid 56, Agencia Tributaria 7, Madrid Salud 7, IAM 6, Agencia para el Empleo 4 y Agencia de Actividades 3">
  <style>
    .ti{font:700 15px system-ui,sans-serif;fill:#0055a0;text-anchor:middle}
    .t{font:12px system-ui,sans-serif;fill:#1a1a1a}
    .v{font:700 12px system-ui,sans-serif;fill:#0055a0}
  </style>
  <text x="350" y="26" class="ti">83 Delegados de Prevención (art. 48 AC)</text>
  <g class="t">
    <text x="20" y="62">Ayuntamiento de Madrid</text>
    <rect x="210" y="50" width="392" height="18" fill="#0055a0"/><text x="612" y="64" class="v">56</text>
    <text x="20" y="94">Agencia Tributaria Madrid</text>
    <rect x="210" y="82" width="49" height="18" fill="#2d8659"/><text x="269" y="96" class="v">7</text>
    <text x="20" y="126">Madrid Salud</text>
    <rect x="210" y="114" width="49" height="18" fill="#2d8659"/><text x="269" y="128" class="v">7</text>
    <text x="20" y="158" style="font-weight:700">IAM (Informática Ayto. Madrid)</text>
    <rect x="210" y="146" width="42" height="18" fill="#e89822"/><text x="262" y="160" class="v" style="fill:#b5740f">6</text>
    <text x="20" y="190">Agencia para el Empleo</text>
    <rect x="210" y="178" width="28" height="18" fill="#0055a0"/><text x="248" y="192" class="v">4</text>
    <text x="20" y="222">Agencia de Actividades</text>
    <rect x="210" y="210" width="21" height="18" fill="#0055a0"/><text x="241" y="224" class="v">3</text>
  </g>
  <line x1="210" y1="40" x2="210" y2="236" stroke="#cbd5e1"/>
  <rect x="120" y="252" width="460" height="52" rx="8" fill="#fff5e6" stroke="#e89822"/>
  <text x="350" y="275" class="t" style="text-anchor:middle;font-weight:700;fill:#b5740f">Comité de Seguridad y Salud único: 15 + 15</text>
  <text x="350" y="293" class="t" style="text-anchor:middle;fill:#555">crédito de 40 h/mes por delegado, adicional al general</text>
</svg>
```

---

## D10 · Representación: funcionarios vs. laborales (umbral 50)

**Sección**: § 9 — Representación de los empleados públicos
**Propósito**: Comparar los órganos de representación de funcionarios (TREBEP) y laborales (ET) con el umbral común de 50.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 300" role="img" aria-label="Funcionarios: Delegados de Personal con menos de 50 y Junta de Personal con 50 o más, según el TREBEP. Laborales: Delegados de Personal con menos de 50 y Comité de Empresa con 50 o más, según el Estatuto de los Trabajadores. El umbral 50 coincide con el del Comité de Seguridad y Salud">
  <style>
    .h{font:700 14px system-ui,sans-serif;fill:#fff;text-anchor:middle}
    .t{font:12px system-ui,sans-serif;fill:#1a1a1a;text-anchor:middle}
    .s{font:11px system-ui,sans-serif;fill:#555;text-anchor:middle}
  </style>
  <rect x="30" y="22" width="310" height="210" rx="10" fill="#f5f8fc" stroke="#0055a0"/>
  <rect x="30" y="22" width="310" height="32" rx="10" fill="#0055a0"/>
  <text x="185" y="44" class="h">FUNCIONARIOS (TREBEP)</text>
  <rect x="50" y="70" width="270" height="64" rx="8" fill="#e8f0f8" stroke="#0055a0"/>
  <text x="185" y="92" class="t" style="font-weight:700">&lt; 50: Delegados de Personal</text>
  <text x="185" y="112" class="s">1 (hasta 30) · 3 (de 31 a 49)</text>
  <text x="185" y="128" class="s">art. 39.2</text>
  <rect x="50" y="146" width="270" height="64" rx="8" fill="#e8f5ee" stroke="#2d8659"/>
  <text x="185" y="168" class="t" style="font-weight:700">≥ 50: Junta de Personal</text>
  <text x="185" y="188" class="s">composición por tramos (máx. 75)</text>
  <text x="185" y="204" class="s">art. 39.3 y 39.5</text>
  <rect x="360" y="22" width="310" height="210" rx="10" fill="#f5f8fc" stroke="#0055a0"/>
  <rect x="360" y="22" width="310" height="32" rx="10" fill="#0055a0"/>
  <text x="515" y="44" class="h">LABORALES (ET)</text>
  <rect x="380" y="70" width="270" height="64" rx="8" fill="#e8f0f8" stroke="#0055a0"/>
  <text x="515" y="92" class="t" style="font-weight:700">&lt; 50: Delegados de Personal</text>
  <text x="515" y="112" class="s">1 (de 6 a 30) · 3 (de 31 a 49)</text>
  <text x="515" y="128" class="s">art. 62 ET</text>
  <rect x="380" y="146" width="270" height="64" rx="8" fill="#e8f5ee" stroke="#2d8659"/>
  <text x="515" y="168" class="t" style="font-weight:700">≥ 50: Comité de Empresa</text>
  <text x="515" y="188" class="s">composición proporcional</text>
  <text x="515" y="204" class="s">arts. 63 y 66 ET</text>
  <rect x="120" y="246" width="460" height="40" rx="8" fill="#fff5e6" stroke="#e89822"/>
  <text x="350" y="271" class="t" style="font-weight:700;fill:#b5740f">El umbral 50 coincide con el del Comité de Seguridad y Salud (PRL)</text>
</svg>
```

---

## D11 · El derecho de reunión (art. 46 TREBEP)

**Sección**: § 10 — Competencias, garantías y derecho de reunión
**Propósito**: Quiénes pueden convocar una reunión y en qué horario se autoriza en el centro de trabajo (art. 46 TREBEP).

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 280" role="img" aria-label="Derecho de reunión del artículo 46: están legitimados las organizaciones sindicales, los Delegados y Juntas de Personal, los Comités de Empresa y los empleados en número no inferior al 40 por ciento del colectivo convocado; las reuniones en el centro de trabajo se autorizan fuera de las horas de trabajo, salvo acuerdo">
  <style>
    .h{font:700 14px system-ui,sans-serif;fill:#fff;text-anchor:middle}
    .t{font:12px system-ui,sans-serif;fill:#1a1a1a;text-anchor:middle}
    .big{font:700 26px system-ui,sans-serif;fill:#0055a0;text-anchor:middle}
    .s{font:11px system-ui,sans-serif;fill:#555;text-anchor:middle}
  </style>
  <rect x="180" y="18" width="340" height="44" rx="8" fill="#0055a0"/>
  <text x="350" y="46" class="h">Derecho de reunión (art. 46 TREBEP)</text>
  <rect x="40" y="80" width="300" height="120" rx="10" fill="#e8f0f8" stroke="#0055a0"/>
  <text x="190" y="104" class="t" style="font-weight:700">Legitimados para convocar</text>
  <text x="190" y="128" class="s">Organizaciones sindicales</text>
  <text x="190" y="148" class="s">Delegados / Juntas de Personal y Comités</text>
  <text x="190" y="176" class="big">≥ 40 %</text>
  <text x="190" y="194" class="s">empleados del colectivo convocado (46.1)</text>
  <rect x="360" y="80" width="300" height="120" rx="10" fill="#e8f5ee" stroke="#2d8659"/>
  <text x="510" y="104" class="t" style="font-weight:700">Reuniones en el centro de trabajo</text>
  <text x="510" y="140" class="t" style="font-weight:700;fill:#2d8659">Fuera de las horas de trabajo</text>
  <text x="510" y="166" class="s">salvo acuerdo entre el órgano de personal</text>
  <text x="510" y="184" class="s">y los legitimados para convocar (46.2)</text>
  <rect x="120" y="216" width="460" height="48" rx="8" fill="#fff5e6" stroke="#e89822"/>
  <text x="350" y="236" class="t" style="font-weight:700;fill:#b5740f">No perjudicará la prestación de los servicios</text>
  <text x="350" y="254" class="s">los convocantes son responsables de su normal desarrollo (46.2)</text>
</svg>
```

---

## D12 · Mapa de integración del Tema 9

**Sección**: § 11 — La representación en el Ayuntamiento de Madrid
**Propósito**: Situar en un solo esquema la LPRL, la representación TREBEP/ET y el Acuerdo-Convenio.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 360" role="img" aria-label="Mapa resumen: la LPRL regula Delegados de Prevención y Comité de Seguridad y Salud; el TREBEP y el Estatuto de los Trabajadores regulan la representación general; el Acuerdo-Convenio del Ayuntamiento de Madrid mejora ambos con 83 delegados, Comité único 15 más 15 y crédito de 40 horas; los convenios colectivos pueden mejorar y desarrollar la LPRL (artículo 2.2)">
  <style>
    .h{font:700 13px system-ui,sans-serif;fill:#fff;text-anchor:middle}
    .t{font:11px system-ui,sans-serif;fill:#1a1a1a;text-anchor:middle}
    .s{font:10px system-ui,sans-serif;fill:#555;text-anchor:middle}
    .ti{font:700 15px system-ui,sans-serif;fill:#0055a0;text-anchor:middle}
  </style>
  <text x="350" y="24" class="ti">Tema 9 — mapa de integración</text>
  <rect x="30" y="42" width="300" height="120" rx="10" fill="#e8f0f8" stroke="#0055a0"/>
  <rect x="30" y="42" width="300" height="28" rx="10" fill="#0055a0"/>
  <text x="180" y="61" class="h">LPRL (Ley 31/1995) — preventiva</text>
  <text x="180" y="92" class="t">Delegados de Prevención (arts. 35-37)</text>
  <text x="180" y="112" class="s">escala 35.2 · competencias/facultades 36 · garantías 37</text>
  <text x="180" y="138" class="t">Comité de Seguridad y Salud (arts. 38-39)</text>
  <text x="180" y="154" class="s">paritario · 50+ · trimestral</text>
  <rect x="370" y="42" width="300" height="120" rx="10" fill="#e8f0f8" stroke="#0055a0"/>
  <rect x="370" y="42" width="300" height="28" rx="10" fill="#0055a0"/>
  <text x="520" y="61" class="h">TREBEP / ET — general</text>
  <text x="520" y="92" class="t">Delegados y Juntas de Personal (art. 39)</text>
  <text x="520" y="112" class="s">umbral 50 · Comité de Empresa (laborales)</text>
  <text x="520" y="138" class="t">Garantías (41) · Reunión (46): 40 %</text>
  <text x="520" y="154" class="s">negociación: Mesas y Acuerdos (36, 38)</text>
  <line x1="180" y1="162" x2="350" y2="196" stroke="#2d8659" stroke-width="1.5"/>
  <line x1="520" y1="162" x2="350" y2="196" stroke="#2d8659" stroke-width="1.5"/>
  <rect x="120" y="198" width="460" height="84" rx="10" fill="#e8f5ee" stroke="#2d8659"/>
  <rect x="120" y="198" width="460" height="28" rx="10" fill="#2d8659"/>
  <text x="350" y="217" class="h">Acuerdo-Convenio Ayto de Madrid (Cap. IX, arts. 45-52)</text>
  <text x="350" y="244" class="t">mejora los mínimos: 83 Delegados de Prevención (IAM 6)</text>
  <text x="350" y="263" class="t">Comité único 15 + 15 · crédito 40 h/mes · Plan de PRL (2020)</text>
  <rect x="160" y="298" width="380" height="46" rx="8" fill="#fff5e6" stroke="#e89822"/>
  <text x="350" y="320" class="t" style="font-weight:700;fill:#b5740f">Art. 2.2 LPRL</text>
  <text x="350" y="337" class="s">sus disposiciones pueden mejorarse y desarrollarse en convenio colectivo</text>
</svg>
```

---
