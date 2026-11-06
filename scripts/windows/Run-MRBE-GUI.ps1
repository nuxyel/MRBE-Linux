param(
    [string]$Distro = "Ubuntu",
    [string]$LinuxProject = "~/MRBE-Linux"
)
$ErrorActionPreference = "Stop"
$Command = "cd $LinuxProject && ./scripts/wsl/run-qemu-gui.sh"
wsl.exe -d $Distro -- bash -lc $Command
if ($LASTEXITCODE -ne 0) {
    throw "O QEMU gráfico não iniciou. Confira WSLg e execute primeiro o modo console."
}
