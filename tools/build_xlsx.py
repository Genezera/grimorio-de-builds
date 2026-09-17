# -*- coding: utf-8 -*-
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import FormulaRule, CellIsRule, DataBarRule
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.drawing.image import Image as XLImage
from openpyxl.utils import get_column_letter as L
from openpyxl.comments import Comment
import chober as D

OUT = sys.argv[1]
F = "Arial"
C = dict(night="13201C", deep="1B2B26", jade="3E9E86", jadeL="D5EEE7", gold="C98E2B", goldL="FBEFD6",
         ink="1F2A27", mute="5E6B67", paper="F7F8F5", line="C9D3CF", red="B84A3A", redL="F6DDD8", ok="2E7D5B", okL="DDF0E6",
         silver="8E9AA6", input="FFF4C2")
thin = Side(style="thin", color=C["line"])
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)

def fill(h): return PatternFill("solid", fgColor=h)
def font(**k):
    k.setdefault("name", F); k.setdefault("size", 10); k.setdefault("color", C["ink"]); return Font(**k)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)

wb = Workbook()

def sheet(title, widths, tab):
    ws = wb.create_sheet(title)
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.tabColor = tab
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[L(i)].width = w
    return ws

def banner(ws, title, sub, ncols):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
    c = ws.cell(1, 1, title); c.font = font(size=18, bold=True, color="FFFFFF"); c.alignment = Alignment(vertical="center", indent=1)
    s = ws.cell(2, 1, sub); s.font = font(size=10, color="CFE3DC", italic=True); s.alignment = Alignment(vertical="center", indent=1, wrap_text=True)
    for col in range(1, ncols + 1):
        ws.cell(1, col).fill = fill(C["night"]); ws.cell(2, col).fill = fill(C["night"])
    ws.row_dimensions[1].height = 34; ws.row_dimensions[2].height = 30

def header(ws, row, labels, color=None):
    for i, t in enumerate(labels, 1):
        c = ws.cell(row, i, t)
        c.font = font(bold=True, color="FFFFFF"); c.fill = fill(color or C["deep"]); c.alignment = CENTER; c.border = BOX
    ws.row_dimensions[row].height = 22

def put(ws, row, values, bold_first=False, zebra=False, height=None):
    for i, v in enumerate(values, 1):
        c = ws.cell(row, i, v)
        c.font = font(bold=(bold_first and i == 1)); c.alignment = WRAP; c.border = BOX
        if zebra: c.fill = fill(C["paper"])
    if height: ws.row_dimensions[row].height = height

def section(ws, row, text, ncols, color=None):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
    c = ws.cell(row, 1, text); c.font = font(size=12, bold=True, color="FFFFFF"); c.alignment = Alignment(vertical="center", indent=1)
    for col in range(1, ncols + 1): ws.cell(row, col).fill = fill(color or C["jade"])
    ws.row_dimensions[row].height = 22

