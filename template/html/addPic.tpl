<script>
$(document).ready(function() {
	$("#sentAddPic").click(function(){
		if( $("#title").val()=='' ){
			$("#title").css("border-color","red");
			return false;
		}else{
			$("#title").css("border-color","");
		}
		if($('#picFile1').val()==''){
			$("#picFile1Txt").text("{ALERTXT08}"); 
			return false;
		}
	});
    
	$('#picFile1').change(function(){  
		var file = this.files[0]; 
		size = file.size; 
		type = file.type; 
		
		if(file.size > {FILESIZE}) { 
			$("#picFile1Txt").text("{PICDSCRIPT3}"); 
			$(this).val(''); 
		}
		else if(file.type != 'image/jpg' && file.type != 'image/jpeg' ) { 
			$("#picFile1Txt").text("{PICDSCRIPT}");
			$(this).val(''); 
		}else{
			$("#picFile1Txt").text("");
		}
	});
});
</script>
<div id="picContent" align="center">
<form action="index.php?op=addPic&a=add" method="post" id="addPicForm" name="addPicForm" Enctype="Multipart/Form-Data">
      <table border="0" width="100%" cellpadding="0" cellspacing="0" id="loginTB">
        <tr>
            <th colspan="2"><h3>{TITLEADDPIC}</h3></th>
        </tr>
        <tr>
            <td>{PICTITLE}＊</td>
            <td><input type="text" name="title" id="title" value="{title}" title="{PICTITLE}" placeholder="{PICTITLEDSCPT}" size="30" maxlength="15" />
			    <label id="titleTxt" class="errorColor"></label>
			</td>
        </tr>
        <tr>
            <td>{PIC}＊<br>({PICDSCRIPT}<br>{PICDSCRIPT3})</td>
            <td><p><input Type="file" name="picFile1"  id="picFile1" title="{PICDSCRIPT}" accept="image/jpeg">
				   <label id="picFile1Txt" class="errorColor"></label>
				</p>
			</td>
        </tr>
        <tr>
            <td>{PICAPTION}</td>
            <td><textarea name="caption" id="caption" cols="32" rows="11" title="{PICAPTION}" placeholder="{PICAPDSCPT}" maxlength="150"></textarea>
				<label id="captiontxt" class="errorColor"></label></td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td><input type="submit" name="sentAddPic" id="sentAddPic" title="{SUBMIT}" class="btn" value="{SUBMIT}" />
                <input type="button" name="button" id="button" value="{RETURNBTN}" class="btn" onclick="self.location.href='{LOGINTOPATH}'" /><br>
                <label class="errorColor">{error}</label>
                <input type="hidden" name="addPicHid" value="addPicForm">
            </td>
        </tr>
      </table>
</form>
</div>
