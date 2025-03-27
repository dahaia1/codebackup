<?php
header("Content-Type:text/html;charset=utf-8");
$t=1;
$i=1;
while ($i<=10){
	$t=$t*$i;
	$i=$i+1;
}
echo "10!=".$t."<br>";
$t=1;
$i=1;
do{
	$t=$t*$i;
	$i=$i+1;
}while($i<=10);
echo "10!=".$t."<br>";
for($i=1,$t=1;$i<=10;$i++){
	$t=$t*$i;
}
echo "10!=".$t."<br>";
$t=1;
$i=1;
for(;$i<=10;){
	$t=$t*$i;
	$i++;
}
echo "10!=".$t."<br>";
for($i=1,$t=1;;){
	if($i>10){
		break;
	}
	$t=$t*$i;
	$i++;
}
echo "10!=".$t."<br>";