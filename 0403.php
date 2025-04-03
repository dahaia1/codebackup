<?php
header("Content-type: text/html; charset=utf-8");
$i=1;
$sum=0;
do{
	$sum+=$i;
	$i++;
}while($i<=100);
echo "1-100的和为：".$sum;
echo "<br>";
echo "<br>";
$n=5;
for($i=1;$i<=$n;$i++){
	for($j=1;$j<=$n-$i;$j++){
		echo '&nbsp;';
	}
	for($k=1;$k<=(2*$i)-1;$k++){
		echo "*";
	}
	echo "<br>";
}