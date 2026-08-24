with open('frontend/src/pages/LandingPage.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace escaped quotes and backslashes
content = content.replace('\"', '"')
content = content.replace('\\', '')

with open('frontend/src/pages/LandingPage.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Sanitized LandingPage.jsx')
