<div id="header">
    <ul id="navigation">
        <li>
            <a href="index.php" id="home">Home</a>
        </li>
        <li>
            <a href="mailto:jellyandjar@yahoo.com.tw" id="email">Email</a>
        </li>
    </ul>

    <a href="index.php" id="logo">
        <h1>{HEADERTITLE}</h1>
        <div style="position: relative;top: -20px;left: 30px;color:#093859;font-weight:bold;">{HEADERTITLEDTAIL}</div>
    </a>
    <ul class="navigation">
        <li class="selected first">
            <a href="index.php" title="{HOMEPAGE}">{HOMEPAGE}</a>
        </li>
        <li>
            <a href="ships.html" title="{ADSEARCH}">{ADSEARCH}</a>
        </li>
        <li>
            <a id="login_btn" href="javascript:;" title="{LOGIN}">{LOGIN}</a> | <a href="{SIGNPATH}" title="{TITLESIGN}">{TITLESIGN}</a>
        </li>
    </ul>
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
        <div>
            <h3>Find A Cruise</h3>
            <form action="">
                <select name="" id="">
                    <option value="month">Any Month</option>
                </select>
                <select name="" id="">
                    <option value="destinations">Any Destinations</option>
                </select>
                <select name="" id="">
                    <option value="ship">Any Ship</option>
                </select>
                <select name="" id="">
                    <option value="port">Any Departure Port</option>
                </select>
                <input type="submit" value=""/>
            </form>
            <div>
                <h3>Already Booked?</h3>
                <ul>
                    <li>
                        <a href="excursions.html">Check out our Excursions</a>
                        <p>You can remove any link to our website from this website template.</p>
                    </li>
                    <li>
                        <a href="restaurant.html">Check out our Specialty Restaurant</a>
                        <p>You're free to use this website template without linking back to us.</p>
                    </li>
                    <li>
                        <a href="activities.html">Check out our Special Activities</a>
                        <p>Please don't hesitate to ask for help on the <a href="http://www.freewebsitetemplates.com/forum/">Forum</a>.</p>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</div>
<form action="" method="post" id="loginFrom" name="loginFrom">
<div id="sign_up" style="display: none; left: 50%; margin-left: -223px; z-index: 1002; position: absolute; top: 840px; margin-top: 0px;">
    <h3 id="see_id">會員登入</h3>
    <div id="sign_up_form">
        <label><strong>Username:</strong> <input type="text" name="mail" id="mail" placeholder="{EMAILTXT}" title="{EMAIL}" class="sprited" /></label>
        <label><strong>Password:</strong> <input type="password" name="pwd" id="pwd" title="{PWD}" class="sprited"></label>
        <div class="errorColor"></div>
        <div id="actions">
            
            <a class="close form_button sprited" id="cancel" href="#">Cancel</a>
            <a class="form_button sprited" id="log_in" title="{LOGINBTN}">Sign in</a>
        </div>
    </div>
    <span>Don't be sad, just <a href="{SIGNPATH}">click here</a> to sign up!</span>
    <a id="close_x" class="close sprited" href="#">close</a>
</div>
</form>
<script>
    $('#login_btn').click(function(e) {
        $('#sign_up').lightbox_me({
            centered: true, 
            onLoad: function() { 
                $('#sign_up').find('input:first').focus()
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
                dataType: "text",
                success : function(re_data) {
console.log(re_data);                           
                }
            });
        }else{
            $('#sign_up').lightbox_me({
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