<?php
session_start();
if(isset($_SESSION['name'])){
    $text = $_POST['text'];
    $name = $_POST['name'];
    $fp = fopen("log.html", 'a');
    $classname='CDKuser';
    if ($name=='Alpha'){
        $classname='msglnuser';}
        
    fwrite($fp, "<div style='width:100%'><div class=$classname> <b>".$name."</b>: ".stripslashes(htmlspecialchars($text))."</div></div><br> 
<style>
.msglnuser{  color: black;
    background-color: #A5D175;
     margin-right: 100px;
    margin-top: 10px;
    margin-left: 15px;
   
display:block;
padding-top: 10px;
    padding-right: 10px;
    padding-bottom: 10px;
    padding-left: 10px;
    border-radius: 15px;
    font-style: italic;
word-wrap: break-word;} 
.CDKuser{background-color: #efefef;
 margin-top: 10px;
    margin-right: 15px;
    margin-left: 100px;
   
   
display:block;
padding-top: 10px;
    padding-right: 10px;
    padding-bottom: 10px;
    padding-left: 10px;
    border-radius: 15px;
word-wrap: break-word;}
   
</style>");
    fclose($fp);
}
?>