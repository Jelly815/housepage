<?php
	$a=(isset($_GET['a'])&&$_GET['a']<>'')?addslashes($_GET['a']):'';
	$id=(isset($_GET['id'])&&$_GET['id']<>'')?intval($_GET['id']):'';

	switch($a){
		case 'del':
			delPic($id);
			break;
		default:
			$tpl=new TemplatePower(_TSHOWPIC);
			$tpl->prepare();
			$tpl -> assignGlobal('UPLOADPICPATH',UPLOADPICPATH);
			
			$showPic=showPic();
			if(!$showPic){
					//echo ALERTXT06;exit;
				header('location:'.INDEXPATH);
			}else{
				$count=count($showPic);
				for($i=0;$i<$count;$i++){
					$tpl->newBlock('pic_row');
					$tpl -> assign(array('EDIT'=>EDIT,'EDITPICTOPATH'=>EDITPICTOPATH,'DEL'=>DEL,'LOGINTOPATH'=>LOGINTOPATH,'para'=>'&a=del&id=','DELALERT'=>DELALERT));
					$tpl->assign(array('id'=>htmlspecialchars($showPic[$i]['ex_id']),'uname'=>htmlspecialchars($showPic[$i]['ex_name']),'department'=>htmlspecialchars($showPic[$i]['depatm']),
					'title'=>htmlspecialchars($showPic[$i]['ex_title']),'pic'=>htmlspecialchars($showPic[$i]['ex_pic']),'txt'=>htmlspecialchars($showPic[$i]['ex_txt'])));
				}
				$tpl->printToScreen();
			}
	}
?>
