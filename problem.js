"use strict";

const sumOfArr = (arr) => {
    let sum = 0;
    for (let i=0; i<arr.length; i++) {
    //   console.log(arr[i]);
      sum += arr[i];
    }
    console.log(sum);
//   let sum = 0;
//   for (let x in arr) {
//     // console.log(arr[x]);
//     sum += arr[x];
//   }
//   console.log(sum);
};

const arr = [1, 2, 3, 4, 10, 11];
sumOfArr(arr);