def est_h(texts, widths):
    lines = 1
    for t, w in zip(texts, widths):
        if t is None: continue
        s = str(t); n = sum(max(1, -(-len(part) // max(8, int(w * 1.1)))) for part in s.split("\n"))
        lines = max(lines, n)
    return min(15 * lines + 4, 160)

PH = D.PHASES
N_PH = len(PH)

# ============================================================ LISTAS (oculta, base das fórmulas)
lst = wb.active; lst.title = "Listas"
lst["A1"], lst["B1"], lst["C1"], lst["D1"], lst["E1"], lst["F1"] = "Nível inicial", "Fase", "Carry", "Objetivo", "Tag", "Ascendência"
for i, p in enumerate(PH, 2):
    lst.cell(i, 1, p["lv"][0]); lst.cell(i, 2, p["name"]); lst.cell(i, 3, p["carry"]); lst.cell(i, 4, p["goal"]); lst.cell(i, 5, p["tag"]); lst.cell(i, 6, p["asc"] or "—")
lst["H1"] = "Status"; lst["H2"], lst["H3"], lst["H4"] = "Pendente", "Fazendo", "Feito"
lst["I1"] = "Sim/Não"; lst["I2"], lst["I3"] = "Sim", "Não"
lst["J1"] = "Modo"; lst["J2"], lst["J3"] = "Barato", "Completo"
lst["K1"] = "Tipo"; lst["K2"], lst["K3"] = "Companion", "Outro"
lst["L1"] = "Unidade"; lst["L2"], lst["L3"] = "%", "Flat"
lst.sheet_state = "hidden"
PH_RANGE = f"Listas!$A$2:$A${N_PH+1}"

# ============================================================ INÍCIO
ws = sheet("INÍCIO", [22, 18, 18, 18, 18, 18, 18, 18, 18], C["gold"])
wb.move_sheet(ws, offset=-1)
banner(ws, "SPIRIT WALKER · ZOO CHOBER CHABER (rota Mattjestic) — Nível 1 → 100",
       f"PoE 2 {D.PATCH} · atualizado {D.UPDATED} · rota barata com trade + opção completa. Edite só as células AMARELAS.", 9)

section(ws, 4, "ONDE ESTOU AGORA", 9, C["gold"])
labels = [("Seu nível atual", 35), ("Modo de investimento", "Barato"), ("Spirit total (do jogo)", 191)]
for i, (lab, val) in enumerate(labels):
    r = 5 + i
    ws.cell(r, 1, lab).font = font(bold=True)
    c = ws.cell(r, 2, val); c.fill = fill(C["input"]); c.font = font(bold=True, size=12, color="0000FF"); c.border = BOX; c.alignment = CENTER
ws["B5"].comment = Comment("Digite seu nível (1–100). Todo o painel se ajusta.", "Guia")
ws["B7"].comment = Comment("Valor mostrado no painel de personagem. Usado no Spirit Planner.", "Guia")
dv = DataValidation(type="whole", operator="between", formula1="1", formula2="100", showErrorMessage=True, errorTitle="Nível", error="Digite um nível de 1 a 100."); ws.add_data_validation(dv); dv.add("B5")
dvm = DataValidation(type="list", formula1="=Listas!$J$2:$J$3"); ws.add_data_validation(dvm); dvm.add("B6")

rows = [
 ("Fase atual", f"=INDEX(Listas!$B$2:$B${N_PH+1},MATCH($B$5,{PH_RANGE},1))"),
 ("Etapa", f"=INDEX(Listas!$E$2:$E${N_PH+1},MATCH($B$5,{PH_RANGE},1))"),
 ("Quem carrega o dano", f"=INDEX(Listas!$C$2:$C${N_PH+1},MATCH($B$5,{PH_RANGE},1))"),
 ("Objetivo da fase", f"=INDEX(Listas!$D$2:$D${N_PH+1},MATCH($B$5,{PH_RANGE},1))"),
 ("Último marco (até seu nível)", "=IFERROR(\"Nv \"&INDEX('Nível 1-100'!$K$4:$K$103,$B$5)&\" — \"&INDEX('Nível 1-100'!$J$4:$J$103,$B$5),\"\")"),
 ("Próximo marco", "=IFERROR(\"Nv \"&INDEX('Nível 1-100'!$A$4:$A$103,MATCH(\"*\",INDEX(('Nível 1-100'!$C$4:$C$103<>\"—\")*('Nível 1-100'!$A$4:$A$103>$B$5)&\"\",0),0)),\"\")"),
 ("Compra recomendada agora", "=IF($B$6=\"Barato\",INDEX('Nível 1-100'!$E$4:$E$103,$B$5),INDEX('Nível 1-100'!$F$4:$F$103,$B$5))"),
 ("Progresso de marcos", "=IFERROR(COUNTIF('Nível 1-100'!$G$4:$G$103,\"Feito\")/100,0)"),
 ("Quests permanentes feitas", "=COUNTIF(Quests!$F$4:$F$32,\"Feito\")&\" de \"&COUNTA(Quests!$C$4:$C$32)"),
]
# próximo marco: fórmula robusta sem array → coluna auxiliar em Nível 1-100 (H) ; substituída abaixo
rows[5] = ("Próximo marco", "=IFERROR(\"Nv \"&INDEX('Nível 1-100'!$A$4:$A$103,MATCH(1,'Nível 1-100'!$I$4:$I$103,0))&\" — \"&INDEX('Nível 1-100'!$C$4:$C$103,MATCH(1,'Nível 1-100'!$I$4:$I$103,0)),\"Você chegou ao fim!\")")
for i, (lab, fml) in enumerate(rows):
    r = 9 + i
    ws.cell(r, 1, lab).font = font(bold=True)
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=9)
    c = ws.cell(r, 2, fml); c.alignment = Alignment(wrap_text=True, vertical="center"); c.font = font(size=11)
    for col in range(1, 10): ws.cell(r, col).border = BOX
    ws.row_dimensions[r].height = 30 if i in (3, 4, 5, 6) else 20
ws["B9"].font = font(size=14, bold=True, color=C["jade"])
ws["B16"].number_format = "0%"
ws.conditional_formatting.add("B16", DataBarRule(start_type="num", start_value=0, end_type="num", end_value=1, color=C["jade"]))

section(ws, 19, "ROTA S-TIER — FASES (a linha dourada é a sua fase)", 9)
header(ws, 20, ["Fase", "Níveis", "Etapa", "Carry", "Dano player/zoo", "Ascendência", "Sai da fase quando…", "", ""])
ws.merge_cells("G20:I20")
for i, p in enumerate(PH):
    r = 21 + i
    vals = [p["name"], f"{p['lv'][0]}–{p['lv'][1]}", p["tag"], p["carry"], f"{p['dmgSplit'][0]}% / {p['dmgSplit'][1]}%", p["asc"] or "—", " · ".join(p["exit"])]
    put(ws, r, vals + ["", ""], bold_first=True)
    ws.merge_cells(start_row=r, start_column=7, end_row=r, end_column=9)
    ws.row_dimensions[r].height = 44
last = 20 + N_PH
ws.conditional_formatting.add(f"A21:I{last}", FormulaRule(formula=[f"$A21=$B$9"], fill=fill(C["goldL"]), font=Font(name=F, bold=True, color="7A5210")))

section(ws, last + 2, "CORREÇÕES FEITAS NA PLANILHA ANTIGA", 9, C["red"])
for i, t in enumerate(D.FIXES):
    r = last + 3 + i
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=9)
    ws.cell(r, 1, "✔ " + t).font = font()
ws.freeze_panes = "A4"

# ============================================================ NÍVEL 1-100
ws = sheet("Nível 1-100", [7, 16, 52, 40, 40, 40, 12, 22, 6], C["jade"])
banner(ws, "NÍVEL 1 → 100 — marco por nível", "Linhas com marco real em negrito. Marque Status = Feito. A linha do seu nível fica dourada (nível no INÍCIO).", 8)
header(ws, 3, ["Nível", "Fase", "Faça agora (marco)", "Foco da fase", "Barato (trade)", "Completo (currency)", "Status", "Carry", "aux"])
dvs = DataValidation(type="list", formula1="=Listas!$H$2:$H$4"); ws.add_data_validation(dvs)
for lv in range(1, 101):
    r = 3 + lv; p = D.phase_for(lv)
    ms = D.MILESTONES.get(lv)
    cheap = p["cheap"][(lv - p["lv"][0]) % len(p["cheap"])]
    full = p["full"][(lv - p["lv"][0]) % len(p["full"])]
    put(ws, r, [lv, p["name"], ms or "—", p["goal"] if lv == p["lv"][0] else p["stats"][0] + " → " + ", ".join(p["stats"][1:4]), cheap, full, "Pendente", p["carry"]], zebra=(lv % 2 == 0))
    ws.cell(r, 9, f'=IF(AND(C{r}<>"—",A{r}>INÍCIO!$B$5),1,0)').font = font(color="AAAAAA", size=8)
    ws.cell(r, 10, f'=IF(C{r}<>"—",C{r},J{r-1})' if lv > 1 else f'=C{r}')
    ws.cell(r, 11, f'=IF(C{r}<>"—",A{r},K{r-1})' if lv > 1 else f'=A{r}')
    if ms: ws.cell(r, 3).font = font(bold=True)
    ws.cell(r, 1).alignment = CENTER; ws.cell(r, 7).alignment = CENTER
    dvs.add(f"G{r}")
    ws.row_dimensions[r].height = est_h([ms, cheap, full], [52, 40, 40])
ws.conditional_formatting.add("A4:H103", FormulaRule(formula=["$A4=INÍCIO!$B$5"], fill=fill(C["goldL"]), font=Font(name=F, bold=True, color="7A5210")))
ws.conditional_formatting.add("G4:G103", CellIsRule(operator="equal", formula=['"Feito"'], fill=fill(C["okL"]), font=Font(name=F, color=C["ok"], bold=True)))
ws.conditional_formatting.add("G4:G103", CellIsRule(operator="equal", formula=['"Fazendo"'], fill=fill(C["goldL"])))
for col in "IJK": ws.column_dimensions[col].hidden = True
ws.freeze_panes = "C4"; ws.auto_filter.ref = "A3:H103"

# ============================================================ ROTA POR FASE
ws = sheet("Rota por Fase", [26, 34, 34, 34, 34, 34], C["jade"])
banner(ws, "ROTA POR FASE — o que jogar, comprar e evitar", "Cada bloco é uma fase. 'Barato' = começar com pouco no trade; 'Completo' = seguir a build como deve ser.", 6)
r = 4
for p in PH:
    section(ws, r, f"{p['name'].upper()}  ·  Nv {p['lv'][0]}–{p['lv'][1]}  ·  {p['tag']}", 6); r += 1
    for lab, val in [("Objetivo", p["goal"]), ("Carry", p["carry"]), ("Ascendência", p["asc"] or "—"), ("Árvore", p["tree"]),
                     ("Rotação", "  →  ".join(p["rotation"])), ("Evite", " · ".join(p["avoid"])), ("Sai da fase quando", " · ".join(p["exit"]))]:
        ws.cell(r, 1, lab).font = font(bold=True, color=C["jade"]); ws.cell(r, 1).alignment = WRAP
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
        ws.cell(r, 2, val).alignment = WRAP
        for col in range(1, 7): ws.cell(r, col).border = BOX
        ws.row_dimensions[r].height = est_h([val], [160]); r += 1
    header(ws, r, ["Barato (trade)", "", "", "Completo (currency)", "", ""], C["gold"])
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3); ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=6); r += 1
    n = max(len(p["cheap"]), len(p["full"]))
    for i in range(n):
        a = p["cheap"][i] if i < len(p["cheap"]) else ""; b = p["full"][i] if i < len(p["full"]) else ""
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3); ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=6)
        ws.cell(r, 1, ("• " + a) if a else "").alignment = WRAP; ws.cell(r, 4, ("• " + b) if b else "").alignment = WRAP
        ws.row_dimensions[r].height = est_h([a, b], [90, 90]); r += 1
    ws.cell(r, 1, "Prioridade de stats: " + " > ".join(p["stats"])).font = font(italic=True, color=C["mute"])
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=6); r += 2

