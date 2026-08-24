#!/usr/bin/env python3
"""
Antigravity 2.0 - Google Workspace & GCP MCP Verification Script
Comprueba la disponibilidad de APIs de GCP, credenciales de Service Account y configuración MCP.
"""

import os
import sys
import json
import subprocess

def check_gcloud():
    print("==> [1/4] Verificando instalación de gcloud CLI...")
    try:
        res = subprocess.run(["gcloud", "version"], capture_output=True, text=True, check=True)
        print("  [OK] gcloud instalado correctamente.")
    except Exception as e:
        print("  [ERROR] gcloud CLI no está instalado o no está en PATH.")
        return False
    return True

def check_gcp_apis(project_id="alert-tine-501115-p4"):
    print(f"==> [2/4] Verificando APIs habilitadas en proyecto GCP: {project_id}...")
    required_apis = [
        "gmail.googleapis.com",
        "drive.googleapis.com",
        "docs.googleapis.com",
        "sheets.googleapis.com",
        "slides.googleapis.com",
        "calendar-json.googleapis.com",
        "chat.googleapis.com",
        "people.googleapis.com",
        "admin.googleapis.com",
        "iam.googleapis.com"
    ]
    
    try:
        res = subprocess.run(
            ["gcloud", "services", "list", "--enabled", f"--project={project_id}", "--format=json"],
            capture_output=True, text=True, check=True
        )
        enabled_services = [s.get("config", {}).get("name") for s in json.loads(res.stdout)]
        
        missing = []
        for api in required_apis:
            if api in enabled_services:
                print(f"  [OK] {api} está ACTIVA")
            else:
                print(f"  [MISSING] {api} NO está activa")
                missing.append(api)
                
        return len(missing) == 0
    except Exception as e:
        print(f"  [WARNING] No se pudo verificar el proyecto GCP '{project_id}'. Error: {e}")
        return False

def check_tenant_config(config_path):
    print(f"==> [3/4] Verificando archivo de tenants: {config_path}...")
    if not os.path.exists(config_path):
        print(f"  [ERROR] El archivo {config_path} no existe.")
        return False
    
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        tenants = data.get("tenants", {})
        print(f"  [OK] Archivo válido. Inquilinos configurados: {list(tenants.keys())}")
        return True
    except Exception as e:
        print(f"  [ERROR] Error al leer {config_path}: {e}")
        return False

def check_sa_key(key_path):
    print(f"==> [4/4] Verificando clave de Service Account: {key_path}...")
    if not os.path.exists(key_path):
        print(f"  [WARNING] La clave {key_path} aún no ha sido generada.")
        return False
    
    try:
        with open(key_path, "r", encoding="utf-8") as f:
            sa_data = json.load(f)
        client_id = sa_data.get("client_id")
        client_email = sa_data.get("client_email")
        print(f"  [OK] Service Account Email: {client_email}")
        print(f"  [OK] OAuth2 Client ID DWD : {client_id}")
        return True
    except Exception as e:
        print(f"  [ERROR] Error al leer {key_path}: {e}")
        return False

def main():
    print("==================================================================")
    print(" VERIFICACIÓN DE INTEGRACIÓN GOOGLE WORKSPACE & GCP MCP")
    print("==================================================================")
    
    config_dir = os.path.dirname(os.path.abspath(__file__))
    tenants_path = os.path.join(config_dir, "workspace_tenants.json")
    sa_key_path = os.path.expanduser(r"~\.config\gcloud\antigravity-sa-key.json")
    
    r1 = check_gcloud()
    r2 = check_gcp_apis()
    r3 = check_tenant_config(tenants_path)
    r4 = check_sa_key(sa_key_path)
    
    print("==================================================================")
    if r1 and r3:
        print(" ESTADO GENERAL: LISTO PARA CONFIGURAR CLIENTES EN ANTIGRAVITY")
    else:
        print(" ESTADO GENERAL: SE REQUIEREN ACCIONES DE CONFIGURACIÓN EN GCP")
    print("==================================================================")

if __name__ == "__main__":
    main()
