# ==============================================================================
# Script de Automatización: Google Cloud & Google Workspace MCP Setup
# Ecosistema Antigravity 2.0 (Multi-Tenant B2B)
# ==============================================================================

param (
    [string]$ProjectId = "antigravity-workspace-control-plane",
    [string]$ServiceAccountName = "mcp-workspace-agent",
    [string]$KeyOutputPath = "$HOME\.config\gcloud\antigravity-sa-key.json"
)

Write-Host "==> [1/5] Configurando Proyecto GCP: $ProjectId..." -ForegroundColor Cyan
gcloud projects create $ProjectId --name="Antigravity Workspace Control Plane" --labels=environment=production,managed_by=antigravity 2>$null
gcloud config set project $ProjectId

Write-Host "==> [2/5] Habilitando APIs de Google Workspace y GCP IAM/STS..." -ForegroundColor Cyan
$apis = @(
    "gmail.googleapis.com",
    "drive.googleapis.com",
    "docs.googleapis.com",
    "sheets.googleapis.com",
    "slides.googleapis.com",
    "calendar-json.googleapis.com",
    "chat.googleapis.com",
    "people.googleapis.com",
    "admin.googleapis.com",
    "iam.googleapis.com",
    "sts.googleapis.com",
    "secretmanager.googleapis.com"
)

foreach ($api in $apis) {
    Write-Host "   -> Habilitando $api..." -ForegroundColor Yellow
    gcloud services enable $api
}

Write-Host "==> [3/5] Creando Service Account de Orquestación Agéntica..." -ForegroundColor Cyan
gcloud iam service-accounts create $ServiceAccountName `
    --description="Service Account para integracion agéntica MCP de Workspace con Antigravity" `
    --display-name="Antigravity Workspace Agent SA" 2>$null

$saEmail = "$ServiceAccountName@$ProjectId.iam.gserviceaccount.com"

Write-Host "==> [4/5] Generando Clave de Credencial JSON..." -ForegroundColor Cyan
$keyDir = Split-Path -Path $KeyOutputPath -Parent
if (-not (Test-Path -Path $keyDir)) {
    New-Item -ItemType Directory -Path $keyDir -Force | Out-Null
}
gcloud iam service-accounts keys create $KeyOutputPath --iam-account=$saEmail

Write-Host "==> [5/5] Obteniendo OAuth2 Client ID para Domain-Wide Delegation (DWD)..." -ForegroundColor Cyan
$clientId = gcloud iam service-accounts describe $saEmail --format="value(oauth2ClientId)"

Write-Host ""
Write-Host "==============================================================================" -ForegroundColor Green
Write-Host " CONFIGURACIÓN DE GOOGLE CLOUD COMPLETADA" -ForegroundColor Green
Write-Host "==============================================================================" -ForegroundColor Green
Write-Host "Service Account Email : $saEmail" -ForegroundColor White
Write-Host "Ruta de Clave JSON   : $KeyOutputPath" -ForegroundColor White
Write-Host "OAuth2 Client ID DWD  : $clientId" -ForegroundColor Yellow
Write-Host ""
Write-Host "PASO OBLIGATORIO PARA CLIENTES ENTERPRISE:" -ForegroundColor Red
Write-Host "Registrar el Client ID ($clientId) en admin.google.com de cada cliente empresarial." -ForegroundColor Red
Write-Host "==============================================================================" -ForegroundColor Green
