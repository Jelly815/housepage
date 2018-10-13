<!DOCTYPE html>
<head>
	  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
      <link rel=stylesheet type="text/css" href="{CSSPATH}style.css">
      <link rel=stylesheet type="text/css" href="{CSSPATH}bootstrap.min.css">
      <script src="js/jquery-1.11.1.js"></script>
      <script>
      $(document).ready(function(){
          /*function isChinese(str){
            var re=/[^\u4e00-\u9fa5]/;
            if(re.test(str)) return false;
            return true;
          }*/
          function validate() {
            var error=0;
            var pwdLen =$("#pwd").val().length;
			var reg = new RegExp(/([\w\-]+\@[\w\-]+\.[\w\-]+)/);
			var reg2 = new RegExp(/^[09]{2}[0-9]{8}$/);	
			var reg3 = new RegExp(/[^\u4e00-\u9fa5]/);
			//name
             if( $("#name").val()=='' ){
               $("#name").css("border-color","red");
               error++;
             }else{
               $("#name").css("border-color","");
             }
			//pwd
             if( $("#pwd").val()==''){
               $("#pwd").css("border-color","red");
               error++;
             }else if(!reg3.test($("#pwd").val())){
               $("#pwd").css("border-color","red");
               $("#pwdtxt").text("{ALERTXT01}");
               error++;
             }else if(pwdLen < 6){
               $("#pwd").css("border-color","red");
               $("#pwdtxt").text("{ALERTXT02}");
               error++;
             }else{
               $("#pwd").css("border-color","");
			   $("#pwdtxt").text("");
             }
			//phone
             if( $("#phone").val()=='' ){
               $("#phone").css("border-color","red");
               error++;
             }else if(!reg3.test($("#phone").val())){
               $("#phone").css("border-color","red");
               $("#phonetxt").text("{ALERTXT01}");
               error++;
             }
			/*else if(!reg2.test($("#phone").val())){
				$("#phone").css("border-color","red");
               	$("#phonetxt").text("ex:0912345678");
				error++;
			}*/
			else{
               $("#phone").css("border-color","");
			   $("#phonetxt").text("");
             }
			//mail
             if( $("#mail").val()=='' ){
               $("#mail").css("border-color","red");
               error++;
             }else if(!reg.test($("#mail").val())){
				$("#mail").css("border-color","red");
               	$("#mailtxt").text("{ALERTXT03}");
				error++;
			 }else{
               $("#mail").css("border-color","");
			   $("#mailtxt").text("");
             }
			//departmant
             if( $("#departmant").val()=='' ){
               $("#departmant").css("border-color","red");
               error++;
             }else{
               $("#departmant").css("border-color","");
             }
             //error
             if(error!=0) return false;
             else return true;
          }
          $("#sentSign").click(function(){
              if (!validate()) {
                    return false;
              }
          });
     });
     </script>
     <title>{TITLESIGN}</title>
</head>
<body>
<div id="header">
	<div class="header-logo"><a href="{INDEXPATH}" title="{HEADERTITLE}">{HEADERTITLE}</a></div>
    <div class="header-title"><a href="{LOGINPATH}" title="{LOGIN}">{LOGIN}</a></div>
    <div class="header-title"><a href="{SIGNPATH}" title="{TITLESIGN}">{TITLESIGN}</a></div>
</div>
<div id="loginContent">
<form action="index.php?op=sign&a=add" method="post" id="signForm" name="signForm">
      <table border="0" width="100%" cellpadding="0" cellspacing="0" id="loginTB">
        <th colspan="2"><h3 align="center">{TITLESIGN}</h3></th></tr>
        <tr>
            <td>{INPUTNAME}＊</td>
            <td><input type="text" name="name" id="name" value="{name}" title="{INPUTNAME}" /></td>
        </tr>
        <tr>
            <td>{PWD}＊</td>
            <td><input type="password" name="pwd" id="pwd" placeholder="{ALERTXT02}" title="{PWD}" /><label id="pwdtxt" class="errorColor"></label></td>
        </tr>
        <tr>
            <td>{INPUTPHONE}＊</td>
            <td><input type="text" name="phone" id="phone" value="{phone}" title="{INPUTPHONE}" /><label id="phonetxt" class="errorColor" ></label></td>
        </tr>
        <tr>
            <td>{EMAIL}＊</td>
            <td><input type="text" name="mail" id="mail" value="{mail}" title="{EMAIL}" /><label id="mailtxt" class="errorColor"></label></td>
        </tr>
        <tr>
            <td>{IMPUTPRTM}＊</td>
            <td><!--<input type="text" name="departmant" id="departmant" value="{prtm}" title="{IMPUTPRTM}" />-->
				<select name="departmant" id="departmant">
					<!-- START BLOCK : pic_row -->
					<option value="{id}">{title}</option>
					<!-- END BLOCK : pic_row -->
				</select>
			</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td><input type="submit" name="sentSign" id="sentSign" value="{SUBMIT}" class="btn" title="{SUBMIT}" />
            	<input type="button" name="button" id="button" value="{RETURNBTN}" class="btn" onClick="self.location.href='index.php'" /><br>
                <label class="errorColor">{error}</label>
                <input type="hidden" name="signHid" value="signForm">
            </td>
        </tr>
      </table>
</form>
</div>
</body>
</html>
