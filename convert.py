import re

with open('frontend/src/pages/raw_body.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace class= with className=
html = html.replace('class=', 'className=')
# Replace for= with htmlFor=
html = html.replace('for=', 'htmlFor=')
# Replace tabindex= with tabIndex=
html = html.replace('tabindex=', 'tabIndex=')
# Replace onclick= with onClick=
html = html.replace('onclick=', 'onClick=')

# Self close img tags
html = re.sub(r'(<img[^>]*?)(?<!/)>', r'\1 />', html)
# Self close input tags
html = re.sub(r'(<input[^>]*?)(?<!/)>', r'\1 />', html)
# Self close hr tags
html = re.sub(r'(<hr[^>]*?)(?<!/)>', r'\1 />', html)
# Self close br tags
html = re.sub(r'(<br[^>]*?)(?<!/)>', r'\1 />', html)

# Convert inline styles
def repl_style(m):
    style_str = m.group(1)
    parts = style_str.split(';')
    obj = []
    for p in parts:
        if ':' in p:
            k, v = p.split(':', 1)
            k = k.strip()
            v = v.strip()
            if '-' in k and not k.startswith('--'):
                pts = k.split('-')
                k = pts[0] + ''.join(x.title() for x in pts[1:])
            obj.append(f"'{k}': '{v}'")
    return 'style={{ ' + ', '.join(obj) + ' }}'

html = re.sub(r'style="([^"]*)"', repl_style, html)

# Handle image imports
html = html.replace('"farmer-planting-seedling.jpg"', '{farmerImg}')
html = html.replace('"farmers-rice-field.jpg"', '{riceImg}')

jsx = f"""import React from 'react';
import {{ useNavigate }} from 'react-router-dom';
import './LandingPage.css';
import farmerImg from '../assets/farmer-planting-seedling.jpg';
import riceImg from '../assets/farmers-rice-field.jpg';

export default function LandingPage() {{
    const navigate = useNavigate();

    return (
        <div className="landing-wrapper">
            {html}
        </div>
    );
}}
"""

# Now write it
with open('frontend/src/pages/LandingPage.jsx', 'w', encoding='utf-8') as f:
    f.write(jsx)

print('Conversion complete')
