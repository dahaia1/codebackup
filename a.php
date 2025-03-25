<?php
header("Content-Type:text/html;charset=utf-8");
$a=3*8%5;
var_dump($a);
echo $a."<br>";
$b=true?0:true?1:2;
var_dump($b);
echo $b."<br>";
$x=1;
$y=2;
$x=$y+=3;
var_dump($x);
echo $x."<br>";
$a1=true or true and false;
var_dump($a1);
echo $a1."<br>";