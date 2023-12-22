<?php
$myfile0= fopen("webdictionary.txt","a");
//$data= fread($myfile0,filesize("webdictionary.txt"));
//echo $data;

//fwrite($myfile0,"i learned the file handling write mode\n");
//fwrite($myfile0,"now time  to revise append functin\n");
//fclose ($myfile0);

fwrite($myfile0,"here we stsrt to append.\n");
fwrite($myfile0,"wait append can be done with fwrite\n");
fclose ($myfile0);

?>