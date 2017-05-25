/**
 * Created by cyj on 2017/5/22.
 */
function logout()
{
	document.cookie="user_id=;";
	document.cookie="login=false;";
	window.location.reload();
	alert('logout');
}

function check_login(cookie)
{
	console.log(cookie);
	if (cookie.match(/login=true/))
	{
		return true;
	}
	return false;
}
function get_user_id(cookies)
{
	var i;
	for (i = 0; i < cookies.length; i++)
	{
		if (cookies[i].search('user_id') != -1)
		{
			var res = cookies[i].split('=')[1];
			return res;
		}
	}
}

function checkcookies(allcookies)
{
	console.log(allcookies);
	console.log(allcookies.replace(" ", ""));
	var cookies_list = allcookies.replace(" ", "").split(";");
	console.log(cookies_list);
	if (cookies_list.some(check_login))
	{
		$('#login_reg').css('display','none');
		$('#user_id_display').text(get_user_id(cookies_list))
	}
	else
	{
		//alert('您尚未登录！请登录!');
		$('#user_information').css('display','none');

		//window.location.href = "/login";
	}
}