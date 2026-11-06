# Execute em PowerShell como Administrador.
$ErrorActionPreference = "Stop"

Write-Host "`n=== MRBE Linux: WSL 2 + Ubuntu 24.04 ===" -ForegroundColor Cyan

try {
    wsl.exe --status
} catch {
    Write-Host "WSL ainda não está disponível. Iniciando instalação..." -ForegroundColor Yellow
}

wsl.exe --set-default-version 2
wsl.exe --install -d Ubuntu

Write-Host "`nSe o Windows solicitar, reinicie o computador." -ForegroundColor Green
Write-Host "Depois abra Ubuntu 24.04 pelo menu Iniciar e crie seu usuário Linux."
