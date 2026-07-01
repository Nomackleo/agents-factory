import os
import sys
import time
import json
import subprocess
from playwright.sync_api import sync_playwright

PROFILE_DIR = os.path.expanduser('~/.notebooklm-mcp-cli/profiles/default')
os.makedirs(PROFILE_DIR, exist_ok=True)

print('Cerrando Brave para liberar el perfil de usuario...')
subprocess.run('taskkill /F /IM brave.exe /T', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(2)

# User's actual Brave profile path
USER_DATA_DIR = r'C:\Users\Nomack\AppData\Local\BraveSoftware\Brave-Browser\User Data'
BRAVE_EXE = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'

with sync_playwright() as p:
    print('Abriendo tu sesión activa de Brave en segundo plano...')
    # Use persistent context with user's actual data dir to bypass Google login completely
    context = p.chromium.launch_persistent_context(
        user_data_dir=USER_DATA_DIR,
        executable_path=BRAVE_EXE,
        headless=False,
        args=['--disable-blink-features=AutomationControlled']
    )
    
    page = context.pages[0] if context.pages else context.new_page()
    print('Navegando a NotebookLM...')
    page.goto('https://notebooklm.google.com/')

    print('Esperando a que la página cargue los cuadernos...')
    # We wait for the logo or text to ensure we are fully logged in
    page.wait_for_selector('text=NotebookLM', timeout=15000)
    page.wait_for_load_state('networkidle')
    time.sleep(2)
    
    print('Extrayendo cookies y tokens de tu sesión existente...')
    cookies = context.cookies()
    
    try:
        csrf = page.evaluate("window.WIZ_global_data ? window.WIZ_global_data.SNlM0e : ''")
    except:
        csrf = ''
        
    profile = {
        'name': 'default',
        'cookies': cookies,
        'csrf_token': csrf,
        'session_id': '',
        'email': 'user',
    }
    
    profile_path = os.path.join(PROFILE_DIR, 'profile.json')
    with open(profile_path, 'w') as f:
        json.dump(profile, f)
        
    print(f'¡Perfil guardado en {profile_path}!')
    context.close()
