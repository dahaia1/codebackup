<?php
header("Content-Type:text/html;charset=utf-8");
$a=6;
$b=3;
$c=($a<10 && $b>1);
var_dump($c);
$c=($a==$b || $b==1);
var_dump($c);
$c=($a>10 xor $b<1);
var_dump($c);
$c=!($a == $b);
var_dump($c);
$a= true;
$b= false;
if ($a || $b){
	echo "条件为真";
} else {
	echo "条件为假";
}
?>