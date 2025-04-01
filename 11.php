<style>
td {
    border: solid 3px;
}
</style>
<?php
header("content-type: text/html; charset=utf-8");
echo "<table>";
for ($i = 1; $i <= 9; $i++) {
    echo "<tr>";
    for ($j = $i; $j <= 9; $j++) {  // 关键的下三角逻辑
        echo "<td>" 
             . $i . "×" . $j . "=" 
             . ($i * $j) 
             . "</td>";
    }
    echo "</tr>";
}
echo "</table>";
?>