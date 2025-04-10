<?php
header("Content-type: text/html; charset=utf-8");
function come(){
	echo "我来了<br>";
}
function go($name="Jack"){
	echo $name."走了<br>";
}
function back($string){
	echo $string."又回来了<br>";
}
$fanc='come';
$fanc();
$fanc='go';
$fanc('TOM');
$fanc='back';
$fanc('Lily');