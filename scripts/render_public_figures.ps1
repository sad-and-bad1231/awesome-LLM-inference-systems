Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $PSScriptRoot
$figs = Join-Path $root 'figs'
$chromeCandidates = @(
    (Join-Path ${env:ProgramFiles} 'Google\Chrome\Application\chrome.exe'),
    (Join-Path ${env:ProgramFiles(x86)} 'Google\Chrome\Application\chrome.exe'),
    (Join-Path ${env:ProgramFiles(x86)} 'Microsoft\Edge\Application\msedge.exe'),
    (Join-Path ${env:ProgramFiles} 'Microsoft\Edge\Application\msedge.exe')
)
$chrome = $chromeCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $chrome) { throw 'Chrome or Edge is required to render SVG figures to PNG.' }

$assets = @(
    @{ Svg = 'ai-inference-systems-cover.svg'; Png = 'ai-inference-systems-cover.png'; Width = 1600; Height = 1080 },
    @{ Svg = 'ai-inference-system-map.svg'; Png = 'ai-inference-system-map.png'; Width = 1600; Height = 900 }
)

foreach ($asset in $assets) {
    $svg = Join-Path $figs $asset.Svg
    $png = Join-Path $figs $asset.Png
    if (-not (Test-Path $svg)) { throw "Missing SVG source: $svg" }
    $uri = 'file:///' + (($svg -replace '\\', '/') -replace ' ', '%20')
    $arguments = @('--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1', "--window-size=$($asset.Width),$($asset.Height)", "--screenshot=$png", '--virtual-time-budget=1000', $uri)
    $process = Start-Process -FilePath $chrome -ArgumentList $arguments -Wait -NoNewWindow -PassThru
    if ($process.ExitCode -ne 0 -or -not (Test-Path $png)) { throw "Failed to render $svg" }
    Write-Output "Rendered $($asset.Png) from $($asset.Svg)"
}
