$(document).ready(function() {
	var isLoggedIn = localStorage.getItem('loggedin');
	
	if(isLoggedIn == 1) {
		$('#sign').hide();
		$('#loginform').hide();
		$('#signupform').hide();
		$('#logoff').show();
	} else {
		$('#sign').show();
		$('#logoff').hide();
	}
	
	$('#loginSubmit').on('click', function(e) {
		e.preventDefault();
		
		var email = $('#email').val();
		var pwd = $('#password').val();
		
		var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/i;
		
		if(email != "" && pwd != "" ) {
			if(!regex.test(email)) {
				$('#msg').html('<span style="color: red;">Invalid email address</span>');
			} else {
				$.ajax({
					method: "POST",
					url: '/login',
					contentType: 'application/json;charset=UTF-8',
					data: JSON.stringify({'username': email, 'password': pwd}),
					dataType: "json",
					success: function(data) {
						localStorage.setItem('loggedin', 1);
						
						$('#sign').hide();
						$('#loginform').hide();
						$('#logoff').show();
						$('#msg').html('<span style="color: green;">You are logged in</span>');
					},
					statusCode: {
						400: function() {
							$('#msg').html('<span style="color: red;">Bad request - invalid credentials</span>');
						}
					},
					error: function(err) {
						console.log(err);
					}
				});
			}
		} else {
			$('#msg').html('<span style="color: red;">Invalid username and password</span>');
		}
	});
	
	$('#logout').on('click', function(e) {
		e.preventDefault();
		
		$.ajax({
			url: '/logout',
			dataType: "json",
			success: function(data) {
				localStorage.setItem('loggedin', 0);
				$('#sign').show();
				$('#logoff').hide();
				$('#msg').html('<span style="color: green;">You are logged off</span>');
			},
			error: function(err) {
				console.log(err);
			}
		});
	});
});