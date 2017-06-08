//发送用户id和对局id
function submit_id()
{
    if($('#user_id').val() == '')
    {
        alert('您还尚未登录,请登录后再操作!');
        return
    }

    if ($('#game_id').val() == '')
    {
        alert('必须输入游戏id');
    }
    else
    {
        console.log($('#user_id').val() + $('#game_id').val());
        socket.emit('game_start', {user_id: $('#user_id').val(), game_id: $('#game_id').val()});
    }
}

///vs ai
function begin_ai_game()
{
    if($('#user_id').val() == '')
    {
        alert('您还尚未登录,请登录后再操作!');
        return
    }

    if ($('#game_id').val() == '')
    {
        alert('必须输入游戏id');
    }
    else
    {
        console.log($('#user_id').val() + $('#game_id').val());
        socket.emit('AI_event', {user_id: $('#user_id').val(), game_id: $('#game_id').val(), method: 'create'});
    }
}

//发送落子消息(用户间对战)
function play_chess_human(msg)
{
    if (DEBUG)
    {
        console.log('发送落子消息');
    }
    socket.emit('play_game_server', {user_id: $('#user_id').val(), game_id: $('#game_id').val(), msg: msg})
}

//发送人机对战落子信息
function play_chess_ai(msg)
{
    if(DEBUG)
    {
        console.log('发送人机对战消息');
    }
    socket.emit('AI_event', {user_id: $('#user_id').val(), game_id: $('#game_id').val(), msg: msg, method: 'play'});
}

//发送对话消息
$('form#sendmessage').submit(
    function submit_message()
    {
        if ($('#game_message').val() == '')
        {
            alert('不能发送空消息！');
        }
        else
        {
            socket.emit('message', {
                user_id: $('#user_id').val(),
                game_id: $('#game_id').val(),
                message: $('#game_message').val()
            });
        }
    }
);

function quit()
{
    if(game_ready)
    {
        socket.emit('game_over_event',
            {'game_id': $('#game_id').val(), 'winner': emeny_name, 'loser': $('#user_id').val()});
    }
}

function send_pass()
{
    if(game_ready && side_me == side_now && mypass==0)
    {
        setsystemmessage('PASS');
        if (side_me == 'black')
        {
            if (AI_mode)
            {
                play_chess_ai('B[tt]');
            }
            else
            {
                play_chess_human('B[tt]');
            }
        }
        else
        {
            if (AI_mode)
            {
                play_chess_ai('W[tt]');
            }
            else
            {
                play_chess_human('W[tt]');
            }
        }
        mypass=1;
        game.pass()
    }
}

function send_undo()
{
    if(game_ready && !AI_mode)
    {
        setsystemmessage('请求悔棋,等待中...');
        if (AI_mode)
        {
            play_chess_ai('undo');
        }
        else
        {
            play_chess_human('undo');
        }
    }
}

function undo_reply(reply)
{
    if (reply)
    {
        if(side_me == side_now)
        {
            have_undoed = true;
            game.undo();
            if(side_now == 'black')
            {
                side_now = 'white';
            }
            else
            {
                side_now = 'black';
            }
        }
        else
        {
            have_undoed = true;
            game.undo();
            have_undoed = true;
            game.undo();
        }
        setsystemmessage('您同意悔棋');
        play_chess_human('undo_agreed');
    }
    else
    {
        setsystemmessage('您不同意悔棋,游戏继续');
        play_chess_human('undo_reject');
    }
}



