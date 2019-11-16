$(document).ready(function() {
	$('#signupSubmit').on('click', function(e) {
		e.preventDefault();
		
		var name = $('#fullname').val();
		var email = $('#email').val();
		var pwd = $('#password').val();
		var cnfpwd = $('#cnfpassword').val();
		
		var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/i;
		
		if(email != "" && pwd != "" && cnfpwd != "") {
			if(pwd != cnfpwd) {
				$('#msg').html('<span style="color: red;">Password and confirm password must match</span>');
			} else if(!regex.test(email)) {
				$('#msg').html('<span style="color: red;">Invalid email address</span>');
			} else {
				$.ajax({
					method: "POST",
					url: '/signup',
					contentType: 'application/json;charset=UTF-8',
					data: JSON.stringify({'name': name, 'email': email, 'password': pwd}),
					dataType: "json",
					success: function(data) {
						$('#signupform').hide();
						$('#msg').html('<span style="color: green;">You are registered successfully</span>');
					},statusCode: {
						400: function() {
							$('#msg').html('<span style="color: red;">Bad request parameters</span>');
						},
						409 : function() {
							$('#msg').html('<span style="color: red;">You are already registered user</span>');
						}
					},
					error: function(err) {
						console.log(err);
					}
				});
			}
		} else {
			$('#msg').html('<span style="color: red;">All fields are required</span>');
		}
	});
});