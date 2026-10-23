import re,sys
D=sys.argv[1]
E=open(D+'/ementario_adm.tex',encoding='utf-8').read()
M=open(D+'/main_ppc_administracao.tex',encoding='utf-8').read()
clean=lambda t: re.sub(r'\\revisao\{|\\textbf\{|\}','',t).strip()
h=lambda t:int(clean(t).replace('.','').replace(' h','').strip())
# --- matriz
mat={}; probs=[]
for ano,(a,b) in enumerate([('QUADRO 3','QUADRO 4'),('QUADRO 4','QUADRO 5'),('QUADRO 5','QUADRO 6:')],1):
    blk=E[E.index(a):E.index(b)]
    s1=s2=tt=0; rows=[]
    for line in blk.split('\n'):
        c=[x.strip() for x in line.replace('\\\\ \\hline','').split('&')]
        if len(c)==5 and 'Bloco Curricular' not in line and 'Subtotais' not in line and 'Sem.' not in line:
            uc=clean(c[0]).replace('--','—').rstrip('*'); bl=clean(c[1]); a1,a2,t=h(c[2]),h(c[3]),h(c[4])
            if a1+a2!=t: probs.append(f'Ano {ano}: {uc}: {a1}+{a2}≠{t}')
            for v in (a1,a2,t):
                if v%20: probs.append(f'Ano {ano}: {uc}: {v} h não é múltiplo de 20')
            s1+=a1;s2+=a2;tt+=t; mat[uc]=(ano,bl,a1,a2,t)
        if 'Subtotais' in line:
            c=line.split('&'); d1,d2,dt=h(c[1]),h(c[2]),h(c[3].replace('\\\\ \\hline',''))
            ok=(d1,d2,dt)==(s1,s2,tt)
            print(f'Ano {ano}: soma das linhas {s1}/{s2}/{tt} h · declarado {d1}/{d2}/{dt} h · {"OK" if ok else "DIVERGE"}')
            if not ok: probs.append(f'Ano {ano}: subtotais divergentes')
blocos={}
for uc,(ano,bl,a1,a2,t) in mat.items(): blocos[bl]=blocos.get(bl,0)+t
print('Por bloco (matriz):',blocos,'· total',sum(blocos.values()))
# --- ementas
em={}
for m in re.finditer(r'Unidade Curricular:\}\}\\\\\[3pt\]\\textbf\{\\large ([^\n]*?)\}\} & .*?Semestre:\}\} \\textbf\{([^}]*)\}.*?\\\\ \\cline\{2-3\}\s*& \\textbf\{[^}]*\} & (?:\\revisao\{)?\\textbf\{(?:\\revisao\{)?(\d+) h\}',E,re.S):
    nm=clean(m.group(1)).replace('\\revisao{',''); em[nm]=(m.group(2),int(m.group(3)))
print('Ementas encontradas:',len(em),'· UCs na matriz:',len(mat))
for uc,(ano,bl,a1,a2,t) in mat.items():
    if uc not in em: probs.append(f'Sem ementa: {uc}'); continue
    sem,ch=em[uc]
    if ch!=t: probs.append(f'CH diverge: {uc}: matriz {t} h × ementa {ch} h')
    base=2*ano-1; esperado=('%dº e %dº'%(base,base+1)) if a1 and a2 else ('%dº'%(base) if a1 else '%dº'%(base+1))
    if not clean(sem).replace(' ','').startswith(esperado.replace(' ','')): probs.append(f'Semestre diverge: {uc}: matriz {esperado} × ementa {sem}')
for nm in em:
    if nm in mat: continue
    if nm.startswith('Libras'):
        ano=nm.split('Ano ')[-1].rstrip('*'); esp=f'Espanhol — Ano {ano}'
        ok=esp in mat and em[nm][1]==mat[esp][4] and em[nm][0]==em[esp][0]
        print(f'{nm} substitui {esp}: CH {em[nm][1]} h e semestre {em[nm][0]}', 'OK' if ok else 'DIVERGE')
        if not ok: probs.append(f'{nm} não bate com {esp}')
    else: probs.append(f'Ementa sem linha na matriz: {nm}')
# --- síntese e quadro 6A
sint=E[E.index('QUADRO 6:'):E.index('QUADRO 6A')]
for rot,chave in [('Formação Geral','Formação Geral'),('Formação Técnica Profissional','Formação Técnica'),('Núcleo Politécnico','Núcleo Politécnico')]:
    m=re.search(re.escape(rot)+r' & \\revisao\{([\d.]+) h\} & \\revisao\{([\d,]+) \\%',sint)
    v=int(m.group(1).replace('.','')); pc=float(m.group(2).replace(',','.'))
    real=blocos[chave]; pr=round(real*100/sum(blocos.values()),2)
    print(f'Síntese {rot}: {v} h ({pc}%) · matriz {real} h ({pr}%)',' OK' if (v,pc)==(real,pr) else ' DIVERGE')
    if (v,pc)!=(real,pr): probs.append(f'Síntese {rot} diverge')
q=E[E.index('QUADRO 6A'):E.index('QUADRO 6A')+3000]
ft=blocos['Formação Técnica']+120; fg=blocos['Formação Geral']+40
for txt in [f'{blocos["Formação Técnica"]} h',f'{ft} h',f'{fg:,}'.replace(',','.')+' h','3.120 h']:
    print(f'Quadro 6A contém "{txt}":', txt in q)
    if txt not in q: probs.append(f'Quadro 6A sem {txt}')
# --- textos do PPC
tot=f'{sum(blocos.values()):,}'.replace(',','.')
for rotulo,pat in [('7.6 CH Total',r'7\.6\. CH Total:.*?\\revisao\{([\d.]+) horas\}'),('7.6.1 CH presencial',r'7\.6\.1 CH Aulas presenciais\}\} & \\revisao\{([\d.]+) horas\}')]:
    m=re.search(pat,M,re.S); v=m.group(1) if m else None
    print(f'{rotulo}: {v}', 'OK' if v==tot else 'DIVERGE')
    if v!=tot: probs.append(f'{rotulo} diverge')
for n in sorted(set(re.findall(r'(\d\.\d{3}) horas',M))): print('Menção no texto:',n,'horas ×',len(re.findall(re.escape(n)+' horas',M)))
print('\nPROBLEMAS:' if probs else '\nNenhuma divergência encontrada.')
for p in probs: print(' -',p)
