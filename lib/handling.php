<?php
header("Content-type:text/html;charset=utf-8");
include_once(__DIR__.'/../include/adodb/adodb.inc.php');
include_once(__DIR__.'/../include/TemplatePower/class.TemplatePower.inc.php');
include_once(__DIR__.'/../lib/main.php');
include_once(__DIR__.'/../lib/function.php');

class db_function extends db_connect{
	public function __construct()
    {
        parent::__construct();
    }


	function insert_data($sql,$vals){
		$re_id 	= 0;
		$sql 	= $this->db->prepare($sql);

		$result = $this->db->execute($sql,$vals);

		if($result && $result->RecordCount() > 0){
			$re_id 	= $this->db->Insert_ID();
		}
		return $re_id;
	}

	function update_data($sql,$vals){
		$re_data 	= false;
		$sql 		= $this->db->prepare($sql);

		$result 	= $this->db->execute($sql,$vals);

		if($result && $result->RecordCount() > 0){
			$re_data= true;
		}
		return $re_data;
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
			$re_array 	= $this->db->Insert_ID();
		}
		return $re_array;
	}

	// 註冊
	function add_user($data){
		$result = $re_array = array();

		$sql 	=  "INSERT INTO `ex_user`
						(ex_name,ex_pwd,ex_mail,ex_age)
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


	// 取得table資料
	function get_table_value($table,$select_field='',$where_str='',$order_by=''){
        $rs     = array();
        if($select_field == ''){
        	$select_field 	= '*';
        }
        $sql 	= "SELECT $select_field FROM $table";

 		if($where_str != ''){
 			$sql 			.= " WHERE ".$where_str;
 		}
 		if($order_by != ''){
 			$sql 			.= " ORDER BY ".$order_by;
 		}
        if($rs 	= $this->db->getAll($sql)){
        	return  $rs;
        }else{
			return  array();
		}
	}

	/**
	 *	取得資料
	 *	@param select: 	is_array	=> array('field1','field2');
	 * 	                is_string 	=> 'field1,field2'
	 *	@param where : 	'type'：0:field;1:手key值;2:沒有值
	 *				array(
	 *					array(0,'field','=','value'),
	 *					array(1,'concat(field1,field2)','LIKE','%value%'),
	 *					array(2,'field','IN (1,2,3,4)',''),
	 *                  array(3,'string')
	 *				);
	 *	@param orderby:	array(
	 *					'field' => 'ASC'
	 *				);
	 *  @param type :   0:getArray();
	 *              1:SelectLimit();
	 *              2:getOne();
	 *  @return array
	*/
	function select_table_data($table,$select,$where = array(),$orderby = array(),
								$type = 0,$page_limit = 0,$page_num = 0)
	{
        $table 			= trim($table);
		$arr 			= $return_data 	= array();
		$chk    		= 'false';
		$select_str 	= $where_str 	= $orderby_str 	= '';
		$where_symbol 	= '=';

		if(!empty($select)){
			// SELECT
			if(is_array($select)){
				$data_count 			= count($select);
				$i = 1;
				foreach($select as $val){
					$field 				= $this->tableField($val);
					$select_str    	   .= ($data_count != $i)?"$field,":"$field";

					$i++;
				}
			}else{
				$select_str 			= $select;
			}

			$sql 		= "SELECT $select_str FROM $table ";

			// WHERE
			$where_count 				= count($where);
			$j = 1;
			if(!empty($where) && $where_count > 0){
				foreach($where as $key 	=> $val){
					$where_type 			= isset($val[0])?intval($val[0]):0;
					$where_field 			= isset($val[1])?$val[1]:'';
					if($where_type == 3){
						$where_symbol       = '';
					}else{
						$where_symbol 		= isset($val[2])?$val[2]:'';
						$where_val 			= isset($val[3])?$val[3]:'';
						if($where_type != 2){
							$arr[] 			= $where_val;
						}

						$where_field 		= ($where_type != 1)?$where_field:
												$this->mssql_real_escape_str($where_field);
					}
					if($where_count != $j){
						$where_str     .= ($where_type == 2 || $where_type == 3)?
											" $where_field $where_symbol AND ":
											" `$where_field` $where_symbol ? AND ";
					}else{
						$where_str     .= ($where_type == 2 || $where_type == 3)?
											" $where_field $where_symbol ":
											" `$where_field` $where_symbol ? ";
					}
					$j++;
				}
				$sql   .= " WHERE $where_str ";
			}

			// ORDER BY
			$orderby_count 				= count($orderby);
			$k = 1;
			if(!empty($orderby) && $orderby_count > 0){
				foreach($orderby as $key => $val){
					$orderby_field 		= $key;
					$orderby_order 		= !empty($val)?strtoupper($val):'ASC';
					$orderby_order  	= ($orderby_order == 'DESC')?$orderby_order:'ASC';
					$orderby_str       .= ($orderby_count != $k)?
											"{$orderby_field} {$orderby_order},":
											"{$orderby_field} {$orderby_order}";

					$k++;
				}
				$sql   .= " ORDER BY $orderby_str ";
			}
			$sql        = $this->db->Prepare($sql);

			if($type == 1){
				$rs     = $this->db->SelectLimit($sql,$page_limit,$page_num,$arr);
	            if(!empty($rs)){
	                $return_data  		= $rs->getArray();
	            }
	        }elseif($type == 2){

	            $return_data      		= $this->db->getOne($sql,$arr);

	        }else{
	        	$rs 	= $this->db->Execute($sql,$arr);

	            if($rs && $rs->RecordCount() > 0){
					$return_data 		= $rs->getAll();
				}
	        }
		}
		return $return_data;
    }

    /**
	 *	取得資料
	 *	@param select: 	is_array	=> array(
	 *			            'table1'    => array(field1,field2...),
	 *			            'table2'    => array(field1,field2...)
	 *			        );
	 * 	                is_string 	=> 'field1,field2'
	 *	@param where : 	0:field;1:手key值;2:沒有值
	 *				array(
	 *					array(0,'field','=','value','table'),
	 *					array(1,'concat(field1,field2)','LIKE','%value%'),
	 *					array(2,'field','IN (1,2,3,4)','','table'),
	 *                  array(3,'string')
	 *				);
	 *	@param orderby:
	 *				array(
	 *					array('table1','field','ASC'),
	 *					array('table2','field','DESC')
	 *				);
	 *  @param type :
	 *				0:getArray();
	 *              1:SelectLimit();
	 *              2:getOne();
	 *  @return array
	*/
	function select_table_data_join($table,$select,$where = array(),$orderby = array(),
								$type = 0,$page_limit = 0,$page_num = 0)
	{

		$arr 			= $return_data 	= array();
		$chk    		= 'false';
		$table_str 		= $select_str 	= $where_str 	= $orderby_str 	= '';
		$where_symbol 	= '=';

		if(!empty($select)){
			// TABLE
			if(is_array($table)){
				foreach ($table as $tb_key => $tb_val) {
					$table_str		   .= "[$tb_val] {$tb_val},";
				}
				$table_str 				= rtrim($table_str,',');
			}else{
				$table_str 				= $table;
			}

			// SELECT
			if(is_array($select)){
				foreach($select as $sel_key => $sel_val){
					foreach ($sel_val as $son_val) {
						$select_str    .= "{$sel_key}.".$this->tableField($son_val).',';
					}
				}
				$select_str 			= rtrim($select_str,',');
			}else{
				$select_str 			= $select;
			}

			$sql 		= "SELECT $select_str FROM $table_str ";

			// WHERE
			$where_count 				= count($where);
			$j = 1;
			if(!empty($where) && $where_count > 0){
				foreach($where as $key 	=> $val){
					$where_tb 			= '';
					$where_type 		= isset($val[0])?intval($val[0]):0;
					$where_field 		= isset($val[1])?$val[1]:'';
					$where_symbol 		= isset($val[2])?$val[2]:'';
					$where_val 			= isset($val[3])?$val[3]:'';
					if($where_type != 2 && $where_type != 3){
						$arr[] 			= $where_val;
					}

					if($where_type != 1 && $where_type != 3){
						$where_tb 		= $val[4].'.';
					}

					$where_field 		= $where_field;
					if($where_count != $j){
						$where_str     .= ($where_type == 2 || $where_type == 3)?
											" {$where_tb}{$where_field} {$where_symbol} AND ":
											" {$where_tb}`{$where_field}` {$where_symbol} ? AND ";
					}else{
						$where_str     .= ($where_type == 2 || $where_type == 3)?
											" {$where_tb}{$where_field} {$where_symbol} ":
											" {$where_tb}`{$where_field}` {$where_symbol} ? ";
					}

					$j++;
				}
				$sql   .= " WHERE $where_str ";
			}

			// ORDER BY
			$orderby_count 				= count($orderby);
			$k = 1;
			if(!empty($orderby) && $orderby_count > 0){
				foreach($orderby as $or_val){
					$orderby_tb 		= $this->mssql_real_escape_str($or_val[0]);
					$orderby_field 		= $this->tableField($or_val[1]);
					$orderby_val 		= $or_val[2];

					$orderby_order 		= !empty($orderby_val)?strtoupper($orderby_val):'ASC';
					$orderby_order  	= ($orderby_order == 'DESC')?$orderby_order:'ASC';
					$orderby_str    	.= ($orderby_count != $k)?
											"{$orderby_tb}.{$orderby_field} {$orderby_order},":
											"{$orderby_tb}.{$orderby_field} {$orderby_order}";
					$k++;
				}
				$sql   .= " ORDER BY $orderby_str ";
			}
			$sql        = $this->db->Prepare($sql);
			if($type == 1){
				$rs     = $this->db->SelectLimit($sql,$page_limit,$page_num,$arr);
	            if(!empty($rs)){
	                $return_data  		= $rs->getArray();
	            }
	        }elseif($type == 2){
	            $return_data      		= $this->db->getOne($sql,$arr);
	        }else{
	        	$rs 	= $this->db->Execute($sql,$arr);
	            if($rs && $rs->RecordCount() > 0){
					$return_data 		= $rs->getArray();
				}
	        }
		}
		return $return_data;
    }

	/**
	 *	新增資料
	 *	@param data  : 	array(
	 *					'field' => value
	 *				);
	 * 	@return true|false
	*/
	function insert_table_data($table,$data){
		$arr 		= array();
		$chk    	= false;
		$field_str  = $value_str 	= '';

		if(is_array($data) && !empty($data)){
			$data_count 	= count($data);
			$i = 1;
			foreach($data as $key => $val){
				$arr[] 				= trim($val);

				$field 		= trim($key);
				$field 		= $this->tableField($key);
				if($data_count != $i){
					$field_str     .= "$field,";
					$value_str     .= "?,";
				}else{
					$field_str     .= "$field";
					$value_str     .= "?";
				}
				$i++;
			}

			$sql 	 = "REPLACE INTO $table ($field_str) VALUES ($value_str)";
			$sql     = $this->db->Prepare($sql);
            if($this->db->Execute($sql,$arr)){
				$chk = true;
			}
		}
		return $chk;
    }

	/**
	 *	更新資料
	 *	@param data  : 	array(
	 *					'field' => array('=','value')
	 *				);
	 *	@param where : 	array(
	 *					'field' => array('=','value')
	 *				);
	 * 	@return true|false
	*/
	function update_table_data($table,$data,$where){
		$arr 		= array();
		$chk    	= false;
		$update_str = $where_str 		= '';
		$update_symbol 	= $where_symbol = '=';

		if(is_array($data) && !empty($data)){
			$data_count = count($data);
			$i 		= 1;
			foreach($data as $key => $val){
				if(is_array($val)){
					$update_symbol 		= $val[0];
					$data_val 	   		= $val[1];
					$arr[] 				= $data_val;
				}else{
					$arr[] 				= $val;
				}

				$field 	= $this->tableField($key);
				if($data_count != $i){
					$update_str    	   .= " $field $update_symbol ?, ";
				}else{
					$update_str        .= " $field $update_symbol ? ";
				}
				$i++;
			}

			$where_count = count($where);
			$j = 1;
			foreach($where as $key => $val){
				if(is_array($val)){
					$where_symbol 		= $val[0];
					$where_val 			= $val[1];
					$arr[] 				= $where_val;
				}else{
					$arr[] 				= $val;
				}

				$w_field = $key;
				if($where_count != $j){
					$where_str         .= " [$w_field] $where_symbol ? AND ";
				}else{
					$where_str         .= " [$w_field] $where_symbol ? ";
				}
				$j++;
			}

			$sql 		= "UPDATE $table SET $update_str WHERE $where_str";
			$sql        = $this->db->Prepare($sql);
            if($this->db->Execute($sql,$arr)){
				$chk 	= true;
			}
		}
		return $chk;
	}

	/**
     *  刪除資料
     *  @param where :  0:field;1:手key值;2:沒有值
     *              array(
     *                  array(0,'field','=','value'),
     *                  array(1,'concat(field1,field2)','LIKE','%value%'),
     *                  array(2,'field','IN (1,2,3,4)','')
     *              );
     *  @return true|false
    */
    function delete_table($table,$where){
        $arr        = array();
        $where_str  = '';

        $sql    = "DELETE FROM $table ";

        if(is_array($where) && !empty($where)){
            // WHERE
            $where_count                = count($where);
            $j = 1;
            if(!empty($where) && $where_count > 0){
                foreach($where as $key  => $val){
                    $where_type         = intval($val[0]);
                    $where_field        = $val[1];
                    $where_symbol       = $this->mssql_real_escape_str($val[2]);
                    $where_val          = $val[3];
                    if($where_type != 2){
                        $arr[]          = $where_val;
                    }

                    $where_field        = ($where_type != 1)?$this->tableField($where_field):
                    						$this->mssql_real_escape_str($where_field);
                    if($where_count != $j){
                        $where_str     .= ($where_type == 2)?
                                            " $where_field $where_symbol AND ":
                                            " $where_field $where_symbol ? AND ";
                    }else{
                        $where_str     .= ($where_type == 2)?
                                            " $where_field $where_symbol ":
                                            " $where_field $where_symbol ? ";
                    }

                    $j++;
                }
                $sql   .= " WHERE $where_str ";
            }
            $sql        = $this->db->Prepare($sql);
            if($this->db->Execute($sql,$arr)){
                return  true;
            }else{
                return  false;
            }
        }else{
            return  false;
        }
    }

    // escape_str
    function mssql_real_escape_str($value){
    	$character	= array('\x00','\n','\r',"\\","'",'"','\x1a');
    	foreach ($character as $character_val) {
    		$value 	= str_replace($character_val, '', $value);
    	}
		return $value;
    }

    function tableField($field,$left = '`',$right = '`'){
    	return ($left.$field.$right);
    }
}
?>
