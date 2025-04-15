const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().trim().split(" ").map(Number);

function solution(input){
    const [a, b] = input;
    console.log((a+b) * (a-b))
    return
}

solution(input);