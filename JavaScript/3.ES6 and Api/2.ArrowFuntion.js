const math =()=>{
    console.log("asi ami ");
}
math()

const Number = [1,3,5,3,2,6]

const newNumber = Number.map(n=>n*2);
console.log(newNumber); 

const remove3 = Number.filter(x=>x!=3);
console.log(remove3);
const find3 = Number.find(x=> x==3)
console.log(find3);