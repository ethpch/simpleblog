$(function () {
	$('#username').focus().blur(checkName);
	$('#password').blur(checkPassword);
});

function checkName() {
	var name = $('#username').val();
	if (name == null || name == "") {
		//alert error
		$('#count-msg').html("不能为空哦！");
		return false;
	}
	var reg = /^\w{3,10}$/;
	if (!reg.test(name)) {
		$('#count-msg').html("输入3-10个字母或数字或下划线！");
		return false;
	}
	$('#count-msg').empty();
	return true;
}

function checkPassword() {
	var password = $('#password').val();
	if (password == null || password == "") {
		//alert error
		$('#password-msg').html("密码不能为空");
		return false;
	}
	var reg = /^\w{3,10}$/;
	if (!reg.test(password)) {
		$('#password-msg').html("输入3-10个字母或数字或下划线");
		return false;
	}
	$('#password-msg').empty();
	return true;
}