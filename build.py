c = open('black-swan-v16.jsx').read()
c = c.replace('import { useState, useEffect, useCallback, useRef } from "react";', 'const { useState, useEffect, useCallback, useRef } = React;')
c = c.replace('export default function BlackSwan', 'function BlackSwan')
c = c.replace('cvRef.current', 'canvasRef.current')
top = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Black Swan v16 OMEGA</title>
<style>html,body,#root{margin:0;padding:0;height:100%;overflow:hidden;background:#050508}</style>
</head>
<body>
<div id="root"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/7.23.9/babel.min.js"></script>
<script type="text/babel" data-presets="react">"""
bot = """
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(React.createElement(BlackSwan));
</script>
</body>
</html>"""
open('index.html','w').write(top + '\n' + c + bot)
print("Done!")
