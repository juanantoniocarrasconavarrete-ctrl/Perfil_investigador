import re,sys,pandas as pd
sys.argv=['x',"/root/.claude/uploads/9462aa68-959c-58ec-9a87-48f8e4e0cd6c/7453a60c-Proyecto_La_Puerta_-_Base_de_Datos_y_Matriz_de_An_lisis_20261009_1658_1.xlsx"]
src=open('analisis.py').read().split('# ---------- cualitativo ----------')[1].split('def code')[0]
raw=pd.read_excel(sys.argv[1],sheet_name='Form Responses 1'); C=list(raw.columns)
df=pd.DataFrame({'abi1':raw[C[24]],'abi2':raw[C[25]]})
exec("import re\ndef has(s, pats): return bool(re.search('|'.join(pats), s, flags=re.I)) if isinstance(s, str) else False\n"+src)
for col,T in [('abi1',T1),('abi2',T2)]:
    for k,p in T.items():
        m=df[col].apply(lambda s:has(s,p)); print('##',col,k,m.sum())
        if k.startswith(('Visión','Sin','Talleres','Simul','Software','Brecha')):
            for s in df.loc[m,col].head(14): print('   ·',s[:110].replace('\n',' '))
