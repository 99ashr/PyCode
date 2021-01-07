const mathBox = document.getElementById('math-box');
const option_1_pg = document.getElementById("option-1");
const option_2_pg = document.getElementById("option-2");
const option_3_pg = document.getElementById("option-3");
const emoji_show = document.getElementById('emoji-show');
const score_pg = document.getElementById('score-box');
const timer_pg = document.getElementById('time-box');
const lost_msg = document.getElementById('lost-msg');
const extra_msg = document.getElementById('extra-msg');
const play_again = document.getElementById('play-again-links');

var score = 0;
var correct_ans = null;

function start() {
    var ans_math = null;
    var qsn_math = null;
    option_1_pg.style.background = "#512275";
    option_2_pg.style.background = "#512275";
    option_3_pg.style.background = "#512275";

    function randomNumber(x) {
        return Math.floor((Math.random() * x) + 1);
    }

    var number1 = randomNumber(10);
    var number2 = randomNumber(10);
    var number3 = randomNumber(10);
    var number1_100 = randomNumber(100);
    var number2_100 = randomNumber(100);
    var number3_100 = randomNumber(100);

    var x = null;
    var x_ans = null;


    var randomNumber_for_operator = randomNumber(5);

    if (score < 20) {
        if (randomNumber_for_operator === 1) {
            qsn_math = number1 + "+" + number2;
            ans_math = number1 + number2;
        } else if (randomNumber_for_operator === 2) {
            qsn_math = number1 + "-" + number2;
            ans_math = number1 - number2;
        } else if (randomNumber_for_operator === 3) {
            qsn_math = number1 + "×" + number2;
            ans_math = number1 * number2;
        } else if (randomNumber_for_operator === 4) {
            var extra_num = number1 * number2;
            qsn_math = extra_num + "÷" + number2;
            ans_math = extra_num / number2;
        } else {
            x = number1;
            x_ans = x + number3;
            qsn_math = "X" + "+" + number3 + "=" + x_ans + "<br>X=?";
            ans_math = x;
        }
    } else if (score < 35) {
        if (randomNumber_for_operator === 1) {
            qsn_math = number1 + "+" + number2 + "+" + number3;
            ans_math = number1 + number2 + number3;
        } else if (randomNumber_for_operator === 2) {
            qsn_math = number1 + "-" + number2 + "-" + number3;
            ans_math = number1 - number2 - number3;
        } else if (randomNumber_for_operator === 3) {
            qsn_math = number1 + "×" + number2 + "×" + number3;
            ans_math = number1 * number2 * number3;
        } else if (randomNumber_for_operator === 4) {
            qsn_math = number1 + "²" + "+" + number2;
            ans_math = (number1 ** 2) + number2;
        } else {
            x = number2_100;
            x_ans = x + number3_100;
            qsn_math = "X" + "+" + number3_100 + "=" + x_ans + "<br>X=?";
            ans_math = x;
        }
    } else if (score < 50) {
        if (randomNumber_for_operator === 1) {
            qsn_math = number1_100 + "+" + number2_100 + "+" + number3_100;
            ans_math = number1_100 + number2_100 + number3_100;
        } else if (randomNumber_for_operator === 2) {
            qsn_math = number1_100 + "-" + number2_100 + "+" + number3_100;
            ans_math = number1_100 - number2_100 + number3_100;
        } else if (randomNumber_for_operator === 3) {
            qsn_math = number1_100 + "×" + number2;
            ans_math = number1_100 * number2;
        } else if (randomNumber_for_operator === 4) {
            qsn_math = number3 + "³" + "-" + number2;
            ans_math = (number3 ** 3) - number2;
        } else {
            x = number3;
            x_ans = x * number2;
            qsn_math = number2 + "x" + "=" + x_ans + "<br>X=?";
            ans_math = x;
        }
    } else if (score < 70) {
        if (randomNumber_for_operator === 1) {
            qsn_math = number1_100 + "+" + number2 + "×" + number3;
            ans_math = number1_100 + number2 * number3;
        } else if (randomNumber_for_operator === 2) {
            qsn_math = number1 + "²" + "+" + number2 + "°" + "+" + number3 + "³";
            ans_math = (number1 ** 2) + (number2 ** 0) + (number3 ** 3);
        } else if (randomNumber_for_operator === 3) {
            var extra_num2 = number1_100 * number3 * number2;
            qsn_math = extra_num2 + "÷" + number2;
            ans_math = extra_num2 / number2;
        } else if (randomNumber_for_operator === 4) {
            var extra_num3 = number3 ** 2;
            qsn_math = "√" + extra_num3 + "+" + number2;
            ans_math = (extra_num3 ** (1 / 2)) + number2;
        } else {
            x = number2_100;
            x_ans = number3_100 - x;
            qsn_math = number3_100 + "-" + "X" + "=" + x_ans + "<br>X=?";
            ans_math = x;
        }
    } else {
        if (randomNumber_for_operator === 1) {
            qsn_math = number1_100 + "-" + number2_100 + "×" + number3;
            ans_math = number1_100 - number2_100 * number3;
        } else if (randomNumber_for_operator === 2) {
            qsn_math = number1 + "²" + "+" + number2 + "²" + "+" + number3 + "²";
            ans_math = (number1 ** 2) + (number2 ** 2) + (number3 ** 2);
        } else if (randomNumber_for_operator === 3) {
            var extra_num4 = number1_100 * number3 * number2;
            qsn_math = extra_num4 + "÷" + number2 + "+" + number3_100;
            ans_math = extra_num4 / number2 + number3_100;
        } else if (randomNumber_for_operator === 4) {
            var extra_num5 = number1_100 ** 2;
            qsn_math = "√" + extra_num5 + "+" + number3_100 + "+" + number2;
            ans_math = (extra_num5 ** (1 / 2)) + number3_100 + number2;
        } else {
            x = number1;
            var extra_num6 = x * number3;
            x_ans = number3;
            qsn_math = extra_num6 + "÷" + "X" + "=" + x_ans + "<br>X=?";
            ans_math = x;
        }

    }

    function make_option(x, y, z) {
        option_1_pg.innerHTML = ans_math + x;
        option_2_pg.innerHTML = ans_math + y;
        option_3_pg.innerHTML = ans_math + z;
    }


    var randomNumber_for_option = randomNumber(33);
    if (randomNumber_for_option === 1) {
        make_option(0, 1, -1);
        correct_ans = option_1_pg;
    } else if (randomNumber_for_option === 2) {
        make_option(0, -1, 1);
        correct_ans = option_1_pg;
    } else if (randomNumber_for_option === 3) {
        make_option(1, 0, -1);
        correct_ans = option_2_pg;
    } else if (randomNumber_for_option === 4) {
        make_option(-1, 0, 1);
        correct_ans = option_2_pg;
    } else if (randomNumber_for_option === 5) {
        make_option(1, -1, 0);
        correct_ans = option_3_pg;
    } else if (randomNumber_for_option === 6) {
        make_option(-1, 1, 0);
        correct_ans = option_3_pg;
    } else if (randomNumber_for_option === 7) {
        make_option(0, 1, 2);
        correct_ans = option_1_pg;
    } else if (randomNumber_for_option === 8) {
        make_option(0, 2, 1);
        correct_ans = option_1_pg;
    } else if (randomNumber_for_option === 9) {
        make_option(1, 0, 2);
        correct_ans = option_2_pg;
    } else if (randomNumber_for_option === 10) {
        make_option(2, 0, 1);
        correct_ans = option_2_pg;
    } else if (randomNumber_for_option === 11) {
        make_option(1, 2, 0);
        correct_ans = option_3_pg;
    } else if (randomNumber_for_option === 12) {
        make_option(2, 1, 0);
        correct_ans = option_3_pg;
    } else if (randomNumber_for_option === 13) {
        make_option(0, -1, -2);
        correct_ans = option_1_pg;
    } else if (randomNumber_for_option === 14) {
        make_option(0, -2, -1);
        correct_ans = option_1_pg;
    } else if (randomNumber_for_option === 15) {
        make_option(-1, 0, -2);
        correct_ans = option_2_pg;
    } else if (randomNumber_for_option === 16) {
        make_option(-2, 0, -1);
        correct_ans = option_2_pg;
    } else if (randomNumber_for_option === 17) {
        make_option(-1, -2, 0);
        correct_ans = option_3_pg;
    } else if (randomNumber_for_option === 18) {
        make_option(-2, -1, 0);
        correct_ans = option_3_pg;
    } else if (randomNumber_for_option == 19) {
        make_option(-3, 0, 3);
        correct_ans = option_2_pg;
    } else if (randomNumber_for_option === 20) {
        make_option(-3, 3, 0);
        correct_ans = option_3_pg;
    } else if (randomNumber_for_option === 21) {
        make_option(0, 3, 4);
        correct_ans = option_1_pg;
    } else if (randomNumber_for_option === 22) {
        make_option(0, 4, 3);
        correct_ans = option_1_pg;
    } else if (randomNumber_for_option === 23) {
        make_option(3, 0, 4);
        correct_ans = option_2_pg;
    } else if (randomNumber_for_option === 24) {
        make_option(4, 0, 3);
        correct_ans = option_2_pg;
    } else if (randomNumber_for_option === 25) {
        make_option(3, 4, 0);
        correct_ans = option_3_pg;
    } else if (randomNumber_for_option === 26) {
        make_option(4, 3, 0);
        correct_ans = option_3_pg;
    } else if (randomNumber_for_option === 27) {
        make_option(0, -3, -4);
        correct_ans = option_1_pg;
    } else if (randomNumber_for_option === 28) {
        make_option(0, -4, -3);
        correct_ans = option_1_pg;
    } else if (randomNumber_for_option === 29) {
        make_option(-3, 0, -4);
        correct_ans = option_2_pg;
    } else if (randomNumber_for_option === 30) {
        make_option(-4, 0, -3);
        correct_ans = option_2_pg;
    } else if (randomNumber_for_option === 31) {
        make_option(-3, -4, 0);
        correct_ans = option_3_pg;
    } else if (randomNumber_for_option === 32) {
        make_option(-4, -3, 0);
        correct_ans = option_3_pg;
    } else {
        make_option(0, 5, -5);
        correct_ans = option_1_pg;
    }
    mathBox.innerHTML = qsn_math;
}

