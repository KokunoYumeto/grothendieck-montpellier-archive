#!/usr/bin/env python3
"""Trace the observed contour for sourceglyph{119A}; no alphabet is assigned.

The input is an enlarged crop of the first rounded glyph in scan
scans/esq_119_042_a.jpg. Crop coordinates below refer to that reviewed 250x305
pixel detail, not to the complete page. The resulting TeX embeds a vector only.
"""
import argparse,collections,hashlib,json,pathlib
import numpy as np
from PIL import Image
from matplotlib.figure import Figure

def rdp(points,tolerance):
    if len(points)<3:return points
    a=points[0];b=points[-1];delta=b-a;length=np.linalg.norm(delta)
    distances=np.linalg.norm(points-a,axis=1) if length==0 else np.abs(delta[0]*(a[1]-points[:,1])-(a[0]-points[:,0])*delta[1])/length
    index=int(np.argmax(distances))
    if distances[index]>tolerance:return np.vstack((rdp(points[:index+1],tolerance)[:-1],rdp(points[index:],tolerance)))
    return np.array([a,b])

def main(crop,output,record):
    image=Image.open(crop).convert('L');box=(38,80,146,199);pixels=np.array(image.crop(box));mask=pixels<125
    seen=set();components=[]
    for y,x in zip(*np.nonzero(mask)):
        if (y,x) in seen:continue
        stack=[(y,x)];seen.add((y,x));part=[]
        while stack:
            p=stack.pop();part.append(p)
            for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
                q=(p[0]+dy,p[1]+dx)
                if 0<=q[0]<mask.shape[0] and 0<=q[1]<mask.shape[1] and mask[q] and q not in seen:seen.add(q);stack.append(q)
        components.append(part)
    isolated=mask.astype(float)
    isolated=np.pad(isolated,1)
    figure=Figure();ax=figure.subplots();contour=ax.contour(isolated,levels=[.5]);paths=contour.allsegs[0]
    allpoints=np.vstack(paths);xmin,ymin=allpoints.min(axis=0);xmax,ymax=allpoints.max(axis=0)
    commands=[];vertices=[]
    for path in paths:
        # Split a closed curve at its furthest point before applying a small,
        # explicitly recorded polygon tolerance.
        start=path[0];split=int(np.argmax(np.linalg.norm(path-start,axis=1)))
        clean=np.vstack((rdp(path[:split+1],.45)[:-1],rdp(path[split:],.45)))
        points=[((x-xmin)/10,(ymax-y)/10) for x,y in clean]
        commands.append(' -- '.join(f'({x:.3f},{y:.3f})' for x,y in points)+' -- cycle')
        vertices.append(len(points))
    tex=r'''% Observed rounded source glyph, cote 119, site 42, PDF page 43.
% Its conventional alphabet assignment remains uncertain; use with \unsure.
% The contour is a vector traced from the reviewed scan detail, not a font alias.
\makeatletter
\newcommand{\sourceglyph}[1]{\mathord{\mathpalette{\EditionSourceGlyph{#1}}{}}}
\newcommand{\EditionSourceGlyph}[3]{%
  \begingroup
  \setbox0=\hbox{$#2 A$}%
  \resizebox{!}{\ht0}{\csname EditionGlyph@#1\endcsname}%
  \endgroup}
\expandafter\newcommand\csname EditionGlyph@119A\endcsname{%
  \begin{tikzpicture}[x=1pt,y=1pt,baseline=0pt]
  \path[fill,even odd rule]
'''+ '\n'.join(commands)+r''';
  \end{tikzpicture}}
\makeatother
'''
    output.parent.mkdir(parents=True,exist_ok=True);output.write_text(tex)
    data={'glyph_id':'119A','source_scan':'scans/esq_119_042_a.jpg','source_pdf_page':43,'typescript_page':40,'crop_sha256':hashlib.sha256(pathlib.Path(crop).read_bytes()).hexdigest(),'reviewed_crop_size':list(image.size),'detail_box':list(box),'luminance_threshold':125,'connectivity':4,'component':'all dark components in the isolated glyph box','component_areas_pixels':sorted([len(c) for c in components],reverse=True),'polygon_tolerance_pixels':.45,'vertices_by_contour':vertices,'source_alphabet':'unresolved; explicitly marked with unsure','vector_tex_sha256':hashlib.sha256(tex.encode()).hexdigest()}
    record.parent.mkdir(parents=True,exist_ok=True);record.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'glyph_id':'119A','vertices':vertices,'contours':len(paths)}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('crop',type=pathlib.Path);p.add_argument('output',type=pathlib.Path);p.add_argument('record',type=pathlib.Path);a=p.parse_args();main(a.crop,a.output,a.record)
