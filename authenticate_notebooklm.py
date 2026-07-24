import os
import subprocess
import time
import sys

print('1. Liberando el proceso de Brave para evitar el bloqueo de perfil (ProcessSingleton)...')
subprocess.run('taskkill /F /IM brave.exe /T', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(2)

print('2. Configurando nlm para usar Brave Browser...')
subprocess.run(['C:\\Users\\Nomack\\.local\\bin\\nlm.exe', 'config', 'set', 'auth.browser', 'brave'], check=True)

print('\n=====================================================================')
print('Lanzando autenticación con NotebookLM para nomack3d@gmail.com...')
print('INSTRUCCIÓN:')
print('1. En la ventana de Brave que se abrirá, inicia sesión con nomack3d@gmail.com.')
print('2. Una vez entres a tu panel de NotebookLM, CIERRA la ventana de Brave.')
print('=====================================================================\n')

process = subprocess.Popen(
    ['C:\\Users\\Nomack\\.local\\bin\\nlm.exe', 'login', '-p', 'nomack3d'],
    stdout=sys.stdout, stderr=sys.stderr
)
process.wait()

print('\n3. Estableciendo nomack3d como perfil predeterminado en nlm...')
subprocess.run(['C:\\Users\\Nomack\\.local\\bin\\nlm.exe', 'login', 'switch', 'nomack3d'], check=True)

print('\n¡Autenticación para nomack3d@gmail.com completada con éxito!')