var do_nt_count = true;
var timer = 29;

function count_down(x) {
    do_nt_count = false;
    timer -= 1;
    setTimeout(function () {
        if (timer > -1) {
            if (timer < 4) {
                timer_pg.style.color = "#c90000";
            } else if (timer < 10) {
                timer_pg.style.color = "#e9de00";
            } else if (timer < 20) {
                timer_pg.style.color = "#03ae02";
            } else {
                timer_pg.style.color = "black";
            }
            timer_pg.innerHTML = "<h2>Time: " + timer + "</h2>";
            count_down();
        } else {
            lost_msg.innerHTML = "Game Over";
            extra_msg.innerHTML = "Ask your enemy to beat your score.<br>Your score is " + score;
            play_again.style.display = "block";
        }

    }, 1000);
}

var gameOver = false;
start();

function check_ans(x) {
    if (do_nt_count) {
        count_down();
    }
    option_1_pg.style.background = "red";
    option_2_pg.style.background = "red";
    option_3_pg.style.background = "red";
    correct_ans.style.background = "green";

    if (timer > -1) {

        setTimeout(function () {
            start();

        }, 500);
    } else {
        lost_msg.innerHTML = "Game Over";
        gameOver = true;
        extra_msg.innerHTML = "Ask your enemy to beat your score.<br>Your score is " + score;
        play_again.style.display = "block";
    }

    if (!gameOver) {


        if (x === correct_ans) {
            emoji_show.innerHTML = "✔️";
            score += 4;
            timer += 3;

        } else {
            emoji_show.innerHTML = "❌";
            score -= 3;
        }
    }
    score_pg.innerHTML = "<h2>Score: " + score + "</h2>";
}