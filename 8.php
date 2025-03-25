<?php
header("Content-Type:text/html;charset=utf-8");
date_default_timezone_set ("PRC");
//if...esleif...
$day = date("D");
if ($day == "Fri") {
echo "Have a nice weekend!"."<br>";
} elseif ($day == "Sun") {
	echo "Have a nice Sunday"."<br>";
} else {
	echo "Have a nice day! "."<br>";
}
//switch
switch ($day) {
case "Mon":
echo "今天是星期一";
break;
case"Tue":
echo "今天是星期二";
break;
case "Wed":
echo "今天是星期三";
break;
case"Thu":
echo "今天是星期四";break;
case "Fri":
echo "今天是星期五";break;
default:
echo "今天休息。";
}
?>