<?php
header("Content-type:text/html;charset=utf-8");
include_once(__DIR__.'/../lib/setting.php');

class db_connect{
	public $conn,$db;

	public function __construct()
	{
		include_once(__DIR__.'/../include/adodb/adodb.inc.php');
		$this->db = ADONewConnection(DATATYPE);
		$this->db->Connect(SERVERNAME,USERNAME,USERPWD,DATANAME);
		$this->db->Execute("SET NAMES 'utf8'");

		$this->conn = $this->db->isConnected();
	}
}
?>