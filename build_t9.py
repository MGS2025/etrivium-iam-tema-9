#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador del index.html del Tema 9 (ETRIVIUM IAM) a partir de los .md.
Replica la estructura validada de los Temas 1-8 (motor de test 1/3, pestaña Índice,
CSS de SVG aislado por diagrama). Incluye equilibrado determinista A/B/C del banco."""
import re, html, json, random, os
from collections import Counter

BASE = "/Users/joanmarquezsotoca/🧠🧠 MGS Brain/ETRIVIUM - Business Launcher v3 — Claude Skill/_repos-publicacion-2026-04-30/etrivium-iam-tema-9"

def read(name):
    with open(os.path.join(BASE, name), encoding="utf-8") as f:
        return f.read()

# ---------- Conversor Markdown -> HTML ----------
def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    return t

CALLOUTS = {
    "DATO CLAVE EXAMEN": ("callout-dato", "Dato clave examen"),
    "CITA CONSTITUCIONAL": ("callout-cita", "Cita constitucional"),
    "CITA NORMATIVA": ("callout-cita", "Cita normativa"),
    "EJEMPLO AYTO MADRID": ("callout-ayto", "Ejemplo Ayto Madrid"),
    "REFERENCIA CRUZADA": ("callout-ref", "Referencia cruzada"),
}

def md_to_html(md, skip_h1=True, drop_header_blockquote=True):
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)
    header_bq_dropped = False
    while i < n:
        line = lines[i]
        s = line.strip()
        if s == "---":
            out.append("<hr>")
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            level = len(m.group(1))
            if level == 1 and skip_h1:
                i += 1
                continue
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
            continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:\-|]+\|$", lines[i+1].strip()):
            header = [c.strip() for c in s.strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            th = "".join(f"<th>{inline(c)}</th>" for c in header)
            trs = ""
            for r in rows:
                tds = "".join(f"<td>{inline(c)}</td>" for c in r)
                trs += f"<tr>{tds}</tr>"
            out.append(f"<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>")
            continue
        if s.startswith(">"):
            bq = []
            while i < n and lines[i].strip().startswith(">"):
                bq.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            text = " ".join(x.strip() for x in bq if x.strip())
            if drop_header_blockquote and not header_bq_dropped and ("Título oficial" in text or "Versión" in text):
                header_bq_dropped = True
                continue
            cm = re.match(r"^\*\*\[([^\]]+)\]\*\*\s*(.*)$", text)
            if cm and cm.group(1) in CALLOUTS:
                cls, kicker = CALLOUTS[cm.group(1)]
                out.append(f'<div class="callout {cls}"><span class="kicker">{kicker}</span>{inline(cm.group(2))}</div>')
            else:
                out.append(f"<blockquote>{inline(text)}</blockquote>")
            continue
        if re.match(r"^\s*-\s+", line):
            items = []
            while i < n and re.match(r"^\s*-\s+", lines[i]):
                items.append(re.sub(r"^\s*-\s+", "", lines[i]).strip())
                i += 1
            lis = "".join(f"<li>{inline(x)}</li>" for x in items)
            out.append(f"<ul>{lis}</ul>")
            continue
        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[i]).strip())
                i += 1
            lis = "".join(f"<li>{inline(x)}</li>" for x in items)
            out.append(f"<ol>{lis}</ol>")
            continue
        if s == "":
            i += 1
            continue
        para = [s]
        i += 1
        while i < n:
            nx = lines[i].strip()
            if nx == "" or nx.startswith(("#", "|", ">", "-", "---")) or re.match(r"^\d+\.\s", nx):
                break
            para.append(nx)
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)

# ---------- Diagramas ----------
def parse_diagramas(md):
    blocks = []
    parts = re.split(r"\n## (D\d+ · [^\n]+)\n", md)
    for k in range(1, len(parts), 2):
        title = parts[k].strip()
        body = parts[k+1]
        sec = ""
        ms = re.search(r"\*\*Sección\*\*:\s*([^\n]+)", body)
        if ms: sec = ms.group(1).strip()
        prop = ""
        mp = re.search(r"\*\*Propósito\*\*:\s*([^\n]+)", body)
        if mp: prop = mp.group(1).strip()
        svgm = re.search(r"```svg\n(.*?)\n```", body, re.S)
        if not svgm: continue
        svg = svgm.group(1)
        did, dtitle = title.split(" · ", 1)
        blocks.append((did.strip(), dtitle.strip(), sec, prop, svg))
    return blocks

def scope_svg(svg, scope):
    """Aísla el CSS del <style> de cada SVG a una clase única para evitar que las
    reglas .h/.t/.s colisionen entre los 12 SVG del documento (bug que hacía que la
    última definición de cada clase ganara para todos -> texto desbordado)."""
    svg = re.sub(r"<svg ", f'<svg class="{scope}" ', svg, count=1)
    def _scope(m):
        css = m.group(1)
        rules = []
        for sels, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
            newsels = ",".join(f".{scope} {s.strip()}" for s in sels.split(",") if s.strip())
            rules.append(f"{newsels}{{{body.strip()}}}")
        return "<style>" + "".join(rules) + "</style>"
    return re.sub(r"<style>(.*?)</style>", _scope, svg, flags=re.S)

def diagramas_html(blocks):
    out = []
    for did, dtitle, sec, prop, svg in blocks:
        svg = scope_svg(svg, "sv" + did.lower())
        out.append(
            f'<div class="diagram">'
            f'<div class="diagram-title">{html.escape(did)} · {html.escape(dtitle)}</div>'
            f'<div class="diagram-sec">{html.escape(sec)}</div>'
            f'{svg}'
            f'<div class="diagram-caption">{html.escape(prop)}</div>'
            f'</div>'
        )
    return "\n".join(out)

# ---------- Test ----------
def parse_test(md):
    seg = md.split("## BANCO DE 150 PREGUNTAS")[1].split("## PLANTILLA DE RESPUESTAS")[0]
    lines = seg.split("\n")
    qs = []
    cur = None
    for line in lines:
        mq = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
        mo = re.match(r"^\s*-\s*([abc])\)\s*(.*)$", line)
        ma = re.match(r"^\s*-\s*\*\*Respuesta:\s*([abc])\*\*\s*·?\s*\*?([^*]*)\*?", line)
        if ma and cur:
            cur["ok"] = ma.group(1)
            cur["ref"] = ma.group(2).strip()
            qs.append(cur)
            cur = None
        elif mo and cur:
            cur[mo.group(1)] = mo.group(2).strip()
        elif mq:
            cur = {"t": mq.group(2).strip()}
    return qs

def balance(qs, seed=20260625):
    n = len(qs)
    targets = (["a"] * (n // 3 + 1) + ["b"] * (n // 3 + 1) + ["c"] * (n // 3 + 1))[:n]
    rnd = random.Random(seed)
    rnd.shuffle(targets)
    bal = []
    for q, tgt in zip(qs, targets):
        correct_text = q[q["ok"]]
        others = [q[x] for x in "abc" if x != q["ok"]]
        slots = {}
        slots[tgt] = correct_text
        rem = [x for x in "abc" if x != tgt]
        for pos, txt in zip(rem, others):
            slots[pos] = txt
        bal.append({"t": q["t"], "a": slots["a"], "b": slots["b"], "c": slots["c"],
                    "ok": tgt, "ref": q.get("ref", "")})
    return bal

# ---------- Casos ----------
def casos_html(md):
    parts = re.split(r"\n## (CASO PRÁCTICO \d+ — [^\n]+)\n", md)
    out = []
    for k in range(1, len(parts), 2):
        title = parts[k].strip()
        body = parts[k+1].split("\n## ")[0]
        body_html = md_to_html(body, skip_h1=True, drop_header_blockquote=False)
        num, rest = title.split(" — ", 1)
        out.append(
            f'<div class="caso-box">'
            f'<h3>{html.escape(num)} — {html.escape(rest)}</h3>'
            f'{body_html}</div>'
        )
    return "\n".join(out)

# ---------- Build ----------
def build():
    indice = md_to_html(read("tema-9-indice.md"))
    contenido = md_to_html(read("tema-9-contenido.md"))
    fuentes = md_to_html(read("tema-9-fuentes.md"))
    validacion = md_to_html(read("tema-9-validacion.md"))
    diag_blocks = parse_diagramas(read("tema-9-diagramas.md"))
    diagramas = diagramas_html(diag_blocks)
    qs = balance(parse_test(read("tema-9-test.md")))
    casos = casos_html(read("tema-9-caso-practico.md"))

    dist = Counter(q["ok"] for q in qs)

    questions_js = "[\n" + ",\n".join(
        "{t:%s,a:%s,b:%s,c:%s,ok:%s,ref:%s}" % (
            json.dumps(q["t"], ensure_ascii=False), json.dumps(q["a"], ensure_ascii=False),
            json.dumps(q["b"], ensure_ascii=False), json.dumps(q["c"], ensure_ascii=False),
            json.dumps(q["ok"], ensure_ascii=False), json.dumps(q["ref"], ensure_ascii=False)
        ) for q in qs) + "\n]"

    css = open(os.path.join(BASE, "_build_css.txt"), encoding="utf-8").read()

    inicio = '''
<section id="inicio" class="tab-content active">
  <div class="card-header">
    <h1>Tema 9 — Prevención de Riesgos Laborales y representación de los empleados públicos</h1>
    <p class="subtitle">Ley 31/1995 (LPRL) · Delegados de Prevención · Comités de Seguridad y Salud · PRL en el Acuerdo-Convenio del Ayuntamiento de Madrid · Representación de los empleados públicos (TREBEP / ET)</p>
  </div>
  <div class="version-banner">
    <span class="badge badge-v1">v1.0</span>
    <div><strong>Generación inicial · datos del Acuerdo-Convenio verificados en fuente oficial</strong><br>
    <small>Bloque I — Administrativo/Jurídico · C1 Técnico Auxiliar TIC · Ayuntamiento de Madrid · 2026-06-25</small></div>
  </div>
  <div class="card">
    <h2 style="margin-top:0">Resumen del tema</h2>
    <p>La <strong>Ley 31/1995 (LPRL)</strong>, anclada en el <strong>art. 40.2 CE</strong> y en la <strong>Directiva Marco 89/391/CEE</strong>, regula la seguridad y salud en el trabajo, también en las <strong>Administraciones Públicas</strong>. Su representación específica son los <strong>Delegados de Prevención</strong> (designados <em>por y entre</em> los representantes del personal; escala del art. 35.2: hasta 30 → el Delegado de Personal, 31-49 → 1, … máximo <strong>8</strong>) y el <strong>Comité de Seguridad y Salud</strong> (órgano <strong>paritario</strong>, a partir de <strong>50</strong> trabajadores, reuniones <strong>trimestrales</strong>). En el <strong>Ayuntamiento de Madrid</strong>, el <strong>Acuerdo-Convenio 2019-2022</strong> (Cap. IX, arts. 45-52) mejora esos mínimos: <strong>83 Delegados de Prevención</strong> (el <strong>IAM</strong>, 6), un <strong>Comité único 15+15</strong> y un <strong>crédito de 40 h/mes</strong>. La <strong>representación general</strong> se rige por el <strong>TREBEP</strong> (Delegados y Juntas de Personal, art. 39; reunión, art. 46) y el <strong>ET</strong> para el personal laboral.</p>
  </div>
  <div class="card">
    <h2 style="margin-top:0">Cómo está organizado este material</h2>
    <table>
      <thead><tr><th>Pestaña</th><th>Contenido</th></tr></thead>
      <tbody>
        <tr><td><strong>Índice</strong></td><td>Estructura del tema y conceptos clave por sección</td></tr>
        <tr><td><strong>Contenido</strong></td><td>11 secciones con texto, tablas y callouts de estudio</td></tr>
        <tr><td><strong>Diagramas</strong></td><td>12 esquemas visuales (SVG)</td></tr>
        <tr><td><strong>Test</strong></td><td>150 preguntas tipo examen con corrección automática y penalización 1/3</td></tr>
        <tr><td><strong>Casos</strong></td><td>6 casos prácticos aplicados al Ayuntamiento de Madrid (IAM)</td></tr>
        <tr><td><strong>Validación</strong></td><td>Checklist de revisión para María / Ana (IAM)</td></tr>
        <tr><td><strong>Fuentes</strong></td><td>Registro normativo, datos verificados y normas de citación</td></tr>
      </tbody>
    </table>
  </div>
</section>'''

    nav = '''
<nav class="tab-nav">
  <div class="logo"><strong style="color:#0055a0;font-size:18px">ETRIVIUM</strong><span style="color:#9aa5b4;font-size:12px">· IAM</span></div>
  <button class="tab-btn active" data-tab="inicio">Inicio</button>
  <button class="tab-btn" data-tab="indice">Índice</button>
  <button class="tab-btn" data-tab="contenido">Contenido</button>
  <button class="tab-btn" data-tab="diagramas">Diagramas</button>
  <button class="tab-btn" data-tab="test">Test <span class="version-badge">150</span></button>
  <button class="tab-btn" data-tab="casos">Casos</button>
  <button class="tab-btn" data-tab="validacion">Validación</button>
  <button class="tab-btn" data-tab="fuentes">Fuentes</button>
</nav>'''

    test_section = '''
<section id="test" class="tab-content">
  <h1>Test de autoevaluación</h1>
  <p class="subtitle">150 preguntas tipo examen (A/B/C). Penalización: cada fallo resta 1/3 de un acierto.</p>
  <div class="test-controls">
    <button class="btn btn-blue" id="btn-correct">Corregir test</button>
    <button class="btn btn-outline" id="btn-show-all">Mostrar todas las respuestas</button>
    <button class="btn btn-warn" id="btn-reset">Reiniciar</button>
  </div>
  <div class="score-bar" id="score-bar" style="display:none">
    <div class="score-item"><div class="score-value" id="sc-total">0</div><div class="score-label">Respondidas</div></div>
    <div class="score-item"><div class="score-value good" id="sc-ok">0</div><div class="score-label">Aciertos</div></div>
    <div class="score-item"><div class="score-value bad" id="sc-ko">0</div><div class="score-label">Fallos</div></div>
    <div class="score-item"><div class="score-value" id="sc-net">0.00</div><div class="score-label">Nota /10</div></div>
  </div>
  <div id="test-body"></div>
</section>'''

    engine = '''
function showTab(id){
  document.querySelectorAll('.tab-content').forEach(s => s.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  document.querySelector('.tab-btn[data-tab="'+id+'"]').classList.add('active');
  window.scrollTo(0,0);
}
function renderTest(){
  const body = document.getElementById('test-body'); body.innerHTML='';
  QUESTIONS.forEach((q, idx) => {
    const div = document.createElement('div');
    div.className='question'; div.dataset.num=idx+1; div.dataset.correct=q.ok;
    const opts = ['a','b','c'].map(l =>
      `<div class="q-opt" data-opt="${l}"><div class="q-letter">${l.toUpperCase()}</div><div>${q[l]}</div></div>`).join('');
    div.innerHTML = `<div class="q-num">Pregunta ${idx+1}</div>
      <div class="q-text">${q.t}</div>
      <div class="q-options">${opts}</div>
      <div class="q-answer"><strong>Correcta: ${q.ok.toUpperCase()})</strong> ${q[q.ok]}
        ${q.ref ? `<div class="q-ref">Ref: ${q.ref}</div>` : ''}</div>`;
    body.appendChild(div);
  });
  body.querySelectorAll('.q-opt').forEach(opt => opt.addEventListener('click', () => {
    const p = opt.closest('.q-options'); p.querySelectorAll('.q-opt').forEach(o=>o.classList.remove('selected'));
    opt.classList.add('selected');
  }));
}
function correctTest(){
  let ok=0,ko=0,total=0;
  document.querySelectorAll('#test-body .question').forEach(q => {
    const sel = q.querySelector('.q-opt.selected'); if(!sel) return; total++;
    const c=q.dataset.correct;
    q.querySelectorAll('.q-opt').forEach(o=>{if(o.dataset.opt===c)o.classList.add('correct');});
    if(sel.dataset.opt===c){ok++;}else{ko++;sel.classList.add('wrong');}
    q.querySelector('.q-answer').classList.add('show');
  });
  const rendered=document.querySelectorAll('#test-body .question').length;
  const net=Math.max(0, ok-ko/3);
  const note=rendered?(net*10/rendered).toFixed(2):'0.00';
  document.getElementById('score-bar').style.display='flex';
  document.getElementById('sc-total').textContent=total;
  document.getElementById('sc-ok').textContent=ok;
  document.getElementById('sc-ko').textContent=ko;
  document.getElementById('sc-net').textContent=note;
}
function showAllAnswers(){
  document.querySelectorAll('#test-body .question').forEach(q=>{
    const c=q.dataset.correct;
    q.querySelectorAll('.q-opt').forEach(o=>{if(o.dataset.opt===c)o.classList.add('correct');});
    q.querySelector('.q-answer').classList.add('show');
  });
}
function resetTest(){
  document.querySelectorAll('#test-body .question').forEach(q=>{
    q.querySelectorAll('.q-opt').forEach(o=>o.classList.remove('selected','correct','wrong'));
    q.querySelector('.q-answer').classList.remove('show');
  });
  document.getElementById('score-bar').style.display='none';
}
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('diagramas-body').innerHTML = DIAGRAMAS_HTML;
  renderTest();
  document.querySelectorAll('.tab-btn').forEach(b=>b.addEventListener('click',()=>showTab(b.dataset.tab)));
  document.getElementById('btn-correct').addEventListener('click', correctTest);
  document.getElementById('btn-show-all').addEventListener('click', showAllAnswers);
  document.getElementById('btn-reset').addEventListener('click', resetTest);
});
'''

    doc = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tema 9 — Prevención de Riesgos Laborales y representación de los empleados públicos | ETRIVIUM IAM</title>
<style>
{css}
</style>
</head>
<body>
{nav}
{inicio}
<section id="indice" class="tab-content">
  <h1>Índice del tema</h1>
  <div id="indice-body">
{indice}
  </div>
</section>
<section id="contenido" class="tab-content">
  <h1>Contenido teórico</h1>
  <div id="contenido-body">
{contenido}
  </div>
</section>
<section id="diagramas" class="tab-content">
  <h1>Diagramas</h1>
  <div id="diagramas-body"></div>
</section>
{test_section}
<section id="casos" class="tab-content">
  <h1>Casos prácticos</h1>
  <p class="subtitle">6 casos aplicados al Ayuntamiento de Madrid (IAM). Cada caso suma 10 puntos.</p>
  <div id="casos-body">
{casos}
  </div>
</section>
<section id="validacion" class="tab-content">
  <h1>Validación</h1>
  <div id="validacion-body">
{validacion}
  </div>
</section>
<section id="fuentes" class="tab-content">
  <h1>Fuentes</h1>
  <div id="fuentes-body">
{fuentes}
  </div>
</section>
<script>
const DIAGRAMAS_HTML = {json.dumps(diagramas, ensure_ascii=False)};
const QUESTIONS = {questions_js};
{engine}
</script>
</body>
</html>'''

    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"index.html generado: {len(doc)} bytes")
    print(f"Preguntas: {len(qs)} · distribución A/B/C: {dict(dist)}")
    print(f"Diagramas: {len(diag_blocks)} · Casos: {casos.count('caso-box')}")

if __name__ == "__main__":
    build()
