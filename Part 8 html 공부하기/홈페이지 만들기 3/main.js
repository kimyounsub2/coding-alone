let target = document.querySelector("#dynamic"); //dynamic이라는 id 속성값을 가지고 있는 문서 객체를 선택

function randomString(){
    let stringArr = ["Learn to HTML","Learn to CSS","Learn to Javascript","Learn to Python","Learn to Ruby"]
    let selectString = stringArr[Math.floor(Math.random()*stringArr.length)]//Math함수를 이용하여 랜덤함수를 불러올수 있다.
    //floor함수를 사용해서 소숫점을 없애주자
    let selectStringArr = selectString.split(""); // stringArr변수의 문구들을 스펠링 하나씩 나눠주기 위한 함수이다.
    return selectStringArr
}

// 타이핑 리셋 함수
function resetTyping(){
    target.textContent = "";
    dynamic(randomString());

}

//한글자씩 텍스트 출력함수
function dynamic(randomArr){

    if(randomArr.length >0){
        target.textContent += randomArr.shift();//shift함수는 배열이 있으면 제일 앞에 있는것을 빼준다.
        setTimeout(function(){
            dynamic(randomArr);
        },80);
    }else{
        setTimeout(resetTyping, 3000);
    }
}
dynamic(randomString());


// 커서 깜빡임 효과 함수
function blink(){
    target.classList.toggle("active");// active라는 클래스가 추가되었다가 삭제되는것을 반복하는 
}
setInterval(blink,500)  // setInterval은 반복 함수이다. 없애라(blink) 0.5초(500)동안

