const Number = [1,3,5,3,2,6]
const newNumber = [...Number,34,22,42]
console.log(Math.max(...newNumber));
console.log(Math.min(...newNumber));

const iGot = `all Number is : ${newNumber}`
console.log(iGot);