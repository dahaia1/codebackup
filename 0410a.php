<?php
header("Content-type: text/html; charset=utf-8");
function fun_sum1($a,$b)
{
	$a=$a+5;
	return $a+$b;
}

$x=10;
$y=20;
echo fun_sum1($x,$y)."<br>";
echo $x."<br>";
function fun_sum2(&$a,&$b){
	$a=$a+5;
	return $a+$b;
}
$x=10;
$y=20;
echo fun_sum2($x,$y)."<br>";
echo $x."<br>";
function fun_sum3($a,$b=20){
	$a=$a+5;
	return $a+$b;
}
$x=10;
echo fun_sum3($x,$y)."<br>";
echo $x."<br>";