param (
    # Sets a default arg of the current dir if none specified.
    [Parameter(Mandatory=$false)][string]$directory = $pwd
 )

# list of all files in the specified dir
$files = Get-ChildItem $directory -File -Filter log* 

$yearRe = [regex]"\d{4}"
$monthRe = [regex]"(?<=-)(\d{2})(?=-)"

for ($i=0; $i -lt $files.Count; $i++) {
    $year = $yearRe.Match($files[$i]) 

    New-Item -ItemType Directory -Force -Path (Join-Path $directory $year) | Out-Null

    $month = $monthRe.Match($files[$i])
    $monthDir = -join($directory,"\",$year,"\",$month)

    New-Item -ItemType Directory -Force -Path $monthDir | Out-Null

    Move-Item -Path $files[$i].FullName -Destination (Join-Path $monthDir $files[$i])
}

