# Genera index.html (presentazione autonoma per GitHub Pages) da presentazione/deck.json, deck.css e slides/*.html
import json, os, re
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
p = os.path.join(base, 'presentazione')
deck = json.load(open(os.path.join(p, 'deck.json'), encoding='utf-8'))
css = open(os.path.join(p, 'deck.css'), encoding='utf-8').read()
slides = []
for sid in deck['order']:
    h = open(os.path.join(p, 'slides', sid + '.html'), encoding='utf-8').read()
    slides.append(re.sub(r'<aside>.*?</aside>', '', h, flags=re.S))
href = next(iter(deck['faces'].values()))['href']
html = f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PIRadar - Gruppo 10</title>
<link rel="icon" href="pitch/logo_piradar.svg">
<link rel="stylesheet" href="{href}">
<style>
html,body{{margin:0;height:100%;background:#0B1828;overflow:hidden}}
#stage{{position:absolute;left:50%;top:50%;width:1920px;height:1080px;transform-origin:center center}}
#stage>section{{position:absolute;inset:0;width:1920px;height:1080px;display:none}}
#stage>section.on{{display:flex}}
{css}
#bar{{position:fixed;right:16px;bottom:12px;font:14px Inter,Arial,sans-serif;color:#8FA3B1;user-select:none}}
#bar a{{color:#3FC1B0}}
</style></head><body>
<div id="stage">
{''.join(slides)}
</div>
<div id="bar"><span id="n"></span> · ← → per cambiare slide · F schermo intero · <a href="https://github.com/EliseyRotar/piradar-basf-hackathon">repo</a></div>
<script>
const s=[...document.querySelectorAll('#stage>section')];let i=0;
function fit(){{const k=Math.min(innerWidth/1920,innerHeight/1080);document.getElementById('stage').style.transform='translate(-50%,-50%) scale('+k+')'}}
function show(j){{i=Math.max(0,Math.min(s.length-1,j));s.forEach((x,k)=>x.classList.toggle('on',k===i));document.getElementById('n').textContent=(i+1)+' / '+s.length;history.replaceState(null,'','#'+(i+1))}}
addEventListener('resize',fit);
addEventListener('keydown',e=>{{if(['ArrowRight','PageDown',' '].includes(e.key))show(i+1);if(['ArrowLeft','PageUp'].includes(e.key))show(i-1);if(e.key==='f'||e.key==='F')document.documentElement.requestFullscreen?.()}});
addEventListener('click',e=>{{if(e.target.closest('a'))return;show(e.clientX>innerWidth/2?i+1:i-1)}});
fit();show((parseInt(location.hash.slice(1))||1)-1);
</script></body></html>"""
open(os.path.join(base, 'index.html'), 'w', encoding='utf-8').write(html)
print('index.html creato con', len(slides), 'slide')
