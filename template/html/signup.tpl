<link rel="stylesheet" href="{CSSPATH}/w3.css">
<div id="signup">
    <h2>{HEADERTITLE}</h2>

    <div class="w3-container">
        <div class="w3-row">
            <div id="profile_tab" class="w3-third tablink w3-bottombar w3-hover-light-grey w3-padding w3-border-red">Profile</div>

            <div id="setting_tab" class="w3-third tablink w3-bottombar w3-hover-light-grey w3-padding">Setting</div>

            <div class="w3-third tablink w3-bottombar w3-hover-light-grey w3-padding">Complete</div>
        </div>

        <div id="profile" class="w3-panel city" style="display:block">
            <h6>{INPUTNAME}<label id="sign_name_error"></label></h6>
            <label>
                <input type="text" name="sname" id="sign_name" value="{name}" title="{INPUTNAME}" class="sprited" />
            </label>
            <h6>{PWD}<label id="sign_pwd_error"></label></h6>
            <label>
                <input type="password" name="pwd" id="sign_pwd" placeholder="{ALERTXT02}" title="{PWD}" class="sprited" />
            </label>
            <label id="pwdtxt"></label>
            <h6>{EMAIL}<label id="sign_mail_error"></label></h6>
            <label>
                <input type="text" name="mail" id="sign_mail" placeholder="{ALERTXT09}" value="{mail}" title="{EMAIL}" class="sprited">
            </label>
            <label id="mailtxt"></label>
            <h6>{AGE}</h6>
            <label>
                <select name="age" id="sign_age" style="height: 30px;width: 390px;border:1pt solid #8191A5;border-radius:4px;">
                    <option value="25">低於25歲</option>
                    <option value="34">25~34歲</option>
                    <option value="44">35~44歲</option>
                    <option value="54">45~54歲</option>
                    <option value="64">55~64歲</option>
                    <option value="65">65歲以上</option>
                </select>
            </label>
            <h6>{SEX}</h6>
            <label>
                <input type="radio" name="sex" value="M" checked="checked">
                <label for="M" style="float: left">{SEXM}</label>
                <input type="radio" name="sex" value="W">
                <label for="W">{SEXW}</label>
            </label>
            <h6>{AREA}</h6>
            <label>
                <select name="area" id="sign_area" style="height: 30px;width: 390px;border:1pt solid #8191A5;border-radius:4px;">
                    <!-- START BLOCK : show_area -->
                    <option value="{id}">{name}</option>
                    <!-- END BLOCK : show_area -->
                </select>
            </label>
            <p>
                <input type="button" id="sign_cancel" class="sprited cancel" onClick="self.location.href='index.php'" title="Cancel" />
                <input type="button" id="sign_sent" value="{SUBMIT}" class="sprited next" title="Next" />
            </p>
        </div>

        <div id="setting" class="w3-panel city" style="display:none">
            <form id="setting_form">
                <input type="hidden" id="profile_hid" name="profile_hid" value="">
            </form>
            <p>
                <input type="button" id="setting_cancel" class="sprited cancel" onclick="changeTab(0, 'profile');" title="Back" />
                <input type="button" id="setting_sent" class="sprited next" title="Next" />
            </p>
        </div>

        <div id="complete" class="w3-panel city" style="display:none">
            <p>Complete.</p>
        </div>
    </div>
</div>
<script>
$(document).ready(function(){
    var profile_hid = '';
    // Profile next
    $("#sign_sent").click(function(){
        if (!validate()) {
            return false;
        }else{
            profile_hid += $("#sign_name").val() + ';;';
            profile_hid += $("#sign_pwd").val()  + ';;';
            profile_hid += $("#sign_mail").val() + ';;';
            profile_hid += $("#sign_age").val() + ';;';
            profile_hid += $("input[type='radio'][name='sex']").val() + ';;';
            profile_hid += $("#sign_area").val() + ';;';

            $("#profile_hid").val(profile_hid);
            changeTab(1, 'setting');
        }
    });
    // Setting next
    $("#setting_sent").click(function(){
        //if (!validate()) {
        //    return false;
        //}else{
            var url         = "action.php?action=signup";
            var form_data   = $('#setting_form').serialize();
            $.ajax({
                url: url,
                type: 'POST',
                dataType: 'json',
                data: form_data,
            })
            .done(function(re_data) {
                if(re_data['status']){
                    var view_html =
                    "{INPUTNAME}："+re_data['data']['user_name']+"<br>"+
                    "{EMAIL}："+re_data['data']['user_mail']+"<br>"+
                    "{AGE}："+re_data['data']['user_age'];

                    $("#complete p").html(view_html);
                    changeTab(2, 'complete');
                }else{
                    $("#complete p").css("color","red").text(re_data['msg']);
                }
            })
            .fail(function() {
                //console.log("error");
            })
            .always(function() {
                //console.log("complete");
            });
    });
});
// Tab 切換
function changeTab(evt, tabName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("city");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" w3-border-red", "");
    }
    document.getElementById(tabName).style.display = "block";
    tablinks[evt].className += " w3-border-red";
}
// 檢查Profile資料
function validate() {
    var error   = 0;
    var pwdLen  = $("#sign_pwd").val().length;
    var reg     = new RegExp(/([\w\-]+\@[\w\-]+\.[\w\-]+)/);
    var reg3    = new RegExp(/[^\u4e00-\u9fa5]/);

    // name
    if( $("#sign_name").val() == '' ){
        $("#sign_name_error").css("color","red").text('＊');
        error++;
    }else{
        $("#sign_name_error").text('');
    }
    // pwd
    if( $("#sign_pwd").val() == ''){
        $("#sign_pwd_error").css("color","red").text('＊');
        error++;
    }else if(!reg3.test($("#sign_pwd").val())){
        $("#sign_pwd_error").css("color","red").text('＊');
        $("#pwdtxt").text("{ALERTXT01}");
        error++;
    }else if(pwdLen < 6){
        $("#sign_pwd_error").css("color","red").text('＊');
        $("#pwdtxt").css("color","red").text("{ALERTXT02}");
        error++;
    }else{
        $("#sign_pwd_error").text('');
        $("#pwdtxt").text("");
    }
    // mail
    if( $("#sign_mail").val() == '' ){
        $("#sign_mail_error").css("color","red").text('＊');
        error++;
    }else if(!reg.test($("#sign_mail").val())){
        $("#sign_mail_error").css("color","red").text('＊');
        $("#mailtxt").text("{ALERTXT03}");
        error++;
    }else{
        $.ajax({
            url: "action.php?action=chkmail",
            type: 'POST',
            dataType: 'json',
            data: {email: $("#sign_mail").val()},
            async: false,
        })
        .done(function(re_data) {
            if(!re_data['status']){
                $("#sign_mail_error").css("color","red").text('＊');
                $("#mailtxt").css("color","red").text(re_data['msg']);
                error++;
            }else{
                $("#sign_mail_error").text('');
            }
        })
        .fail(function() {
            //console.log("error");
        })
        .always(function() {
            //console.log("complete");
        });

    }

    // error
    if(error != 0) return false;
    else return true;
}
</script>