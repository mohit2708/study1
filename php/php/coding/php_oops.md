### user.php
```php
<?php
mysql_connect("localhost","root","");
mysql_select_db("Webspread");
$sql2 = NULL;
if(isset($_POST['SubmitButton']))
{
	$source_path = $_FILES['fileToUpload']['tmp_name'];
	$name = $_FILES['fileToUpload']['name'];
	$pic = $_FILES['fileToUpload']['name'];
	  
	  $rand = time().'_';
	  $des_path ="image/$rand$name";
	 move_uploaded_file($source_path,$des_path);
	 
	$pic1 = ($_post['fileToUpload']);
	$img = $rand.$pic;
	
	$txtName = ($_POST['name']);
	$email = ($_POST['email']);
	$mob = ($_POST['mobile']);
	$city = ($_POST['city']);
	
	$sql = "INSERT INTO login (name,email,mobile,city,image) values('$txtName','$email','$mob','$city','$img')";
	mysql_query($sql);
	
		$location ='login-index.php';
		header("Location:$location");
		exit();
}
	
	if(isset($_POST['Updatebutton']))
	{
		
	$id = $_GET['id'];
	$name = $_POST['name'];
	$email =  $_POST['email'];
	$mobile = $_POST['mobile'];
	$city = $_POST['city'];
	
	
	 $query = mysql_query("update login set name='$name', email='$email', mobile='$mobile', city='$city' where id='$id'");
		
		$location ='login-index.php';
		header("Location:$location");
		exit();
	}
if(isset($_GET['id']))
	{	
$id = $_GET['id'];
$sql1 = mysql_query("select * from login where id='$id'");
$sql2 = mysql_fetch_array($sql1);
	}

?>
<html>
<head>
</head>
<script type="text/javascript" src="js/jquery.min.js"></script>
<script type="text/javascript" src="js/jquery-1.9.1.min.js"></script>
<body>
<form name="loginform" id="loginform" action="#" method="post" enctype="multipart/form-data" >
<table border="1">
<tr>
	<td>Name:</td>
	<td><input type="text" id="name" name="name" placeholder="Enter Name" value="<?php echo $sql2['name']; ?>"></td> </tr>
</tr>
<tr>
	<td>Email:</td>
	<td><input type="email" id="email" name="email" placeholder="Enter Email" value="<?php echo $sql2['email']; ?>"></td> 
</tr>
<tr>
	<td>Mobile No:</td>
	<td><input type="text" placeholder="Mobile Number" id="mobile" name="mobile" value="<?php echo $sql2['mobile']; ?>"></td> 
</tr>

<tr> 
	<td>City:</td>
	<td><input type="text" id="city" name="city" placeholder="Enter City" value="<?php echo $sql2['city']; ?>"></td> 
</tr>
<tr> <td>File Name:</td> <td><input type="file" name="fileToUpload" id="fileToUpload"></td> </tr>
<tr>
<?php if(isset($_GET['id'])){ ?>
	<td><input type="submit" name="Updatebutton" value="Update"></td>
<?php } else{?>
<td><input type="submit" name="SubmitButton" value="Submit"></td>	
<?php }	?>

</tr>

</table>	
</form>

<script src="js/common.js"></script>
</body>
</html>
```
### list.php
```php
<?php
mysql_connect("localhost", "root", "") ;
mysql_select_db("Webspread");

if(isset($_POST['delete']))
{
	$checkbox=$_POST['deletecheck'];
	foreach ($checkbox as $value)
	{
		$sql = mysql_query("delete from login Where id='$value'");
	}
}



$result = mysql_query("select * from login");
?>
<form action="#" method="post">
<table border='1'>
<tr><td>Id</td><td>Name</td><td>Email</td><td>Mobile</td><td>City</td><td>Photo</td><td>Action</td></tr>
<?php
while ($row = mysql_fetch_array($result, MYSQL_ASSOC)) 
{	?>
	<tr>
		<td><?php echo $row['id'];?></td>
		<td><?php echo $row['name'];?></td>
		<td><?php echo $row['email'];?></td>
		<td><?php echo $row['mobile'];?></td>
		<td><?php echo $row['city'];?></td>
		<td><img width="100" height="100" src="image/<?php echo $row['image'];?>"></td>
		<td><a href="login.php?id=<?php echo $row['id']; ?>&action=edit">edit</a>
		<input name="deletecheck[]" type="checkbox" id="checkbox" value="<?php echo $row['id'];?>"> </td>
	</tr>
	<?php 
}
mysql_free_result($result);
?>
<tr>
<td><input name="delete" type="submit" id="delete" value="Delete"></td>
</tr>
</table>
</form>
```