# ============================================================ SKILLS & SUPPORTS
ws = sheet("Skills & Supports", [16, 30, 10, 20, 20, 20, 20, 20, 24, 60], C["jade"])
banner(ws, "SKILLS & SUPPORTS — rota Chober Chaber (Mattjestic)", "Filtre a coluna Fase. Coluna J explica cada skill; no fim da aba, o que cada support faz.", 10)
header(ws, 3, ["Fase", "Skill", "Set", "Support 1", "Support 2", "Support 3", "Support 4", "Support 5", "Função", "Por que está na build"])
r = 4
for p in PH:
    for g in p["gems"]:
        s = g["sup"] + [""] * (5 - len(g["sup"]))
        put(ws, r, [p["name"], g["skill"], g["set"], *s[:5], g["role"], g.get("why", "")], zebra=(PH.index(p) % 2 == 1), height=est_h([g.get("why", "")], [60]))
        ws.cell(r, 2).font = font(bold=True, color=C["jade"] if "Silverfist" in g["skill"] or "Azmerian" in g["skill"] else C["ink"])
        r += 1
ws.freeze_panes = "C4"; ws.auto_filter.ref = f"A3:J{r-1}"
r += 1
section(ws, r, "O QUE CADA SUPPORT FAZ E POR QUE USAR", 10); r += 1
for k_, v_ in sorted(D.SUPWHY.items()):
    ws.cell(r, 2, k_).font = font(bold=True); ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=10)
    ws.cell(r, 3, v_).alignment = WRAP; ws.row_dimensions[r].height = est_h([v_], [150]); r += 1

