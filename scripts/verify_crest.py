import numpy as np
from PIL import Image
from scipy import ndimage
FW,FH,COLS,NFR=80,64,10,70
CH='sprites/preview_assets/char'; PREV='_crest_legendary_preview'
struct=np.array([[0,1,0],[1,1,1],[0,1,0]])  # 4-conn
jobs=[('warrior','helmet_rare1','helmet_warrior_legendary2'),
      ('mage','helmet_mage4','helmet_mage_legendary2'),
      ('ranger','helmet_ranger4','helmet_ranger_legendary2')]
def sheet(p): return np.array(Image.open(p).convert('RGBA'))
allok=True
for cls,body,outn in jobs:
    for suf in ('','_f'):
        src=sheet(f'{CH}/{body}{suf}.png'); out=sheet(f'{PREV}/{outn}{suf}.png')
        dropped=0; s_act=0; o_act=0; multi=0; strays=0; crest_frames=0
        for fi in range(NFR):
            r,c=fi//COLS,fi%COLS
            sl=(slice(r*FH,(r+1)*FH),slice(c*FW,(c+1)*FW))
            a_s=src[sl][...,3]>0; a_o=out[sl][...,3]>0
            if a_s.any(): s_act+=1
            if a_o.any(): o_act+=1
            dropped+=int((a_s&~a_o).sum())
            accent=a_o&~a_s
            if accent.any(): crest_frames+=1
            lab_s,n_s=ndimage.label(a_s,struct)
            lab_o,n_o=ndimage.label(a_o,struct)
            if n_o>n_s: multi+=1
            # accent stray: accent pixel whose out-label has NO body pixel
            body_labels=set(np.unique(lab_o[a_s]))
            acc_labels=set(np.unique(lab_o[accent])) if accent.any() else set()
            if acc_labels-body_labels: strays+=int(np.isin(lab_o[accent],list(acc_labels-body_labels)).sum())
        ok = (dropped==0 and s_act==o_act and multi==0 and strays==0)
        allok &= ok
        print(f'{outn}{suf:2}  dropped={dropped}  parity={o_act}/{s_act}  crest_frames={crest_frames}  accent_multi_comp={multi}  accent_strays={strays}  -> {"PASS" if ok else "FAIL"}')
print('\nALL PASS' if allok else '\nSOME FAILED')
