<?php
header("Content-type: text/html; charset=utf-8");
function my_fun($a=1){
	echo $a."<br>";
	return;
	$a++;
	echo $a."<br>";
}
my_fun();
function squre($num){
	return $num*$num."<br>";
}
echo squre(4);