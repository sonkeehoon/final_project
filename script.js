var url = '127.0.0.1';
var port = '5500';


function message(){
    alert("예매가 완료되었습니다.")
}

function showInfo(){
    
    var date=document.getElementById("input_date").value;
    var concert=document.getElementById("concert").value;
    
    if(concert ==="선택하세요" ||  date===""){

        alert("날짜와 공연을 선택해 주세요.");
        document.querySelector('#seat_info').innerHTML="";

    }
    
    else {


        document.querySelector('#seat_info').innerHTML='남은좌석 : 10 \
        <input type="button" id="join" value="예매하기" onclick="message()">' ;
    }
}

function showLogin(){

    document.querySelector('.id').innerHTML= '<input type="text" id="ID" name="ID" placeholder="아이디">';
    document.querySelector('.pass').innerHTML= '<input type="password" id="password" name="password" placeholder="비밀번호">';
    document.querySelector('.button').innerHTML='<input type="button" id="login" name="button" value="로그인"></button>';
    document.querySelector('.join').innerHTML='<input type="button" id="login" name="button" \
    value="회원가입" onclick="showLoginPage()" ></button>';
  
}

function showLoginPage() {
    window.open('http://'+url+':'+port+'/join.html');
}

function showSeat() {
    window.open('http://'+url+':'+port+'/seat.html');
}

// function showTicketingPage() {
//     window.open('http://'+url+':'+port+'/ticketingPage.html');
// }



var Body={
            setColor : function (color){
                // document.querySelector('body').style.color = color;
                $('body').css('color',color);
            },
            setBgColor : function (color){
                // document.querySelector('body').style.backgroundColor = color;
                $('body').css('backgroundColor',color);
            }
        }



function nightDayHandler(self){
        
    if (self.value === 'night mode'){
        Body.setColor('white');
        Body.setBgColor('black');
        self.value='day mode';
    } else {
        Body.setColor('black');
        Body.setBgColor('bisque');
        self.value='night mode';
    }
}

function showDate(){
    document.querySelector('#date').innerHTML=Date()
}


function setBtnDisable(self){
    // var btn=document.getElementById("submit_btn");
    var btn=document.getElementById(self.id);

        btn.disabled="disabled";
        btn.style.backgroundColor="grey"
}


function onFocusHandler(){
    var input=document.getElementById("name");
    input.value='';
}