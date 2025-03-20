<?php
header("Content-Type:text/html;charset=utf-8");
$x=5;
$y="5";
var_dump($x == $y);
var_dump($x === $y);
var_dump($x != $y);
var_dump($x !== $y);
$a=5;
$b=8;
var_dump($a >= $b);
var_dump($a < $b);
if ($x === $y){
	echo "它们完全相同";
} else {
	echo "它们不完全相同";
}
$c=84;
$r=$c >= 60 ? "及格" : "不及格";
echo "<br>";
echo $r;
?>