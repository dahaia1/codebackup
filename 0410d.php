<?php
header("Content-type: text/html; charset=utf-8");
function &test(){
	static $b=0;
	$b=$b+1;
	echo $b."<br>";
	return $b;
}
$a=test();
$a=5;
$a=test();
$a=&test();
$a=5;
$a=test();
$unm=1234;
$math=&$num;
echo "\$math is:".$math."<br>";
unset($math);
echo "\$num is:".$num."<br>";
