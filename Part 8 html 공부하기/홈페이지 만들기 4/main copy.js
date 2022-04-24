//import BLOCKS from ".Part 8 html 공부하기/홈페이지 만들기 4/block.js"

//dom
const playground = document.querySelector(".playground > ul");
const gameText = document.querySelector(".game-text");
const scoreDisplay = document.querySelector(".score");
// Setting
const GAME_ROWS = 20;
const GAME_COLS = 10;

// variables 변동이 심한
let score = 0; // 초기 점수
let duration = 500; // 블록이 떨어지는 시간 0.5
let downInterval;
let tempMovingItem;

const BLOCKS = {
    tree: [ // ㅗ의 모형을 여러방향으로 만들기 위해
        [[2,1],[0,1],[1,0],[1,1]],
        [[1,2],[0,1],[1,0],[1,1]],
        [[1,2],[0,1],[2,1],[1,1]],
        [[2,1],[1,2],[1,0],[1,1]],
    ],
    square: [ //ㅁ모양
        [[0,0],[0,1],[1,0],[1,1]],
        [[0,0],[0,1],[1,0],[1,1]],
        [[0,0],[0,1],[1,0],[1,1]],
        [[0,0],[0,1],[1,0],[1,1]],
    ],
    bar: [ //ㅡ모양
        [[1,0],[2,0],[3,0],[4,0]],
        [[2,-1],[2,0],[2,1],[2,2]],
        [[1,0],[2,0],[3,0],[4,0]],
        [[2,-1],[2,0],[2,1],[2,2]],
    ],
    zee: [ // Z 모양
        [[0,0],[1,0],[1,1],[2,1]],
        [[0,1],[1,0],[1,1],[0,2]],
        [[0,1],[1,1],[1,2],[2,2]],
        [[2,0],[2,1],[1,1],[1,2]],
    ],
    elLeft: [ 
        [[0,0],[0,1],[1,1],[2,1]],
        [[1,0],[1,1],[1,2],[0,2]],
        [[0,1],[1,1],[2,1],[2,2]],
        [[1,0],[2,0],[1,1],[1,2]],
    ],
    elRight: [ 
        [[1,0],[2,0],[1,1],[1,2]],
        [[0,0],[0,1],[1,1],[2,1]],
        [[0,2],[1,0],[1,1],[1,2]],
        [[0,1],[1,1],[2,1],[2,2]],
    ],    
    
}

const movingItem = {
    type:"",
    direction: 3, // 블록을 좌우로 움직일때 좌표를 구하기 위해
    top: 0,
    left:0,
};


init()

// functons
function init(){
    tempMovingItem = {...movingItem};
    for (let i=0; i < GAME_ROWS; i++){
        prependNewLine()
    }
    generateNewBlock()
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
function renderBlocks(moveType = ""){
    const {type, direction, top, left} = tempMovingItem;
    const movingBlocks = document.querySelectorAll(".moving")
    movingBlocks.forEach(moving =>{
        moving.classList.remove(type,"moving");
    })

    BLOCKS[type][direction].some(block=>{
        const x = block[0] + left;
        const y = block[1] + top;
        //3항 연산자 : const xxx = 조건? 참일 경우:거짓일 경우 (조건이 오고 참일경우 그리고 거짓일 경우 변수에 담을수 있다.)
        const target = playground.childNodes[y] ? playground.childNodes[y].childNodes[0].childNodes[x] : null;// 세로가장 마지막값을 null지정
        const isAvailable = checkEmpty(target);
        if(isAvailable){
            target.classList.add(type, "moving")
        } else{
            tempMovingItem = {...movingItem}
            if(moveType === "retry"){
                clearInterval(downInterval)
                showGameoverText()
            }
            setTimeout(()=>{
                renderBlocks("retry");
                if(moveType ==="top") {
                    seizeBlock(); // 
                }
            },0)
            return true;
        }
    })
    movingItem.left = left;
    movingItem.top = top;
    movingItem.direction = direction;
}
function seizeBlock(){
    const movingBlocks = document.querySelectorAll(".moving")
    movingBlocks.forEach(moving =>{
        moving.classList.remove("moving");
        moving.classList.add("seized")
    })
    checkMatch()
}
function checkMatch(){
    const childNodes = playground.childNodes;
    childNodes.forEach(child=>{
        let matched = true;
        child.children[0].childNodes.forEach(li=>{
            if(!li.classList.contains("seized")){
                matched = false;
            }
        })
        if(matched){
            child.remove();
            prependNewLine()
            score++;
            scoreDisplay.innerText = score;
        }
    })
    generateNewBlock()
}



function generateNewBlock(){

    clearInterval(downInterval);
    downInterval = setInterval(()=>{
        moveBlock("top",1)
    },duration)


    const blockArray = Object.entries(BLOCKS);
    const randomIndex = Math.floor(Math.random() * blockArray.length)
    movingItem.type = blockArray[randomIndex][0]
    movingItem.top = 0;
    movingItem.left = 3;
    movingItem.direction = 0;
    tempMovingItem = { ...movingItem};
    renderBlocks()
}

function checkEmpty(target){
    if(!target || target.classList.contains("seized")){
        return false;
    }
    return true;
}

function moveBlock(moveType, amount){
    tempMovingItem[moveType] += amount;
    renderBlocks(moveType)
}
function changeDirection(){
    const direction = tempMovingItem.direction;
    direction === 3 ? tempMovingItem.direction = 0 : tempMovingItem.direction += 1;
    renderBlocks()
}
function dropBlock(){
    clearInterval(downInterval);
    downInterval = setInterval(()=>{
        moveBlock("top",1)
    },10)
}
function showGameoverText(){
    gameText.style.display = "flex"
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
        case 38: // direction을 바꿀때 UP키 키코드는 38이다
            changeDirection();
            break;
        case 32://스페이스바 코드가 32이다
            dropBlock();
            break;
        default:
            break;
    }
})
