#!/usr/bin/env python3
"""Genera los iconos PWA de ABISMO (bola de bolos azul sobre fondo navy)."""
import math
from PIL import Image, ImageDraw, ImageFilter

OUT = "/Users/clickcom/Documents/abismo"

def hex2rgb(h):
    h = h.lstrip('#')
    return (int(h[0:2],16), int(h[2:4],16), int(h[4:6],16))

def lerp(a,b,t): return a+(b-a)*t

STOPS = [(0.0,'#eaf4ff'),(0.26,'#5f9fe0'),(0.60,'#2a54a8'),(1.0,'#0a1838')]
STOPS = [(o,hex2rgb(c)) for o,c in STOPS]

def sample(t):
    t = 0.0 if t<0 else 1.0 if t>1 else t
    for i in range(len(STOPS)-1):
        o0,c0 = STOPS[i]; o1,c1 = STOPS[i+1]
        if t <= o1:
            f = 0 if o1==o0 else (t-o0)/(o1-o0)
            return tuple(int(round(lerp(c0[k],c1[k],f))) for k in range(3))
    return STOPS[-1][1]

def make(size):
    S = size
    img = Image.new('RGB',(S,S),hex2rgb('#0a1024'))
    px = img.load()
    # resplandor inferior (tipo farola)
    gcx,gcy,gr = S*0.5, S*0.92, S*0.72
    gc = (90,150,230)
    for y in range(S):
        for x in range(S):
            d = math.hypot(x-gcx,y-gcy)/gr
            if d < 1:
                a = (1-d)*0.28
                r,g,b = px[x,y]
                px[x,y] = (min(255,int(r+gc[0]*a)), min(255,int(g+gc[1]*a)), min(255,int(b+gc[2]*a)))
    # esfera (bola de bolos)
    cx,cy,rad = S*0.5, S*0.5, S*0.30
    hlx,hly = cx-rad*0.34, cy-rad*0.40   # foco de luz
    for y in range(max(0,int(cy-rad-2)), min(S,int(cy+rad+2))):
        for x in range(max(0,int(cx-rad-2)), min(S,int(cx+rad+2))):
            dx,dy = x-cx, y-cy
            if dx*dx+dy*dy <= rad*rad:
                t = math.hypot(x-hlx,y-hly)/rad
                px[x,y] = sample(t)
    draw = ImageDraw.Draw(img)
    # agujeros de dedos
    for ox,oy in [(-0.16,-0.05),(0.16,-0.05),(0.0,0.22)]:
        hx,hy = cx+ox*rad, cy+oy*rad; hr = rad*0.135
        draw.ellipse([hx-hr,hy-hr,hx+hr,hy+hr], fill=hex2rgb('#0a1526'))
    # brillo especular
    sx,sy,srr = cx-rad*0.34, cy-rad*0.40, rad*0.22
    for y in range(max(0,int(sy-srr)), min(S,int(sy+srr))):
        for x in range(max(0,int(sx-srr)), min(S,int(sx+srr))):
            d = math.hypot(x-sx,y-sy)/srr
            if d < 1:
                a = (1-d)**1.6
                r,g,b = px[x,y]
                px[x,y] = (min(255,int(r+(255-r)*a)), min(255,int(g+(255-g)*a)), min(255,int(b+(255-b)*a)))
    return img

for size, name in [(512,'icon-512.png'), (192,'icon-192.png'), (180,'apple-touch-icon.png')]:
    make(size).save(f"{OUT}/{name}")
    print("escrito", name)
print("OK")
