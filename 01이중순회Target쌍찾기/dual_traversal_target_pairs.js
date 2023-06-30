//  이중순회 쌍 찾기 Dual Traversal Target Pair
//  dual traversal은 알고리즘의 핵심 개념이다.


// 문제
// 함수에 숫자 배열과 '특정수(target)'을 인자(Argument)로 넘기면,
// 더해서 '특정수(target)'이 나오는 index를 배열에 담아 return한다.

const nums = [4, 11, 14, 9];
const target = 13;

const twoSum = (nums, target) => {
    for(let i=0; i < nums.length-1; i++){
        for(let j=i+1; j < nums.length; j++){
            if(target == nums[i] + nums[j]){
                return [i, j];
            }
        }
    }
};

console.log(twoSum(nums,target));