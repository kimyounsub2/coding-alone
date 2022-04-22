// html에서 타입에다 module을 넣으면 js를 불러오지를 못한다.

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

export default BLOCKS;