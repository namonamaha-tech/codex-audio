"""Build self-contained poster HTML files, then render A4 PDF + PNG.

Usage: python3 posters/src/build.py
"""
import base64
import re
import subprocess
from pathlib import Path

SRC = Path(__file__).resolve().parent
OUT = SRC.parent
POSTERS = ["poster-1-focus", "poster-2-marathon"]

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


def main():
    css = inline_css()
    founder = (SRC / "founder.html").read_text()
    for name in POSTERS:
        html = (SRC / f"{name}.html").read_text()
        html = html.replace('<link rel="stylesheet" href="poster.css">', f"<style>{css}</style>")
        html = html.replace("{{FOUNDER}}", founder).replace("{{HELPER}}", HELPER)
        (OUT / f"{name}.html").write_text(html)
    subprocess.run(["node", str(SRC / "render.js"), str(OUT), *POSTERS], check=True)


if __name__ == "__main__":
    main()
