// Hand-drawn marker accents generated with Rough.js (MIT, github.com/rough-stuff/rough).
// Usage: node make_rough.js <out.json>  (run with NODE_PATH pointing at a node_modules that has roughjs)
const rough = require('roughjs');
const fs = require('fs');

const gen = rough.generator();
const opts = (seed, extra = {}) => ({ seed, roughness: 1.6, bowing: 1.4, strokeWidth: 3, stroke: '#000', ...extra });
const paths = d => gen.toPaths(d).map(p => p.d);

const out = {
  // loose double-stroke ellipse to circle a word (viewBox 0 0 200 80)
  ellipse: paths(gen.ellipse(100, 40, 188, 66, opts(3))),
  // scribbled underline (viewBox 0 0 200 20)
  underline: paths(gen.linearPath([[4, 12], [70, 8], [140, 13], [196, 7]], opts(11, { roughness: 2.2 }))),
  // hand-drawn arrow (viewBox 0 0 120 60)
  arrow: paths(gen.curve([[6, 50], [40, 20], [80, 14], [108, 22]], opts(5, { roughness: 1.2 })))
    .concat(paths(gen.linearPath([[94, 10], [110, 22], [96, 34]], opts(6, { roughness: .8 })))),
};
fs.writeFileSync(process.argv[2], JSON.stringify(out));
console.log('wrote rough accents');
