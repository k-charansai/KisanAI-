with open('frontend/src/pages/LandingPage.jsx', 'r', encoding='utf-8') as f:
    jsx = f.read()

# Make 'Start Diagnosis' buttons work via React router
jsx = jsx.replace('href="#"', 'onClick={() => navigate(\'/diagnose\')}')
jsx = jsx.replace('href="/diagnose"', 'onClick={() => navigate(\'/diagnose\')}')

# Remove empty onclick attributes that might have been copied
jsx = jsx.replace('onClick=""', '')
jsx = jsx.replace('onclick=""', '')

with open('frontend/src/pages/LandingPage.jsx', 'w', encoding='utf-8') as f:
    f.write(jsx)
print('Navigation links updated')
