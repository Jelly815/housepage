<?php
    $tpl=new TemplatePower(_TINDEX);
    $tpl->prepare();
	$tpl -> assignGlobal("UPLOADPICPATH",UPLOADPICPATH);
	$tpl->assign(array('FIRST'=>10,'LIMIT'=>10));

	$indexShow=indexShow(0,10);
	if(!$indexShow){
			echo ALERTXT06;exit;
	}else{
		while ($val = $indexShow->fetchRow()){
			$tpl->newBlock('index_row');
			
			$tpl->assign(array('uname'=>htmlspecialchars($val['ex_name']),'department'=>htmlspecialchars($val['depatm']),'title'=>htmlspecialchars($val['ex_title']),
			'pic'=>htmlspecialchars($val['ex_pic']),'txt'=>htmlspecialchars($val['ex_txt'])));
		}
	}
    $tpl->printToScreen();
?>
