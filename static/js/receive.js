var socket = io.connect();
$(document).ready(function ()
    {
        var allcookies = document.cookie;

        checkcookies(allcookies);
        socket.on('connect', function ()
            {
                //socket.emit('connect_event', {data: '连接成功'});
                console.log('连接成功');
            });
        socket.on('server_response', function (msg)
            {
                if (DEBUG)
                {
                    console.log(msg);
                }
            });
    });
socket.on('game_start', function (msg)
    {
        if (DEBUG)
        {
            console.log(msg)
        }
        if (msg.user_id == $('#user_id').val() && msg.begin == 0 && msg.game_id == $('#game_id').val())
        {
            console.log('成功创建游戏');
            alert('成功创建游戏，ID为:' + msg.game_id);
            side_me = msg.side;
            game_started = 0;
            game_ready = false;

        }
        if (msg.game_id == $('#game_id').val() && msg.user_id != $('#user_id').val() && msg.begin == 1)
        {
            alert('另一个用户成功连接,游戏开始!');
            $('#gameinfo').text($('#user_id').val() + '(黑)和' + msg.user_id + '(白)的对决');
            emeny_name = msg.user_id;
            $('div#player_side').text('你执黑棋');
            game_ready = true;
            side_now='black';
            side_me = 'black';
        }
        if (msg.game_id == $('#game_id').val() && msg.user_id == $('#user_id').val() && msg.begin == 1)
        {
            alert('成功连接游戏,游戏开始!');
            $('#gameinfo').text(msg.emeny + '(黑)和' + $('#user_id').val() + '(白)的对决');
            emeny_name = msg.emeny
            side_me = 'white';
            side_now = 'black';
            game_ready = true;
            $('div#player_side').text('你执白棋');

        }
    }
);

//开始游戏错误信息
socket.on('start_error', function (msg)
    {
        if (DEBUG)
        {
            console.log(msg)
        }
        if (msg.game_id == $('#game_id').val())
        {
            alert('加入游戏失败,该游戏ID已被使用');
        }
    });

//人人对战收到的落子信息
socket.on('play_game_client', function (msg)
    {
        //alert('接受到信息');
        //game = eval('new Map(' + msg.data + ')');

        var game_msg = msg;
        if (game_msg.game_id == $('#game_id').val() && game_msg.user_id != $('#user_id').val())
        {
            if (game_msg.msg == 'undo')
            {
                var r = confirm('对方请求悔棋');
                undo_reply(r);
                return;
            }
            if (game_msg.msg == 'undo_agreed')
            {
                if(side_me == side_now)
                {
                    have_undoed = true;
                    game.undo();
                    have_undoed = true;
                    game.undo();
                }
                else
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
                setsystemmessage('对方同意悔棋,悔棋成功!');
                return;
            }
            if (game_msg.msg == 'undo_reject')
            {
                setsystemmessage('对方不同意悔棋,游戏继续');
                return;
            }
            var place = game_msg.msg;
            var letter_x = place.charAt(2);
            var letter_y = place.charAt(3);
            var n_x = string.indexOf(letter_x);
            var n_y = string.indexOf(letter_y);
            if(DEBUG)
            {
                console.log('收到落子消息')
                console.log(msg)
            }
            mypass=0;
            if (place.charAt(0) == 'B')
            {
                side_now = "white";
            }
            else
            {
                side_now = "black";
            }
            if(DEBUG)
            {
                console.log('改变当前势力');
                console.log(side_now);
            }
            if (side_me == side_now)
            {
                setsystemmessage('敌方落子:[' + letter_x + ',' + letter_y + ']\n现在轮到我方落子');
            }

            if (n_x == 19 && n_y == 19)
            {
                game.pass();
                setsystemmessage('敌方放弃落子\n现在轮到我方落子')
            }
            else
            {
                peer_play = true;
                game.playAt(n_x, n_y);
            }

        }
    }
);

//与AI对战的游戏开始事件
socket.on('ai_game_start', function (msg)
    {
        game_started = 1;
        AI_mode = true;
        game_ready = true;
        side_me = 'black';
        $('#gameinfo').text($('#user_id').val()+'(黑)与MuGo(白)的对局');
        alert('对局开始');
    });


//接受AI落子信息
socket.on('ai_game_client', function (msg)
    {

        var place = msg.msg;
        var letter_x = place.charAt(2);
        var letter_y = place.charAt(3);
        var n_x = string.indexOf(letter_x);
        var n_y = string.indexOf(letter_y);
        if(DEBUG)
        {
            console.log('AI落子信息', msg);
            console.log(n_x, ' ', n_y);
        }
        peer_play = true;
        game.playAt(n_x,n_y);
        setsystemmessage('敌方落子:[' + letter_x + ',' + letter_y + ']\n现在轮到我方落子');

    });

socket.on('game_info', function (msg)
    {
        if (DEBUG)
        {
            console.log(msg)
        }
        $('#game_info_content').html(msg.data);
    });

//收到message
socket.on('message', function (msg)
    {
        //只有game_id一致时才显示

        if (msg.game_id == $('#game_id').val())
        {
            setmessage(msg.user_id + ':' + msg.message);
            if (DEBUG)
            {
                console.log('收到聊天信息', msg)
            }
        }
    });

//游戏结束事件
socket.on('game_over', function (msg)
    {
        if(game_ready && msg.game_id == $('#game_id').val())
        {
            game_ready = false;

            if(msg.winner == $('#user_id').val())
            {
                alert('对手认输,恭喜你获得胜利!');
                setsystemmessage('游戏结束\n胜利者是'+msg.winner+'\n刷新页面开始下一句游戏');
            }
            else
            {
                alert('很遗憾,你失败了......');
                setsystemmessage('游戏结束\n胜利者是'+msg.winner+'\n刷新页面开始下一句游戏');
            }

        }

    });

//获取对局信息
function get_game_info()
{
    socket.emit('get_wait_game', {});
}

//显示收到的消息，可以用更美观的方式实现
//TODO
function setmessage(msg)
{
    $('div#gamemessage').append('<br>' + $('<div/>').text(msg).html());
}

//设置系统消息
function setsystemmessage(msg)
{
    $('div#system_message').text(msg);
}
