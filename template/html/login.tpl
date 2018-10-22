<form action="" method="post" id="loginFrom" name="loginFrom">
<div id="sign_up" style="display: none; left: 50%; margin-left: -223px; z-index: 1002; position: absolute; top: 840px; margin-top: 0px;">
    <h3 id="see_id">會員登入</h3>
    <div id="sign_up_form">
        <label><strong>Username:</strong> <input type="text" name="mail" id="mail" placeholder="{EMAILTXT}" title="{EMAIL}" class="sprited" /></label>
        <label><strong>Password:</strong> <input type="password" name="pwd" id="pwd" title="{PWD}" class="sprited"></label>
        <div class="errorColor"></div>
        <div id="actions">
            <a class="close form_button sprited" id="cancel" href="javascript:;" title="Cancel"></a>
            <a class="form_button sprited" id="log_in" href="javascript:;" title="{LOGINBTN}"></a>
        </div>
    </div>
    <span>Don't be sad, just <a href="{SIGNPATH}">click here</a> to sign up!</span>
    <a id="close_x" class="close sprited" href="#">close</a>
</div>
</form>
<script>
    $('#login_btn').click(function(e) {
        $('#sign_up').lightbox({
            centered: true,
            onLoad: function() {
                $('#sign_up').find('input:first').focus();
            }
        });
        e.preventDefault();
    });

    $('#log_in').click(function(e) {
        var url     = "action.php?action=login";
        var user    = $("#mail").val();
        var pwd     = $("#pwd").val();

        if(user != '' && pwd != ''){
            $.ajax({
                type :"POST",
                url  : url,
                data : {
                    user : user,
                    pwd : pwd,
                },
                dataType: "json",
                success : function(re_data) {
                    if(re_data['status']){
                        $('.navigation #login_li').html('<a id="logout_btn" href="javascript:;" title="{LOGOUT}">{LOGOUT}</a>');
                        $('#log_in_text').text(re_data['msg']);
                        $('#log_in').trigger('close');
                    }else{
                        $('.errorColor').text(re_data['msg']);
                    }
                }
            });
        }else{
            $('#sign_up').lightbox({
                centered: true,
                onLoad: function() {
                    $('#sign_up').find('input:first').focus();
                    $('.errorColor').text('{ALERTXT05}');
                }
            });
            e.preventDefault();
        }
    });
</script>