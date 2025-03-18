<?php
header("Content-Type:text/html;charset=utf-8");
$a=10;
echo -$a . "<br>";
$b1=10;
$b2=20;
$b=$b1+$b2;
echo $b . "<br>";
$c1=10;
$c2=20;
echo $c=$c1*$c2 . "<br>";
$d1=123;
$d2=20;
$d3=4;
$d4="2.05aabb";
echo var_dump($d1/$d2);
echo var_dump($d2/$d3);
echo var_dump($d2/$d4);
echo 12.3%5.2;
echo 12%5;
echo -12%5;
echo 12%-5;
?>