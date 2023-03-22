<?php
function chkLogin($uid){
    if($uid != '')return true;
    else return false;
}
function grave($str){
    if($str != '')return '`'.$str.'`';
    else return '';
}
function getImg($name,$tmp,$fileFolder,$page){
    if($page<>'') $page.="/";
	$fileName=date('YmdHis').'.jpg';

    if(is_dir($fileFolder.$page)){
        if(file_exists($fileFolder.$page.$fileName)){
            $fileName="2_".$fileName;
        }
    }else{
        mkdir($fileFolder.$page) ;
        if(file_exists($fileFolder.$page.$fileName)){
            $fileName="2_".$fileName;
        }
    }

    if(copy($tmp,$fileFolder.$page.$fileName))return $fileName;
	else return '';
}
?>
