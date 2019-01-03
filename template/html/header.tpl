<div class="header">
    <ul id="navigation">
        <li>
            <a href="index.php" id="home" title="Home">Home</a>
        </li>
        <li>
            <a href="mailto:{ADMINMAIL}" id="email" title="Email">Email</a>
        </li>
    </ul>
    <div id="log_in_text">{USER_NAME}</div>
    <a href="index.php" id="logo" title="{HEADERTITLE}">
        <h1>{HEADERTITLE}</h1>
        <div>{HEADERTITLEDTAIL}</div>
    </a>
    <ul class="navigation">
        <li {SELECTED_DEFAULT}>
            <a href="index.php" title="{HOMEPAGE}">{HOMEPAGE}</a>
        </li>
        <li>
            <a id="navi_search" href="javascript:;" title="{ADSEARCH}">{ADSEARCH}</a>
        </li>
        <li {SELECTED_SIGNUP} id="login_li">
            {LOGIN_URL}
        </li>
    </ul>
    <div id="search_div">
        <input id="search_key" name="key" type="text" value="" placeholder="{ALERTXT11}">
        <a class="search_key_button sprited" id="key_button" href="javascript:;" title=""></a>
        <!--
        <form class="attireCodeToggleBlock" action="" style="display: none">
            <input
                    type="text"
                    multiple = "multiple"
                    class="multipleInputDynamicWithInitialValue"
                    name="search_key"
                    data-url="json/data.json"
                    placeholder="{ALERTXT10}"
                    id="area"
            />

            <button class="submitBtn" type="submit">Submit</button>
        </form>-->
    </div>
    <!-- START BLOCK : index_header -->
    <div id="featured">
        <div class="first">
            <ul>
                <li class="selected first">
                    <a href="featured.html">Featured Destinations</a>
                    <div>
                        <a href="featured.html">
                            <img src="template/images/couples.jpg" alt=""/>
                        </a>
                        <p>This website template has been designed by
                            <a href="http://www.freewebsitetemplates.com/">Free Website Templates</a> for you, for free. You can replace all this text with your own text.
                        </p>
                    </div>
                </li>
                <li>
                    <a href="deals.html">Hot Deals</a>
                    <div>
                        <a href="deals.html">
                            <img src="template/images/riverside.jpg" alt=""/>
                        </a>
                        <p>You can remove any link to our website from this website template, you're free to use this website template without linking back to us.
                        </p>
                    </div>
                </li>
                <li>
                    <a href="offers.html">Special Offers</a>
                    <div>
                        <a href="offers.html">
                            <img src="template/images/mountains.jpg" alt=""/>
                        </a>
                        <p>If you're having problems editing this website template, then don't hesitate to ask for help on the <a href="http://www.freewebsitetemplates.com/forum/">Forum</a>.
                        </p>
                    </div>
                </li>
            </ul>
        </div>

    </div>
    <!-- END BLOCK : index_header -->
</div>
<script>
$(function () {
    //var $select = $('select');

    // Run, fire and forget
    //$select.fastselect()

    // Run via plugin facade and get instance
    //var fastSelectInstance = $select.fastselect(options).data('fastselect');

    // run directly
    //var fastSelectInstance = new $.Fastselect($select.get(0), options);
    // 關鍵字搜尋
    $('#search_key').tagsInput({placeholder:'{ALERTXT11}'});
    // 縣市
    //$('.singleSelect').fastselect();
    //$('.multipleInputDynamicWithInitialValue').fastselect();
    $('#search_city').change(function(event) {
        if($(this).select().val() != ''){
            $('.attireCodeToggleBlock').show();
            //$('.fstMultipleMode .fstResultItem').remove();
//console.log('start');
            $.ajax({
                url: 'action.php',
                type: 'GET',
                dataType: 'json',
                async: false,
                data: {
                    action: 'getarea',
                    city_id: $(this).select().val()},
            })
            .done(function(re_data) {
                var new_option = '';

                $.each(re_data, function(i, val) {
                     new_option += '<span id="'+re_data[i].value+'" class="fstResultItem">'+re_data[i].text+'</span>';
                });

                $('.attireCodeToggleBlock .fstResults').remove('span').html(new_option);

                $('.multipleInputDynamicWithInitialValue').fastselect();
                $('.multipleInputDynamicWithInitialValue').data('data-url', 'json/data.json');
            })
            .fail(function() {
                console.log("error");
            });
            /*
            $.get('action.php',
                {
                    action: 'getarea',
                    city_id: $(this).select().val()
                },
                function(re_data){
                    var restaurant = $('.multipleInputDynamicWithInitialValue');

                    var owner = restaurant.data("data-url");
                    restaurant.data("data-url", JSON.parse("json/data.json"));
                    //console.log(re_data);
                    //$('.multipleInputDynamicWithInitialValue').data(re_data);

                    //var a = $('.multipleInputDynamicWithInitialValue').data('data-url'); //getter

                    //$('.multipleInputDynamicWithInitialValue').data('data-url',"json/data.json"); //setter
                }
            );*/
        }else{
            $('.attireCodeToggleBlock').hide();
        }
    });
    $('#navi_search').click(function(event) {
        $('.navigation li').removeClass('selected first');
        $(this).parent('li').addClass('selected first');
        $('#search_div').show().css('display',"inline-block" );
    });
});
</script>