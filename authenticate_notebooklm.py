import os
import subprocess
import time
import sys

print('Terminando procesos de Brave para liberar el puerto 9222...')
subprocess.run('taskkill /F /IM brave.exe /T', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

time.sleep(2)

print('Configurando nlm para usar brave...')
subprocess.run(['C:\\Users\\Nomack\\.local\\bin\\nlm.exe', 'config', 'set', 'auth.browser', 'brave'], check=True)

print('Lanzando autenticación...')
# Run the login command and wait for it to finish
# We do NOT run in background, we let it open the browser so the user can login.
process = subprocess.Popen(
    ['C:\\Users\\Nomack\\.local\\bin\\nlm.exe', 'login', '--force', '--clear'],
    stdout=sys.stdout, stderr=sys.stderr
)
process.wait()

print('Proceso completado.')
