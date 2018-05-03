<?php
$base=$_REQUEST['image'];
//$aller=$_POST['allergies'];
$binary=base64_decode($base);
header('Content-Type: bitmap; charset=utf-8');
$file = fopen('uploaded_image.jpg', 'wb');
fwrite($file, $binary);
fclose($file);

//file_put_contents('uploaded_aller.txt', var_export(implode('|',$aller), true));

//header('Content-Type: bitmap; charset=utf-8');
//$file = fopen('uploaded_image.jpg', 'wb');
//fwrite($file, $binary);
//fclose($file);
//echo 'Image upload complete!!, Please check your php file directory……';
$finalresult = shell_exec("python nutrisafe.py");
echo $finalresult;
?>