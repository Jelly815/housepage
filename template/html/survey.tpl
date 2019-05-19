<style>
#featured label input[type="radio"] {
    background-position: -201px 0;
    padding: 2px 8px;
    line-height: 31px;
    width: 27px;
}
#featured label input[type="text"] {
    border: 1px #AAAAAA solid;
    height:20px;
    width:300px;
}
#featured label textarea {
    border: 1px #AAAAAA solid;
}
#sent_survey{
    position: absolute;
    margin: -350px 0 0 320px;
}
#sent_survey button{
    width:100px;
    height: 40px;
    cursor: pointer;
}
</style>
<div id="featured">
	<h2>{survey_title}</h2>
	<div>
        <form id="form_data">
		<div id="right">
			<ul>
                <!-- START BLOCK : view_list -->
                <li>
                    <p>
                        <label style="width: 460px;">{list_num}、{title}</label>
                        <label>{html}</label>
                    </p>
                </li>
                <!-- END BLOCK : view_list -->
			</ul>
		</div>
        </form>
	</div>
</div>
<div id="sent_survey"><button>送出</button></div>
<script>
$("#sent_survey button").on('click', function(event) {
    var url         = "action.php?action=survey";
    var form_data   = $('#form_data').serialize();
    console.log(form_data);
    $.ajax({
        url: url,
        type: 'POST',
        dataType: 'json',
        data: form_data,
    })
    .done(function(re_data) {
        if(re_data['status']){
            alert("感謝您的回饋!");
            document.location.href = "index.php";
        }else{
            console.log("error");
        }
    })
    .fail(function() {
        //console.log("error");
    })
    .always(function() {
        //console.log("complete");
    });
});
</script>