//登出
function logout()
{
    document.cookie="user_id=;";
    document.cookie="login=false;";
    window.location.reload();
    alert('logout');
}

//检查是否已经登录
function check_login(cookie)
{

    if (cookie.match(/login=true/))
    {
        return true;
    }
    return false;
}
//从cookie获取用户ID
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
//检查cookies
function checkcookies(allcookies)
{

    var cookies_list = allcookies.replace(" ", "").split(";");

    if (cookies_list.some(check_login))
    {
        $('#login_reg').css('display','none');
        $('#user_id_display').text(get_user_id(cookies_list))
        $('#user_id').val(get_user_id(cookies_list));
    }
    else
    {
        //alert('您尚未登录！请登录!');
        $('#user_information').css('display','none');

        //window.location.href = "/login";
    }
}

