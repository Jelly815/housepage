<?php
	$a=(isset($_GET['a'])&&$_GET['a']<>'')?addslashes($_GET['a']):'';
	$id=(isset($_GET['id'])&&$_GET['id']<>'')?intval($_GET['id']):'';
	
	switch($a){
		case 'edit':
			editPic($id);
		break;
		default:
	}
	
	$showPic=showPic($id);
	if(!$showPic){
			echo ALERTXT06;exit;
	}else{
		$name=htmlspecialchars($showPic[0]['ex_title']);
		$pic=htmlspecialchars($showPic[0]['ex_pic']);
		$caption=htmlspecialchars($showPic[0]['ex_txt']);
		
		$tpl=new TemplatePower(_TEDITPIC);
		$tpl->prepare();
		
		$tpl->assign(array('UPLOADPICPATH'=>UPLOADPICPATH,'EDITPICTOPATH'=>EDITPICTOPATH,'para'=>"&a=edit&id=$id",'title'=>$name,'pic'=>$pic,'caption'=>$caption));
		$tpl->assign(array('PICTITLE'=>PICTITLE,'PICTITLEDSCPT'=>PICTITLEDSCPT,'PIC'=>PIC,'PICDSCRIPT'=>PICDSCRIPT,'PICDSCRIPT2'=>PICDSCRIPT2,'PICDSCRIPT3'=>PICDSCRIPT3,'ALERTXT08'=>ALERTXT08,'TITLEEDITPIC'=>TITLEEDITPIC));
		$tpl->assign(array('FILESIZE'=>FILESIZE,'PICAPTION'=>PICAPTION,'PICAPDSCPT'=>PICAPDSCPT,'SUBMIT'=>SUBMIT,'RETURNBTN'=>RETURNBTN,'LOGINTOPATH'=>LOGINTOPATH));
		$tpl->assign('error',$error);
		$tpl->printToScreen();
	}
?>
