<?php
$sign_txt 	= array(
	'INPUTNAME' => INPUTNAME,
	'PWD'		=> PWD,
	'EMAIL'		=> EMAIL,
	'ALERTXT02'	=> ALERTXT02,
	'ALERTXT03' => ALERTXT03,
	'ALERTXT09'	=> ALERTXT09
);
$text 		= array_replace_recursive($text,$sign_txt);
/*
	switch($a){
		 case 'add':
			$dataArr=addUser();
			break;
		 default:

	}
	$tpl=new TemplatePower(_TSIGN);
	$tpl->prepare();
	$tpl->assign($dataArr);
	$tpl->assign(array('TITLESIGN'=>TITLESIGN,'INPUTNAME'=>INPUTNAME,'PWD'=>PWD,'INPUTPHONE'=>INPUTPHONE,'EMAIL'=>EMAIL,'IMPUTPRTM'=>IMPUTPRTM,'SUBMIT'=>SUBMIT,'RETURNBTN'=>RETURNBTN,'LOGIN'=>LOGIN,'LOGINPATH'=>LOGINPATH,'TITLESIGN'=>TITLESIGN,'SIGNPATH'=>SIGNPATH,'HEADERTITLE'=>HEADERTITLE,'INDEXPATH'=>INDEXPATH));
	$tpl->assign(array('CSSPATH'=>CSSPATH,'ALERTXT01'=>ALERTXT01,'ALERTXT02'=>ALERTXT02,'ALERTXT03'=>ALERTXT03,'error'=>$error));

	$getDepatm=getDepatm();
	$count=count($getDepatm);
	for($i=0;$i<$count;$i++){
		$tpl->newBlock('pic_row');
		$tpl->assign(array('id'=>$getDepatm[$i]['ex_id'],'title'=>$getDepatm[$i]['ex_title']));
	}

	$tpl->printToScreen();
*/
?>