# ============================================================ GEAR
ws = sheet("Gear", [14, 36, 36, 36, 30, 36], C["gold"])
banner(ws, "GEAR — do barato ao completo", "Barato = poucos Exalts no trade · Valor = bom custo-benefício · Completo = build como deve ser. Preços variam: use as faixas.", 6)
header(ws, 3, ["Slot", "Barato", "Valor", "Completo", "Prioridade de affix", "Nota"])
for i, g in enumerate(D.GEAR):
    r = 4 + i
    put(ws, r, [g["slot"], g["cheap"], g["value"], g["full"], g["affix"], g["note"]], bold_first=True, height=est_h([g["cheap"], g["value"], g["full"], g["note"]], [36, 36, 36, 36]))
ws.cell(4, 6).font = font(bold=True, color=C["red"]); ws.cell(12, 6).font = font(bold=True, color=C["red"])
r = 5 + len(D.GEAR)
section(ws, r, "ORDEM DE COMPRA — onde gastar primeiro", 6, C["gold"]); r += 1
header(ws, r, ["#", "Item", "Fase", "Custo", "Impacto", ""]); r += 1
for b in D.BUY_ORDER:
    put(ws, r, [b["p"], b["item"], b["phase"], b["cost"], b["impact"], ""]); ws.cell(r, 1).alignment = CENTER; r += 1
ws.freeze_panes = "B4"

# ============================================================ SPIRIT PLANNER
ws = sheet("Spirit Planner", [30, 12, 13, 12, 10, 14, 30], C["gold"])
banner(ws, "SPIRIT PLANNER — cabe no seu Spirit?", "Amarelo = você edita. Estimativa: custo ÷ ((1 + increased) × more/less). Confira sempre o valor final no jogo.", 7)
section(ws, 4, "PARÂMETROS", 7, C["gold"])
params = [("Spirit total", "=INÍCIO!B7", "Vem do INÍCIO (B7)."),
          ("Trusted Kinship alocado?", "Sim", "30% more eficiência p/ Companion · 20% less p/ o resto."),
          ("Easy Going alocado?", "Sim", "+25% increased eficiência de Companion."),
          ("Outros % increased eficiência (ex.: 0,10)", 0, "Jewels/itens. Digite como fração."),
          ("Idolatry alocado?", "Não", "+2% eficiência por Idol."),
          ("Nº de Idols equipados", 0, "")]
dvyn = DataValidation(type="list", formula1="=Listas!$I$2:$I$3"); ws.add_data_validation(dvyn)
for i, (lab, val, note) in enumerate(params):
    r = 5 + i
    ws.cell(r, 1, lab).font = font(bold=True)
    c = ws.cell(r, 2, val); c.border = BOX; c.alignment = CENTER
    if i == 0: c.font = font(bold=True, color="008000")
    else: c.fill = fill(C["input"]); c.font = font(bold=True, color="0000FF")
    ws.cell(r, 3, note).font = font(italic=True, color=C["mute"]); ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=7)
    if val in ("Sim", "Não"): dvyn.add(f"B{r}")
ws["B8"].number_format = "0%"
ws.cell(11, 1, "Increased (Companion)").font = font(bold=True); ws["B11"] = '=IF(B7="Sim",0.25,0)+B8+IF(B9="Sim",0.02*B10,0)'; ws["B11"].number_format = "0%"
ws.cell(12, 1, "Increased (Outros)").font = font(bold=True); ws["B12"] = '=B8+IF(B9="Sim",0.02*B10,0)'; ws["B12"].number_format = "0%"
ws.cell(13, 1, "Multiplicador more/less (Companion / Outro)").font = font(bold=True); ws["B13"] = '=IF(B6="Sim",1.3,1)'; ws["C13"] = '=IF(B6="Sim",0.8,1)'

section(ws, 15, "SEU ZOO (exemplo preenchido: Ato 4 barato — troque pelos seus valores)", 7)
header(ws, 16, ["Skill / Companion", "Ativo?", "Tipo", "Custo base", "Unidade", "Spirit usado", "Nota"])
zoo = [("Mighty Silverfist", "Sim", "Companion", 47.4, "%", "47,4% antes de reduções (guia)"),
       ("Quadrilla (2º beast)", "Sim", "Companion", 42.3, "%", "42,3% antes de reduções (guia)"),
       ("Wild Protector", "Sim", "Companion", 0, "Flat", "Digite o custo mostrado no jogo"),
       ("Wind Dancer", "Sim", "Outro", 0, "Flat", "Digite o custo base do jogo"),
       ("Discipline / Malice", "Não", "Outro", 0, "Flat", "Digite o custo base do jogo"),
       ("Withering Presence", "Não", "Outro", 0, "Flat", "Sofre o 'less' do Trusted Kinship"),
       ("Skeletal Cleric", "Não", "Outro", 0, "Flat", ""),
       ("Vile Vulture", "Não", "Companion", 45.3, "%", "T15"),
       ("Rhex", "Não", "Companion", 31.2, "%", "Aura barata"),
       ("Outro", "Não", "Outro", 0, "Flat", "")]
