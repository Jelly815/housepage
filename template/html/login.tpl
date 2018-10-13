<!DOCTYPE html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<link rel=stylesheet type="text/css" href="{CSSPATH}style.css">
        <link rel=stylesheet type="text/css" href="{CSSPATH}bootstrap.min.css">
	    <title>{TITLELOGIN}</title>
	</head>
	<body>
	<div>
		<div id="header">
			<div class="header-logo"><a href="{INDEXPATH}" title="{HEADERTITLE}">{HEADERTITLE}</a></div>
			<div class="header-title"><a href="{LOGINPATH}" title="{LOGIN}">{LOGIN}</a></div>
			<div class="header-title"><a href="{SIGNPATH}" title="{TITLESIGN}">{TITLESIGN}</a></div>
		</div>
		<div id="loginContent" align="center">
		<form action="" method="post" id="loginFrom" name="loginFrom">
		  <table border='0' width='100%' cellpadding="0" cellspacing="0" id="loginTB">
			<tr>
				<th colspan="2"><h3 align="center">{LOGIN}</h3></th>
			</tr>
			<tr>
				<td>{EMAIL}</td>
				<td><input type="text" name="mail" id="mail" placeholder="{EMAILTXT}" title="{EMAIL}" /></td>
			</tr>
			<tr>
				<td>{PWD}</td>
				<td><input type="password" name="pwd" id="pwd" title="{PWD}" /></td>
			</tr>
			<tr>
				<td>&nbsp;</td>
				<td><input type="submit" name="sentLogin" id="sentLogin" value="{LOGINBTN}" class="btn" title="{LOGINBTN}" />
					<input type="button" name="button" id="button" value="{SIGNBTN}" class="btn" onClick="self.location.href='index.php?op=sign'" /><br>
					<label class="errorColor">{error}</label>
					<input type="hidden" name="loginHid" value="loginFrom">
				</td>
			</tr>
		  </table>
		</form>
    </div>
	</div>
	</body>
</html>
