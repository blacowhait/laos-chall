<?php 

include 'config.php';

$res = NULL;

if(isset($_POST['query'])){
	$query = $_POST['query'];
	$res = $conn->query('SELECT * FROM news WHERE id ='.$query.';');
}
?>

<html>
	<head>
		<title>BIGGEST Data Breaches History</title>
	</head>
	<body>
		<form method="POST" action="/">
			<input name="query" type="text" placeholder="(example : 1)">
			<button type="submit">Show News</button>
		</form>
		<?php 
			if($res !== NULL)
				foreach ($res as $row) {
					echo "<h1>".$row['title']."</h1>";
					echo "<p>".$row['content']."</p>";
				}
		?>
	</body>
</html>
