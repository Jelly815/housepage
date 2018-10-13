<?php
	$a=(isset($_GET['a'])&&$_GET['a']<>'')?addslashes($_GET['a']):'';

	switch($a){
		case 'add':
			addPic();
		break;
		default:
			$tpl=new TemplatePower(_TADDPIC);
			$tpl->prepare();
			$tpl->assign(array('PICTITLE'=>PICTITLE,'PICTITLEDSCPT'=>PICTITLEDSCPT,'PIC'=>PIC,'PICDSCRIPT'=>PICDSCRIPT,'PICDSCRIPT2'=>PICDSCRIPT2,'PICDSCRIPT3'=>PICDSCRIPT3,'ALERTXT08'=>ALERTXT08,'TITLEADDPIC'=>TITLEADDPIC));
			$tpl->assign(array('FILESIZE'=>FILESIZE,'PICAPTION'=>PICAPTION,'PICAPDSCPT'=>PICAPDSCPT,'SUBMIT'=>SUBMIT,'RETURNBTN'=>RETURNBTN,'LOGINTOPATH'=>LOGINTOPATH));
			$tpl->assign('error',$error);
			$tpl->printToScreen();
	}
?>
