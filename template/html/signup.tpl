<link rel="stylesheet" href="{CSSPATH}/w3.css">
<div id="signup">
    <h2>{PAGE_TITLE}</h2>

    <div class="w3-container">
        <div class="w3-row">
            <a href="javascript:void(0)" onclick="openCity(event, 'profile');">
                <div class="w3-third tablink w3-bottombar w3-hover-light-grey w3-padding w3-border-red">Profile</div>
            </a>
            <a href="javascript:void(0)" onclick="openCity(event, 'setting');">
                <div class="w3-third tablink w3-bottombar w3-hover-light-grey w3-padding">Setting</div>
            </a>
            <a href="javascript:void(0)" onclick="openCity(event, 'complete');">
                <div class="w3-third tablink w3-bottombar w3-hover-light-grey w3-padding">Complete</div>
            </a>
        </div>

        <div id="profile" class="w3-panel city" style="display:block">
            <h6><font color="red">＊</font> {INPUTNAME}</h6>
            <label>
                <input type="text" name="sname" id="sign_name" value="{name}" title="{INPUTNAME}" class="sprited" />
            </label>
            <h6><font color="red">＊</font> {PWD}</h6>
            <label>
                <input type="password" name="pwd" id="sign_pwd" placeholder="{ALERTXT02}" title="{PWD}" class="sprited" />
            </label>
            <label id="pwdtxt" class="errorColor"></label>

            <h6><font color="red">＊</font> {EMAIL}</h6>
            <label>
                <input type="text" name="mail" id="sign_mail"  value="{mail}" title="{EMAIL}" class="sprited">
            </label>
            <label id="mailtxt" class="errorColor"></label>

            <p>
                <input type="button" name="cancel" id="sign_cancel" value="{RETURNBTN}" class="sprited" onClick="self.location.href='index.php'" />
                <input type="button" name="sentSign" id="sign_sent" value="{SUBMIT}" class="sprited" title="{SUBMIT}" />

                <label class="errorColor">{error}</label>
                <input type="hidden" name="signHid" value="signForm">
            </p>

        </div>

        <div id="setting" class="w3-panel city" style="display:none">
            <h2>Setting</h2>
            <p>Setting.</p>
        </div>

        <div id="complete" class="w3-panel city" style="display:none">
            <h2>Complete</h2>
            <p>Complete.</p>
        </div>
    </div>


    <h3></h3>



</div>
<script>
$(document).ready(function(){
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
function openCity(evt, cityName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("city");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" w3-border-red", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.firstElementChild.className += " w3-border-red";
}
</script>