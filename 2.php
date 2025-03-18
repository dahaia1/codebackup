<?php
header("Content-Type:text/html;charset=utf-8");
$r=10;
define("PI",3.1415);
$circle=2*PI*$r;
$area=PI*$r*$r;
echo "圆的半径：" . $r . "<br>圆的周长：" . $circle ."<br>圆的面积：" . $area ."<br>";
$output="圆的半径：" . $r ."<br>";
echo $output;
$output="圆的周长：" . $circle ."<br>";
echo $output;
$output="圆的面积：" . $area ."<br>";
echo $output;