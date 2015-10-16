<style>
table, th, td {
 border: 1px solid black;
 border-collapse: collapse;
}
</style>
<table>

<?php

foreach (glob("print/*.JPG") as $filename){
   $preview_name = substr($filename, 6, strlen($filename));
   echo "<form action='printing.cgi' method='post'>" . "<tr><th>" . "<img name='file' src='print/preview/$preview_name'/>" . "</th><th>" . "<input type='text' name='file' value='$filename' readonly>" . "</th><th>" . "<input type='number' name='number' value='1' min='1' max='99'>" . "</th><th>" . "<input type='submit' value='Adet Bas'>" . "</th></tr>" . "</form>";
}

?>
</table>
