<?php
header("Content-type:text/html;charset=utf-8");
include_once('./include/adodb/adodb.inc.php');
include_once('./include/TemplatePower/class.TemplatePower.inc.php');
include_once('./lib/main.php');
include_once('./lib/function.php');

$db = ADONewConnection(DATATYPE);
$db->Connect(SERVERNAME,USERNAME,USERPWD,DATANAME);
$db->Execute("SET NAMES 'utf8'");

$name=$phone=$email=$prtm=$error='';
$dataArr=array();
$errorNum=0;
$op=(isset($_GET['op'])&&$_GET['op']<>'')?addslashes($_GET['op']):'';
$uid=(isset($_SESSION['uid'])&&!empty($_SESSION['uid']))?$_SESSION['uid']:'';
$a=(isset($_GET['a'])&&$_GET['a']<>'')?addslashes($_GET['a']):'';

if($db->isConnected()){
	//登入
	if(isset($_POST['loginHid'])&&$_POST['loginHid']=='loginFrom'){
        $email = (isset($_POST['mail'])&&$_POST['mail']<>'')?$db->qstr($_POST['mail']):$db->qstr('');
        $pwd = (isset($_POST['pwd'])&&$_POST['pwd']<>'')?$db->qstr($_POST['pwd']):$db->qstr('');
        $pwd=md5(trim($pwd,"'"));
        
        $sql = sprintf("select * from `ex_user` where ex_mail=%s and ex_pwd='%s'",$email,$pwd);
        $array = $db->getRow($sql);

        if(!empty($array)){
           $_SESSION['uid']=$array['ex_id'];
           $_SESSION['uname']=$array['ex_name'];
           $_SESSION['umail']=$array['ex_mail'];
           $_SESSION['uphone']=$array['ex_phone'];
           $_SESSION['udepartment'] =$array['ex_department'];
           header("location: ".LOGINTOPATH);
        }else{
           $error=ALERTXT05;
        }
    }
}else{
      echo ALERTXT06;exit;
}
//首頁顯示
function indexShow($start,$end){
	global $db;
	$start=intval($start);
	$end=intval($end);
	$sql = sprintf("select a.ex_title,a.ex_txt,b.ex_pic,c.ex_name,(select ex_title from `ex_department` where ex_id=c.ex_department) AS 'depatm' from `ex_data` a,`ex_pic` b,`ex_user` c where a.ex_id=b.ex_did and c.ex_id=b.ex_uid order by a.ex_date desc limit %s,%s",$start,$end);
	$result = $db->execute($sql);
	
	return $result;
}
//作品瀏覽
function showPic($id=''){
	global $db,$uid;
	$sql = sprintf("select a.ex_id,a.ex_title,a.ex_txt,b.ex_pic,c.ex_name,(select ex_title from `ex_department` where ex_id=c.ex_department) AS 'depatm' from `ex_data` a,`ex_pic` b,`ex_user` c where a.ex_id=b.ex_did and c.ex_id=b.ex_uid and c.ex_id=%s",$uid);
	if($id<>'')$sql .= sprintf(" and a.ex_id=%s",$id); 
	$sql .= ' order by a.ex_date desc';
	
    $array = $db->getAll($sql);
	return $array;
}
//註冊
function addUser(){
	global $db,$name,$phone,$email,$prtm,$error;
    $name = (isset($_POST['name'])&&$_POST['name']<>'')?$db->qstr($_POST['name']):$db->qstr('');
    $pwd = (isset($_POST['pwd'])&&$_POST['pwd']<>'')?$db->qstr($_POST['pwd']):$db->qstr('');
    $phone = (isset($_POST['phone'])&&$_POST['phone']<>'')?$db->qstr($_POST['phone']):$db->qstr('');
    $email = (isset($_POST['mail'])&&$_POST['mail']<>'')?$db->qstr($_POST['mail']):$db->qstr('');
    $prtm = (isset($_POST['departmant'])&&$_POST['departmant']<>'')?intval($_POST['departmant']):$db->qstr('');

    $sql = sprintf("select * from `ex_user` where ex_mail=%s",$email);
    $array = $db->getRow($sql);
    if(empty($array)){
            $pwd=md5(trim($pwd,"'"));
            
            $sql = sprintf("insert into `ex_user` (ex_name,ex_mail,ex_pwd,ex_phone,ex_department,ex_date) values (%s,%s,'%s',%s,%s,'%s')",$name,$email,$pwd,$phone,$prtm,date("Y-m-d H:i:s"));

            if ($db->Execute($sql) === false) {
                echo ALERTXT06;exit;
            }else{
				echo "<script charset='UTF-8'>alert('".INSERTUSERSUCC."');location.href = '".INDEXPATH."';</script>";
            }
    }else{
              $name=trim($name,"'");
              $phone=trim($phone,"'");
              $email=trim($email,"'");
              $prtm=trim($prtm,"'");
              $dataArr=array('name'=>$name,'phone'=>$phone,'mail'=>$email,'prtm'=>$prtm);
              $error=ALERTXT04;
			  return $dataArr;
    }
}
//新增作品
function addPic(){
	global $db,$uid;
	$userId=$db->qstr($uid);
	$title = (isset($_POST['title'])&&$_POST['title']<>'')?$db->qstr($_POST['title']):$db->qstr('');
	$caption = (isset($_POST['caption'])&&$_POST['caption']<>'')?$db->qstr($_POST['caption']):$db->qstr('');
	
	$sqlUser = sprintf("select ex_uid from `ex_pic` where ex_uid=%s",$uid);
	$arrayUser = $db->getAll($sqlUser);
	$countUser=count($arrayUser);
	
	if($countUser<3){
		$sql = sprintf("insert into `ex_data` (ex_user_id,ex_title,ex_txt,ex_date) values (%s,%s,%s,'%s')",$userId,$title,$caption,date("Y-m-d H:i:s"));
	
		if ($db->Execute($sql) === false) {
			echo ALERTXT06;exit;
		}else{
			$picId=$db->Insert_ID();	//取得作品序號
			$fileFolder='../';
			$folder=PICFOLDER;
			$name=mb_convert_encoding($_FILES["picFile1"]["name"],"big5","utf8");
			$tmp=$_FILES["picFile1"]["tmp_name"];
			if(!empty($name)){ 			//上傳檔案
				$fileName=getImg($name,$tmp,$fileFolder,$folder);
				
				if($fileName<>''){
					$sql = "insert into `ex_pic` (ex_uid,ex_did,ex_pic) ";
					$sql .= " values ($userId,$picId,'$fileName')";
					
					if ($db->Execute($sql) === false) {
						if(is_file(UPLOADPICPATH.$fileName)) unlink(UPLOADPICPATH.$fileName);
						$delSql=sprintf("delete from `ex_data` where ex_id=%s",$picId);
						if ($db->Execute($delSql) === false) {
							echo ALERTXT06;exit;
						}
						echo ALERTXT06;exit;
					}else{
						echo "<script charset='UTF-8'>alert('".INSERTSUCC."');location.href = '".LOGINTOPATH."';</script>";
					}
				}
			}	
		}
	}else echo "<script charset='UTF-8'>alert('".ALERTXT07."');location.href = '".LOGINTOPATH."';</script>";
}
//編輯
function editPic($id){
	global $db,$uid;
	$userId=$db->qstr($uid);
	$title = (isset($_POST['title'])&&$_POST['title']<>'')?$db->qstr($_POST['title']):$db->qstr('');
	$caption = (isset($_POST['caption'])&&$_POST['caption']<>'')?$db->qstr($_POST['caption']):$db->qstr('');
	
	$sql = sprintf("update `ex_data` set ex_title=%s,ex_txt=%s,ex_date='%s' where ex_user_id=%s and ex_id=%s",$title,$caption,date("Y-m-d H:i:s"),$userId,$id);
	
	if ($db->Execute($sql) === false) {
		echo ALERTXT06;exit;
	}else{
		$fileFolder='../';
		$folder=PICFOLDER;
		$name=mb_convert_encoding($_FILES["picFile1"]["name"],"big5","utf8");
		$tmp=$_FILES["picFile1"]["tmp_name"];
		
		$sqlPic = sprintf("select ex_pic from `ex_pic` where ex_uid=%s and ex_did=%s",$uid,$id);
		
		if(!empty($name)){ 				//上傳檔案
			$fileName=getImg($name,$tmp,$fileFolder,$folder);
			
			if($fileName<>''){
				if(is_file(UPLOADPICPATH.$db->getOne($sqlPic))) unlink(UPLOADPICPATH.$db->getOne($sqlPic));
				$sql = sprintf("update `ex_pic` set ex_pic='%s' where ex_uid=%s and ex_did=%s",$fileName,$userId,$id);
				
				if ($db->Execute($sql) === false) {
					echo ALERTXT06;exit;
				}
			}
		}
		echo "<script charset='UTF-8'>alert('".EDITSUCC."');location.href = '".LOGINTOPATH."';</script>";
	}
}
//刪除作品
function delPic($id){
	global $db,$uid;
	$sql = sprintf("select ex_id from `ex_data` where ex_user_id=%s and ex_id=%s",$uid,$id);
    
	if($db->getOne($sql)>0){
		$delSql=sprintf("delete from ex_data where  ex_user_id=%s and ex_id=%s",$uid,$id);
		if ($db->Execute($delSql) === false) {
			echo ALERTXT06;exit;
		}else{
			$sqlPic = sprintf("select ex_pic from `ex_pic` where ex_uid=%s and ex_did=%s",$uid,$id);
			if(is_file(UPLOADPICPATH.$db->getOne($sqlPic))) unlink(UPLOADPICPATH.$db->getOne($sqlPic));
			$delSql2=sprintf("delete from ex_pic where ex_uid=%s and ex_did=%s",$uid,$id);
			if ($db->Execute($delSql2) === false) {
				echo ALERTXT06;exit;
			}else header("location: ".LOGINTOPATH);
		}
	}else header("location: ".LOGINTOPATH);
}
//部門
function getDepatm(){
	global $db;
	$sql = "select * from `ex_department` order by ex_sort";
    $array = $db->getAll($sql);
	return $array;
}
?>
