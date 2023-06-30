//  숫자 뒤집기 Number Reverse


// 문제
// Reverse 함수에 정수인 숫자를 인자로 받는다. 숫자를 뒤집어 return한다.

function reverse(x){
    const reversedStr = [...x.toString()].reverse().join('');
    const reversedNum = parseInt(reversedStr);
    return reversedNum;
};

console.log(reverse(2024));