dvt = DataValidation(type="list", formula1="=Listas!$K$2:$K$3"); dvu = DataValidation(type="list", formula1="=Listas!$L$2:$L$3")
ws.add_data_validation(dvt); ws.add_data_validation(dvu)
for i, (n, on, t, cost, unit, note) in enumerate(zoo):
    r = 17 + i
    put(ws, r, [n, on, t, cost, unit, None, note])
    for col in (1, 2, 3, 4, 5):
        ws.cell(r, col).fill = fill(C["input"]); ws.cell(r, col).font = font(color="0000FF", bold=(col == 1))
    dvyn.add(f"B{r}"); dvt.add(f"C{r}"); dvu.add(f"E{r}")
    ws.cell(r, 6, f'=IF(B{r}<>"Sim",0,IF(E{r}="%",D{r}/100*$B$5,D{r})/IF(C{r}="Companion",(1+$B$11)*$B$13,(1+$B$12)*$C$13))')
    ws.cell(r, 6).number_format = "0.0"; ws.cell(r, 6).font = font(bold=True)
    ws.cell(r, 7).font = font(italic=True, color=C["mute"])
end = 17 + len(zoo) - 1
r = end + 2
R0 = r
for lab, fml, fmt in [("Spirit reservado", f"=SUM(F17:F{end})", "0.0"), ("Spirit livre", f"=B5-B{R0}", "0.0"), ("Uso", f"=IFERROR(B{R0}/B5,0)", "0%")]:
    ws.cell(r, 1, lab).font = font(bold=True, size=12)
    c = ws.cell(r, 2, fml); c.number_format = fmt; c.font = font(bold=True, size=12); c.border = BOX; r += 1
ws.cell(r, 1, "Status").font = font(bold=True, size=12)
ws.cell(r, 2, f'=IF(B{end+3}<0,"ESTOUROU — desligue algo",IF(B{end+4}>0.9,"No limite","OK"))').font = font(bold=True, size=12)
ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
ws.conditional_formatting.add(f"B{end+3}", CellIsRule(operator="lessThan", formula=["0"], fill=fill(C["redL"]), font=Font(name=F, color=C["red"], bold=True)))
ws.conditional_formatting.add(f"B{end+4}", DataBarRule(start_type="num", start_value=0, end_type="num", end_value=1, color=C["gold"]))
ws.conditional_formatting.add(f"B{r}", FormulaRule(formula=[f'LEFT(B{r},3)="EST"'], fill=fill(C["redL"]), font=Font(name=F, color=C["red"], bold=True)))
ws.conditional_formatting.add(f"B{r}", FormulaRule(formula=[f'B{r}="OK"'], fill=fill(C["okL"]), font=Font(name=F, color=C["ok"], bold=True)))
ws.cell(r + 2, 1, "Assunção: custos '%' são % do Spirit máximo antes de reduções (conforme o guia imortilize). Os valores 'Flat' você copia do jogo. É uma estimativa — o painel de skills do jogo é a verdade final.").font = font(italic=True, color=C["mute"])
ws.merge_cells(start_row=r + 2, start_column=1, end_row=r + 2, end_column=7)

# ============================================================ BEASTS
ws = sheet("Companions & Beasts", [22, 34, 20, 11, 9, 38, 46, 20], C["jade"])
banner(ws, "COMPANIONS & BEASTS — o que capturar", "Custo = % de Spirit antes de reduções. Prioridade de aura: " + " > ".join(D.AURA_PRIORITY[:5]), 8)
header(ws, 3, ["Beast", "Onde", "Papel", "Custo base", "Tier", "Mods desejados", "Supports", "Requer"])
for i, b in enumerate(D.BEASTS):
    r = 4 + i
    put(ws, r, [b["name"], b["where"], b["role"], (b["cost"] / 100) if b["cost"] else "—", b["tier"], b["mods"], b["sup"], b["req"]], bold_first=True, height=est_h([b["where"], b["mods"], b["sup"]], [34, 38, 46]))
    ws.cell(r, 4).number_format = "0.0%"; ws.cell(r, 5).alignment = CENTER; ws.cell(r, 4).alignment = CENTER
    ws.cell(r, 5).font = font(bold=True, color=C["gold"] if b["tier"].startswith("S") else C["ink"])
r = 5 + len(D.BEASTS)
section(ws, r, "LOOP DE CAPTURA", 8); r += 1
for i, t in enumerate(["Ache um beast raro/unique capturável.", "Pause (atalho do Marketplace no botão do meio) e leia os mods antes de bater.", "Se não servir, siga em frente; se servir, use Tame Beast com ele em vida baixa.", "Compare a reserva no Spirit Planner: aura boa que estoura Spirit piora o setup.", "Suba a gem Tame Beast e coloque supports de sobrevivência (Meat Shield II, Loyalty)."], 1):
    ws.cell(r, 1, f"Passo {i}").font = font(bold=True, color=C["jade"])
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=8); ws.cell(r, 2, t); r += 1
ws.freeze_panes = "B4"

