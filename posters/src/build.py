"""Build self-contained poster HTML files, then render A4 PDF + PNG.

Usage: python3 posters/src/build.py
"""
import base64
import json
import re
import subprocess
from pathlib import Path

SRC = Path(__file__).resolve().parent
OUT = SRC.parent
POSTERS = ["poster-1-focus", "poster-2-marathon", "poster-3-gita"]
ART = SRC / "art"

HELPER = """
<div class="helper no-print">
  <button onclick="window.print()">Print / Save as PDF (A4)</button>
  <button onclick="document.querySelector('.photo-input').click()">Add founder photo</button>
  Click the photo frame, or paste an image (Ctrl/Cmd+V), to place Dr. Velumani's photo. It is shown in grayscale.
  When printing: paper A4, margins None, scale 100%, background graphics ON.
</div>
<script>
(function () {
  var frame = document.querySelector('.photo');
  function show(file) {
    if (!file || !/^image\\//.test(file.type)) return;
    var r = new FileReader();
    r.onload = function () {
      var img = frame.querySelector('.photo-img');
      if (!img) { img = document.createElement('img'); img.className = 'photo-img'; img.alt = ''; frame.appendChild(img); }
      img.src = r.result;
    };
    r.readAsDataURL(file);
  }
  frame.querySelector('.photo-input').addEventListener('change', function (e) { show(e.target.files[0]); });
  document.addEventListener('paste', function (e) {
    var items = (e.clipboardData || {}).items || [];
    for (var i = 0; i < items.length; i++) if (items[i].type.indexOf('image') === 0) show(items[i].getAsFile());
  });
})();
</script>
"""


def inline_css() -> str:
    css = (SRC / "poster.css").read_text()

    def embed(m):
        data = base64.b64encode((SRC / m.group(1)).read_bytes()).decode()
        return f'url("data:font/ttf;base64,{data}")'

    return re.sub(r'url\("(fonts/[^"]+)"\)', embed, css)


def icon(name):
    svg = (ART / "icons" / f"{name}.svg").read_text()
    svg = re.sub(r'\s(width|height|class)="[^"]*"', "", svg, count=3)
    return svg.replace("<svg", f'<svg class="ico ico-{name}" aria-hidden="true"', 1)


def rough(name):
    boxes = {"ellipse": "0 0 200 80", "underline": "0 0 200 20", "arrow": "0 0 120 60"}
    d = "".join(f'<path d="{p}" vector-effect="non-scaling-stroke"/>' for p in json.loads((ART / "rough.json").read_text())[name])
    return (f'<svg class="rough rough-{name}" viewBox="{boxes[name]}" preserveAspectRatio="none" aria-hidden="true">'
            f'<g fill="none" stroke="#000" stroke-width="3" stroke-linecap="round">{d}</g></svg>')


def expand(html):
    html = re.sub(r"\{\{icon:([\w-]+)\}\}", lambda m: icon(m.group(1)), html)
    html = re.sub(r"\{\{rough:(\w+)\}\}", lambda m: rough(m.group(1)), html)
    html = re.sub(r"\{\{path:([\w-]+)\}\}", lambda m: re.search(r' d="([^"]+)"', (ART / "icons" / f"{m.group(1)}.svg").read_text()).group(1), html)
    return re.sub(r"\{\{art:(\w+)\}\}", lambda m: (ART / f"{m.group(1)}.svg").read_text(), html)


def main():
    css = inline_css()
    founder = (SRC / "founder.html").read_text()
    for name in POSTERS:
        html = (SRC / f"{name}.html").read_text()
        html = html.replace('<link rel="stylesheet" href="poster.css">', f"<style>{css}</style>")
        html = expand(html.replace("{{FOUNDER}}", founder).replace("{{HELPER}}", HELPER))
        (OUT / f"{name}.html").write_text(html)
    subprocess.run(["node", str(SRC / "render.js"), str(OUT), *POSTERS], check=True)


if __name__ == "__main__":
    main()
