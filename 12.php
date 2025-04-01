
<style>
td {
    border: solid 3px;
}
</style>
<?php
header('Content-Type: text/html; charset=utf-8');
echo "<table>";
for ($i = 1; $i <= 9; $i++) {
    echo "<tr>";
    for ($j = 1; $j <= $i; $j++) {  // 关键修改：列数随行号变化
        echo '<td>' . getCN($j) . getCN($i) . ($i*$j<10?'得':'') . getCN($i * $j) . '</td>';
    }
    echo "</tr>";
}
echo "</table>";
function getCN($num) {
    $cns = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九'];
    $units = ['', '十'];
    
    if ($num < 10) {
        return $cns[$num];
    } else if ($num <= 99) {
        $tens = intval($num / 10);
        $ones = $num % 10;
        $result = ($tens > 1 ? $cns[$tens] : '') . $units[1];
        $result .= $ones != 0 ? $cns[$ones] : '';
        return $result;
    }
    return strval($num); // 超过99的数值直接返回数字
}


?>