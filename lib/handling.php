<?php
header("Content-type:text/html;charset=utf-8");
include_once('./include/adodb/adodb.inc.php');
include_once('./include/TemplatePower/class.TemplatePower.inc.php');
include_once('./lib/main.php');
include_once('./lib/function.php');

class db_function extends db_connect{
	public function __construct()
    {
        parent::__construct();
    }

    // 登入
	function login($email,$pwd){
		$result = $re_array = array();
		$pwd 	= md5($pwd);

		$sql 	=  "SELECT 	`ex_name`,`ex_mail`
					FROM 	`ex_user`
					WHERE 	ex_mail = ? AND
							ex_pwd 	= ? ";

		$vals 	= array($email,$pwd);
		$sql 	= $this->db->prepare($sql);

		$result = $this->db->execute($sql,$vals);

		if($result && $result->RecordCount() > 0){
			$re_array 	= $result->getArray();
		}
		return $re_array;
	}

	// 註冊
	function add_user($data){
		$result = $re_array = array();

		$sql 	=  "INSERT INTO `ex_user`
						(ex_name,ex_pwd,ex_mail)
					VALUES
						(?,?,?)";

		$val 	= array($data[0],$data[1],$data[2]);
		$sql 	= $this->db->prepare($sql);
		$result = $this->db->execute($sql,$val);
		$user_id 		= $this->db->Insert_ID();

		if($user_id != ''){
			$re_array 	= array(
				'user_name' => $data[0],
				'user_mail' => $data[2]
			);
		}

		return $re_array;
	}
	// 檢查mail
	function chk_mail($email){
		$result = array();
		$re_chk = true;
		$sql 	=  "SELECT 	`ex_mail`
					FROM 	`ex_user`
					WHERE 	ex_mail = ? ";

		$vals 	= array($email);
		$sql 	= $this->db->prepare($sql);

		$result = $this->db->execute($sql,$vals);

		if($result && $result->RecordCount() > 0){
			$re_chk = false;
		}
		return $re_chk;
	}

	//新增作品
	function addPic(){
		global $uid;
		$userId=$this->db->qstr($uid);
		$title = (isset($_POST['title'])&&$_POST['title']<>'')?$this->db->qstr($_POST['title']):$this->db->qstr('');
		$caption = (isset($_POST['caption'])&&$_POST['caption']<>'')?$this->db->qstr($_POST['caption']):$this->db->qstr('');

		$sqlUser = sprintf("select ex_uid from `ex_pic` where ex_uid=%s",$uid);
		$arrayUser = $this->db->getAll($sqlUser);
		$countUser=count($arrayUser);

		if($countUser<3){
			$sql = sprintf("insert into `ex_data` (ex_user_id,ex_title,ex_txt,ex_date) values (%s,%s,%s,'%s')",$userId,$title,$caption,date("Y-m-d H:i:s"));

			if ($this->db->Execute($sql) === false) {
				echo ALERTXT06;exit;
			}else{
				$picId=$this->db->Insert_ID();	//取得作品序號
				$fileFolder='../';
				$folder=PICFOLDER;
				$name=mb_convert_encoding($_FILES["picFile1"]["name"],"big5","utf8");
				$tmp=$_FILES["picFile1"]["tmp_name"];
				if(!empty($name)){ 			//上傳檔案
					$fileName=getImg($name,$tmp,$fileFolder,$folder);

					if($fileName<>''){
						$sql = "insert into `ex_pic` (ex_uid,ex_did,ex_pic) ";
						$sql .= " values ($userId,$picId,'$fileName')";

						if ($this->db->Execute($sql) === false) {
							if(is_file(UPLOADPICPATH.$fileName)) unlink(UPLOADPICPATH.$fileName);
							$delSql=sprintf("delete from `ex_data` where ex_id=%s",$picId);
							if ($this->db->Execute($delSql) === false) {
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
		global $uid;
		$userId=$db->qstr($uid);
		$title = (isset($_POST['title'])&&$_POST['title']<>'')?$this->db->qstr($_POST['title']):$this->db->qstr('');
		$caption = (isset($_POST['caption'])&&$_POST['caption']<>'')?$this->db->qstr($_POST['caption']):$this->db->qstr('');

		$sql = sprintf("update `ex_data` set ex_title=%s,ex_txt=%s,ex_date='%s' where ex_user_id=%s and ex_id=%s",$title,$caption,date("Y-m-d H:i:s"),$userId,$id);

		if ($this->db->Execute($sql) === false) {
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
					if(is_file(UPLOADPICPATH.$this->db->getOne($sqlPic))) unlink(UPLOADPICPATH.$this->db->getOne($sqlPic));
					$sql = sprintf("update `ex_pic` set ex_pic='%s' where ex_uid=%s and ex_did=%s",$fileName,$userId,$id);

					if ($this->db->Execute($sql) === false) {
						echo ALERTXT06;exit;
					}
				}
			}
			echo "<script charset='UTF-8'>alert('".EDITSUCC."');location.href = '".LOGINTOPATH."';</script>";
		}
	}
	//刪除作品
	function delPic($id){
		global $uid;
		$sql = sprintf("select ex_id from `ex_data` where ex_user_id=%s and ex_id=%s",$uid,$id);

		if($this->db->getOne($sql)>0){
			$delSql=sprintf("delete from ex_data where  ex_user_id=%s and ex_id=%s",$uid,$id);
			if ($this->db->Execute($delSql) === false) {
				echo ALERTXT06;exit;
			}else{
				$sqlPic = sprintf("select ex_pic from `ex_pic` where ex_uid=%s and ex_did=%s",$uid,$id);
				if(is_file(UPLOADPICPATH.$this->db->getOne($sqlPic))) unlink(UPLOADPICPATH.$this->db->getOne($sqlPic));
				$delSql2=sprintf("delete from ex_pic where ex_uid=%s and ex_did=%s",$uid,$id);
				if ($this->db->Execute($delSql2) === false) {
					echo ALERTXT06;exit;
				}else header("location: ".LOGINTOPATH);
			}
		}else header("location: ".LOGINTOPATH);
	}
	//部門
	function getDepatm(){
		$sql = "select * from `ex_department` order by ex_sort";
	    $array = $this->db->getAll($sql);
		return $array;
	}
}
?>
