param($path)
$x = New-Object -ComObject Excel.Application
$x.DisplayAlerts = $false; $x.Visible = $false
$wb = $x.Workbooks.Open($path)
$x.CalculateFull()
$errs = 0; $n = 0
foreach ($ws in $wb.Worksheets) {
  $ur = $ws.UsedRange
  foreach ($c in $ur.Cells) {
    if ($c.HasFormula) { $n++; $t = [string]$c.Text; if ($t -match '^#') { $errs++; Write-Output ("ERR " + $ws.Name + "!" + $c.Address(0,0) + " " + $t + " " + $c.Formula) } }
  }
}
Write-Output "formulas=$n errors=$errs"
$s = $wb.Worksheets.Item("INÍCIO")
foreach ($r in 5..17) { Write-Output ("INICIO " + $r + ": " + $s.Cells.Item($r,1).Text + " | " + $s.Cells.Item($r,2).Text) }
$p = $wb.Worksheets.Item("Spirit Planner")
foreach ($r in 11..32) { Write-Output ("SP " + $r + ": " + $p.Cells.Item($r,1).Text + " | " + $p.Cells.Item($r,2).Text + " | " + $p.Cells.Item($r,6).Text) }
$wb.Save(); $wb.Close(); $x.Quit()
