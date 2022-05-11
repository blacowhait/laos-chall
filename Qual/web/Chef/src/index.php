<?php
error_reporting(0);
session_start();
$cookie_name = "user";
$cookie_value = "juna";
setcookie($cookie_name, $cookie_value);

if(!isset($_COOKIE[$cookie_name])) {
} else {
  echo "<h1>Hello Chef " . $cookie_value . "!</h1>";
}


if($_COOKIE['user']=='admin')
{
	echo "Hello Chef '" . $cookie_value . "'!<br>";
	echo "LA2022{chef_cookie_cook_xdxdxd_LINZ_IS_HERE}<br>";
}
else{
	echo "<h1> Ur not chef admin! </h1>";
}

?>