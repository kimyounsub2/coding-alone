//dom
const playground = document.querySelector(".playground > ul");

// Setting
const GAME_ROWS = 20;
const GAME_COLS = 10;

// variables 변동이 심한
let score = 0; // 초기 점수
let duration = 500; // 블록이 떨어지는 시간 0.5
let downInterval;
let tempMovingItem;

const BLOCKS = {
    tree: [ // tree는 모형을 돌렸을때 모양을 의미하기 위해 임의로 선언함
        [[2,1],[0,1],[1,0],[1,1]],
        [],
        [],
        [],
    ]
}

const movingItem = {
    type:"tree",
    direction: 0, // 블록을 좌우로 움직일때 좌표를 구하기 위해
    top: 0,
    left:3,
};


init()

// functons
function init(){
    tempMovingItem = {...movingItem};
    for (let i=0; i < GAME_ROWS; i++){
        prependNewLine()
    }
    renderBlocks()
}


function prependNewLine(){
    const li = document.createElement("li");
    const ul = document.createElement("ul");
    for(let j=0; j<GAME_COLS; j++){
        const matrix = document.createElement("li");
        ul.prepend(matrix);
    }
    li.prepend(ul)
    playground.prepend(li)

}
function renderBlocks(){
    const {type, direction, top, left} = tempMovingItem;
    const movingBlocks = document.querySelectorAll(".moving")
    movingBlocks.forEach(moving =>{
        moving.classList.remove(type,"moving");
    })

    BLOCKS[type][direction].forEach(block=>{
        const x = block[0] + left;
        const y = block[1] + top;
        //3항 연산자 : const xxx = 조건? 참일 경우:거짓일 경우 (조건이 오고 참일경우 그리고 거짓일 경우 변수에 담을수 있다.)
        const target = playground.childNodes[y] ? playground.childNodes[y].childNodes[0].childNodes[x] : null;// 세로가장 마지막값을 null지정
        const isAvailable = checkEmpty(target);
        if(isAvailable){
            target.classList.add(type, "moving")
        } else{
            tempMovingItem = {...movingItem}
            renderBlocks()
        }
        
    })
}
function checkEmpty(target){
    if(!target){
        return false;
    }
    return true;
}

function moveBlock(moveType, amount){
    tempMovingItem[moveType] += amount;
    renderBlocks()
}

//event handing 키를 눌렀을때 행동
document.addEventListener("keydown", e =>{
    switch(e.keyCode){
        case 39://오른쪽 키 코드가 39이다.
            moveBlock("left",1);
            break;
        case 37:// 왼쪽 키코드가 37이다.
            moveBlock("left", -1);
            break;
        case 40:// 아래 키코드가 40이다.
            moveBlock("top",1);
            break;
        default:
            break;
    }
})
