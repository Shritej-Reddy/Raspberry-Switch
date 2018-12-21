<?php
	$status = $_GET['button'];
	file_put_contents("status.txt", $status);
	file_get_contents("status.txt");
?>

<!DOCTYPE html>
<html>
<head>
<style>
</style>
	<link rel='stylesheet' type='text/css' href = 'css/main.css'>
	<title>Button Test</title>
</head>

<body>
	<div>
		<br><br><br><br><br><br><br><br><br>
		<h2 style="text-align: center"> Raspberry Controller </h2>
		<form class = "button" action = "button.php" method = "GET">
			<input type = "hidden" class = "button" name = "button" value = "on">
			<input type = "submit" value = "ON">
		</form>
		<form action="button.php" method = "GET">
			<input type = "hidden" name ="button" value = "off">
			<input type = "submit" value = "OFF">
		</form>
	</div>
</body>
</html>