# ============================================================ ASCENDÊNCIA & PASSIVAS
ws = sheet("Ascendência & Árvore", [8, 26, 26, 50, 44, 14], C["jade"])
banner(ws, "ASCENDÊNCIA & ÁRVORE DE PASSIVAS", "Ordem obrigatória: Wild Protector → The Natural Order → The Catha's Balance → Idolatry. Texto dos nós conforme PoE2DB.", 6)
header(ws, 3, ["#", "Nó", "Quando", "O que faz", "Por que", ""])
for i, a in enumerate(D.ASCENDANCY):
    put(ws, 4 + i, [a["order"], a["node"], a["when"], a["text"], a["why"], ""], height=60); ws.cell(4 + i, 2).font = font(bold=True, color=C["gold"]); ws.cell(4 + i, 1).alignment = CENTER
r = 9
section(ws, r, "PASSIVAS-CHAVE", 6); r += 1
header(ws, r, ["", "Nó", "Tipo", "O que faz", "Por que", "Quando"]); r += 1
for k in D.KEY_PASSIVES:
    put(ws, r, ["", k["node"], k["type"], k["text"], k["why"], k["when"]], height=44); ws.cell(r, 2).font = font(bold=True); r += 1
r += 1
section(ws, r, "ÁRVORE POR ETAPA", 6); r += 1
header(ws, r, ["Nível", "Foco", "Dano", "Defesa", "Spirit", "Não faça"]); r += 1
for t in D.TREE_STAGES:
    put(ws, r, [t["lv"], t["focus"], t["dmg"], t["def"], t["spirit"], t["dont"]], height=36); r += 1
ws.cell(r + 1, 1, "Dica: use o planner da Mobalytics (links em Fontes) para ver o caminho exato de cada ato — as cores Amarelo/Rosa/Verde são árvore principal / Weapon Set 1 / Weapon Set 2.").font = font(italic=True, color=C["mute"])
ws.merge_cells(start_row=r + 1, start_column=1, end_row=r + 1, end_column=6)

# ============================================================ QUESTS
ws = sheet("Quests", [12, 22, 30, 40, 12, 12], C["gold"])
banner(ws, "RECOMPENSAS PERMANENTES — não pule", "+130 Spirit, resistências e weapon set points ao longo da campanha. Marque Feito.", 6)
header(ws, 3, ["Ato", "Área", "Boss / Quest", "Recompensa", "Prioridade", "Status"])
for i, q in enumerate(D.DATA["quests"]):
    r = 4 + i
    put(ws, r, [q["act"], q["area"], q["boss"], q["reward"], q["prio"], "Pendente"], zebra=(i % 2 == 1))
    dvs.add(f"F{r}"); ws.cell(r, 5).alignment = CENTER; ws.cell(r, 6).alignment = CENTER
qe = 3 + len(D.QUESTS)
ws.conditional_formatting.add(f"E4:E{qe}", CellIsRule(operator="equal", formula=['"CRÍTICA"'], fill=fill(C["redL"]), font=Font(name=F, color=C["red"], bold=True)))
ws.conditional_formatting.add(f"F4:F{qe}", CellIsRule(operator="equal", formula=['"Feito"'], fill=fill(C["okL"]), font=Font(name=F, color=C["ok"], bold=True)))
ws.conditional_formatting.add(f"A4:D{qe}", FormulaRule(formula=['$F4="Feito"'], font=Font(name=F, color="9AA5A1", strike=True)))
ws.freeze_panes = "A4"; ws.auto_filter.ref = f"A3:F{qe}"

# ============================================================ TRICKS
ws = sheet("Tricks Pro", [14, 11, 32, 90], C["red"])
banner(ws, "TRICKS DE PROFISSIONAL", "O que streamers e jogadores de topo fazem para ganhar tempo, dano e segurança.", 4)
header(ws, 3, ["Categoria", "Nível", "Trick", "Como fazer"])
for i, t in enumerate(D.TRICKS):
    r = 4 + i
    put(ws, r, [t["cat"], t["lvl"], t["title"], t["body"]], height=est_h([t["body"]], [90]))
    ws.cell(r, 3).font = font(bold=True); ws.cell(r, 2).alignment = CENTER
te = 3 + len(D.TRICKS)
for txt, col in [("Fácil", C["okL"]), ("Médio", C["goldL"]), ("Avançado", C["redL"])]:
    ws.conditional_formatting.add(f"B4:B{te}", CellIsRule(operator="equal", formula=[f'"{txt}"'], fill=fill(col)))
ws.freeze_panes = "A4"; ws.auto_filter.ref = f"A3:D{te}"

# ============================================================ DIAGNÓSTICO
ws = sheet("Diagnóstico", [36, 70, 4, 34, 60], C["red"])
banner(ws, "DIAGNÓSTICO — o dano caiu? algo deu errado?", "Sintoma → causa provável → correção. Abaixo, análise do seu setup atual (imagens do seu setup).", 5)
header(ws, 3, ["Sintoma", "O que fazer", "", "", ""])
for i, (q, a) in enumerate(D.TROUBLESHOOT):
    put(ws, 4 + i, [q, a, "", "", ""], bold_first=True, height=34)
