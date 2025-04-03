<html>
<body>
 <form action="" method="get">
	 请输入姓名：<input type="text" name="username"/>
 </form>
 <?php
 header("Content-type: text/html; charset=utf-8");
error_reporting(0);
 $user=$_GET['username'];
 echo "学生姓名：".$user."<br>";?>
 <from method="get">
 请输入商品原价: <input type="text" name="a" value=500>
 <select name="discount">
	<option>九折</option>
	<option>八折</option>
	<option>七折</option>
	<option>六折</option>
	<option>五折</option>
</select>
<input type="submit" value="计算"/>
</form>
<?php
error_reporting(0);
header("Content-type: text/html; charset=utf-8");
$a=$_GET['a'];
$discount=$_GET['discount'];
switch ($a){
	case "九折":
		$discount=0.9;
		break;
	case "八折":
		$discount=0.8;
		break;
	case "七折":
		$discount=0.7;
		break;
	case "六折":
		$discount=0.6;
		break;
	case "五折":
		$discount=0.5;
		break;
	default:
		$discount=1.0;
		break;
}
$b=$a*$discount;
echo "商品促销后价格是:".$a.'元';?>
</body>
</html>
