<?php
header("Content-Type:text/html;charset=utf-8");
$a=9;
$b=12;
echo $a&$b;
echo "<br>";
echo $a | $b;
echo "<br>";
echo $a ^ $b;
echo "<br>";
echo -$a;
echo "<br>";
echo ~$a;
echo "<br>";
echo $a << 2;
echo "<br>";
echo $b >> 2;
?>