r = 5 + len(D.TROUBLESHOOT)
section(ws, r, "SEU SETUP ATUAL — análise", 5, C["gold"]); r += 1
import os
for it in D.CURRENT_SETUP["items"]:
    ws.cell(r, 1, it["what"]).font = font(bold=True); ws.cell(r, 1).alignment = WRAP
    ws.cell(r, 2, it["verdict"]).alignment = WRAP
    p = os.path.join("media", it["img"])
    img = XLImage(p); img.width, img.height = int(img.width * 0.62), int(img.height * 0.62)
    ws.add_image(img, f"D{r}")
    ws.row_dimensions[r].height = max(img.height * 0.78, 60)
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=2)
    r += 1

# ============================================================ ATLAS
ws = sheet("Atlas", [18, 50, 40], C["jade"])
banner(ws, "ATLAS — checklist e árvore", "Da entrada no T1 até Uber Arbiter. Nós do Atlas conforme o guia T15+ (0.5.5).", 3)
header(ws, 3, ["Etapa", "Meta", "Upgrade-chave"])
for i, a in enumerate(D.DATA["atlasCheck"]):
    put(ws, 4 + i, [a["stage"], a["goal"], a["gear"]], bold_first=True, height=30)
r = 5 + len(D.ATLAS_CHECK)
section(ws, r, "ÁRVORE DO ATLAS", 3); r += 1
header(ws, r, ["Grupo", "Nó", ""]); r += 1
for grp, nodes in D.ATLAS.items():
    for n in nodes:
        put(ws, r, [grp, n, ""]); ws.cell(r, 1).font = font(bold=True, color=C["jade"]); r += 1

# ============================================================ OTIMIZAÇÕES + META + UNIQUES
ws = sheet("Otimizações & Meta", [6, 44, 40, 58, 44], C["red"])
banner(ws, "NOSSA ROTA OTIMIZADA — o que mudou e por quê", f"Baseado em {D.META['effigy_pop']} Spirit Walkers com Sylvan's Effigy + 24 zoos nível 98–99 da liga {D.META['league']} (poe.ninja, {D.SNAP}).", 5)
header(ws, 3, ["#", "Otimização", "Evidência (dados)", "Por quê", "Guia base dizia"])
for i, o in enumerate(D.OPTIMIZATIONS):
    r = 4 + i
    put(ws, r, [i + 1, o["t"], o["ev"], o["why"], o["was"]], height=est_h([o["why"], o["ev"]], [58, 40]))
    ws.cell(r, 2).font = font(bold=True, color=C["gold"]); ws.cell(r, 1).alignment = CENTER
    ws.cell(r, 5).font = font(italic=True, color=C["mute"])
r = 5 + len(D.OPTIMIZATIONS)
for ch in D.META["charts"] + [{"title": "Supports no Zekoa", "rows": D.META["zekoaLinks"]}, {"title": "Notables mais comuns (24 zoos top)", "rows": D.META["sample"]["notables"]}]:
    section(ws, r, ch["title"].upper() + "  (% de uso)", 5); r += 1
    first = r
    for n, v in ch["rows"]:
        ws.cell(r, 2, n).font = font(); ws.cell(r, 3, v / 100).number_format = "0%"
        for col in (2, 3): ws.cell(r, col).border = BOX
        r += 1
    ws.conditional_formatting.add(f"C{first}:C{r-1}", DataBarRule(start_type="num", start_value=0, end_type="num", end_value=1, color=C["gold"]))
    r += 1

ws = sheet("Uniques", [7, 24, 20, 11, 11, 11, 16, 50, 46, 40], C["gold"])
banner(ws, "UNIQUES DA BUILD — preço real, uso no meta e quando entram", f"Preços em Divine Orb (1 div ≈ 353 Exalted) no poe.ninja em {D.SNAP}. 'Uso' = % dos zoos com Sylvan's Effigy. Filtre por Fase/Faixa.", 10)
header(ws, 3, ["", "Unique", "Slot", "Faixa", "Preço (div)", "Uso", "Fase", "Por quê", "Mods principais", "Como / versões"])
PHN = {p["id"]: p["name"] for p in PH}
order = {p["id"]: i for i, p in enumerate(PH)}
for i, u in enumerate(sorted(D.UNIQUES, key=lambda u: (order.get(u["p"], 99), u["price"] or 0))):
    r = 4 + i
    put(ws, r, ["", u["n"], u["slot"], u["tier"], u["price"], (u["use"] / 100) if u["use"] is not None else "—", PHN.get(u["p"], u["p"]), u["why"], "\n".join(u["mods"]), u["rf"] + (" · " + u["how"] if u["how"] else "")],
        height=max(56, est_h([u["why"], "\n".join(u["mods"]), u["rf"] + u["how"]], [50, 46, 40])))
    ws.cell(r, 2).font = font(bold=True, color="AF6025"); ws.cell(r, 5).number_format = "0.000"; ws.cell(r, 6).number_format = "0%"
    for col in (4, 5, 6): ws.cell(r, col).alignment = CENTER
ue = 3 + len(D.UNIQUES)
for txt, col in [("Barato", C["okL"]), ("Valor", C["goldL"]), ("Luxo", C["redL"])]:
    ws.conditional_formatting.add(f"D4:D{ue}", CellIsRule(operator="equal", formula=[f'"{txt}"'], fill=fill(col)))
