<?php
header("Content-type: text/html; charset=utf-8");
$var=344;
if(isset($var)){
	echo "变量已设置。"."<br>";
	echo $var."<br>";
}
$a="test";
$b="anotthertest";
var_dump(isset($a));
var_dump(isset($a,$b));
unset($a);
var_dump(isset($a));
var_dump(isset($a,$b));
$foo=NULL;
var_dump(isset($foo));
?>