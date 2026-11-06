param(
    [string]$Distro = "Ubuntu",
    [string]$LinuxProject = "~/MRBE-Linux",
    [int]$Jobs = 4
)
$ErrorActionPreference = "Stop"
$Command = "cd $LinuxProject && JOBS=$Jobs ./scripts/wsl/build.sh"
wsl.exe -d $Distro -- bash -lc $Command
if ($LASTEXITCODE -ne 0) {
    throw "A compilação do MRBE Linux falhou. Copie a mensagem completa do Ubuntu."
}