ws.freeze_panes = "C4"; ws.auto_filter.ref = f"A3:J{ue}"
UNIQ_SHEET = ws
r = ue + 2
section(ws, r, "IDOLS E SOUL CORES", 10); r += 1
header(ws, r, ["", "Idol", "Onde", "", "Preço (div)", "", "", "Efeito", "", ""]); r += 1
IDOL_ROW0 = r
for i2 in D.IDOLS:
    put(ws, r, ["", i2["n"], i2["where"], "", i2["price"], "", "", i2["eff"], "", ""], height=34)
    ws.cell(r, 2).font = font(bold=True); ws.cell(r, 5).number_format = "0.000"; r += 1

# ============================================================ PASSIVAS & ITENS (dados do planner)
import json as _json, base64 as _b64, io as _io
from PIL import Image as _PIL
AS = _json.load(open("assets.json", encoding="utf-8"))
def _png(key, size):
    if not key or key not in AS["icons"]: return None
    im = _PIL.open(_io.BytesIO(_b64.b64decode(AS["icons"][key].split(",", 1)[1]))).convert("RGBA")
    im.thumbnail((size, size)); bio = _io.BytesIO(); im.save(bio, "PNG"); bio.seek(0)
    x = XLImage(bio); x.width, x.height = im.size; return x
_sorted_u = sorted(D.UNIQUES, key=lambda u: (order.get(u["p"], 99), u["price"] or 0))
for i, u in enumerate(_sorted_u):
    im = _png(AS["uniqIcon"].get(u["n"]), 44)
    if im: UNIQ_SHEET.add_image(im, f"A{4 + i}")
for j, i2 in enumerate(D.IDOLS):
    im = _png(AS["uniqIcon"].get(i2["n"]), 30)
    if im: UNIQ_SHEET.add_image(im, f"A{IDOL_ROW0 + j}")
ws = sheet("Passivas & Itens", [7, 30, 12, 8, 70, 4], C["gold"])
banner(ws, "PASSIVAS & SETS POR FASE — nossa rota", "Atos 1–2: leveling de spear. Ato 3+: árvore própria (consenso dos 24 zoos top, sem nós de ataque) e sets com uniques no set principal, barato e completo. Árvore visual no app.", 5)
r = 4
SETN = {"m": "Principal", "s1": "Weapon Set I", "s2": "Weapon Set II"}
for p in PH:
    nt = AS["notables"][p["id"]]
    section(ws, r, f"{p['name'].upper()} · {nt['count']} pontos principais" + (f" · {nt['s1']} Set I · {nt['s2']} Set II" if nt["s1"] else ""), 5); r += 1
    header(ws, r, ["", "Notable", "Árvore", "Novo?", "Efeito"]); r += 1
    if p["id"] not in ("a1", "a2"): ws.cell(r - 2, 1).value = ws.cell(r - 2, 1).value + "  ·  árvore própria (zoos top, sem ataque)"
    for n in nt["list"]:
        if n["k"] == 3: continue
        put(ws, r, ["", n["n"] + (" (só passagem)" if n.get("pass") else ""), SETN[n["set"]], "NOVO" if n["new"] else "", " · ".join(n["s"])], height=32)
        ws.cell(r, 2).font = font(bold=True, color=C["ok"] if n["new"] else C["ink"])
        im = _png(n["ic"], 26)
        if im: ws.add_image(im, f"A{r}")
        r += 1
    items_by_mode = [("Set de leveling (spear)", AS["guide"][p["id"]])] if p["id"] not in AS["sets"] else [("Set principal — BARATO", AS["sets"][p["id"]]["cheap"]), ("Set principal — COMPLETO", AS["sets"][p["id"]]["full"])]
    for label, its in items_by_mode:
      header(ws, r, ["", label, "Slot", "Único", "Mods que importam / sockets / nota"], C["gold"]); r += 1
      for it in its:
        txt = (it["x"] or "—") + ("  |  Sockets/versão: " + ", ".join(it["r"]) if it["r"] else "") + ("  |  " + it["note"] if it.get("note") else "")
        put(ws, r, ["", it["n"], it["slot"], "Sim" if it["u"] else "", txt], height=max(40, est_h([txt], [70])))
        ws.cell(r, 2).font = font(bold=True, color="AF6025" if it["u"] else C["ink"])
        im = _png(it["ic"], 34)
        if im: ws.add_image(im, f"A{r}")
        r += 1
    r += 1
ws.freeze_panes = "A4"

# ============================================================ FONTES
ws = sheet("Fontes", [58, 44, 70], C["silver"])
banner(ws, "FONTES", "Pesquisadas em 15/09/2026. Preços de mercado mudam — por isso usamos faixas (Barato / Valor / Completo).", 3)
header(ws, 3, ["Fonte", "Usado para", "Link"])
for i, s in enumerate(D.DATA["sources"]):
    r = 4 + i
    put(ws, r, [s["name"], s["use"], s["url"]], height=30)
    ws.cell(r, 3).hyperlink = s["url"]; ws.cell(r, 3).font = font(color="1F5FBF", underline="single")

wb.active = 0
for w in wb.worksheets:
    w.sheet_view.zoomScale = 100
wb.save(OUT)
print("saved", OUT)
