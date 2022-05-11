<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.topnav {
  overflow: hidden;
  background-color: #333;
}

.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #4CAF50;
  color: white;
}
</style>
</head>
<div class="topnav">
  <a class="active" href="index.php">Home</a>
  <a href="list.php">Books</a>
</div>

<div style="padding-left:16px">
  <h2>List Books</h2>
    <p>Welcome to LSI IPB!! Silahkan pilih buku yang mau Anda baca
      <ul>
        <li><a href="list.php?page=book1.php">Kingsman: The Secret Service</a></li>
        <li><a href="list.php?page=book2.php">Enola Holmes</a></li>
        <li><a href="list.php?page=book3.php">Secret File</a></li>
      </ul>
    
    <?php 
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);
    if (isset($_GET['page'])) 
    {   
        include $_GET['page']; 
    } 
    else 
    {
    }
    
    ?>
    
  </body>
</html>


