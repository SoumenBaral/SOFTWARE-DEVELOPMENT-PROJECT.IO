const person = {
    name : "Soumen",
    friends: ["shuvo","shakib","Alamin","Anoara"],
    shuvo_Activity: {
        job: "Vadaima",
        salary : null,
        Age : 25
    },
    Age: 26
}

// make function that will return a the value is od odd or even 

function OddOrEven(x) {
    if(x%2==0){
        console.log("Its a Even number");
    }
    else{
        console.log("Its defiantly Odd number ");
    }
}

OddOrEven(30)


// question 2: Is the year is leapYear ????


function leapYear(num){
    if(num%400 == 0){
        console.log("This is leapYear");
    }
    else if(num%100==0){
        console.log("This is not leapYear");
    }
    else if (num%4 == 0 ){
        console.log("This is leapYear baby ");
    }
    else{
        console.log("This is not leapYear");
    }
}


leapYear(2023)

for(let i = 1; i<50; i++){
    if(i%3==0 && i%5 == 0){
        console.log(i);
    }
}

friends =  ["shuvo","shakib","AlaminAlomHero","Anoara"]
let x = [""] ;
for (let i = 0; i < friends.length; i++) {
    const element = friends[i];
    console.log(element.length);
    if(x[0].length<element.length){
        x[0] = element;
    }
}
console.log(x[0]);


let numbers = [1,4,2,1,2,5,3,4,5];
const uniqueNumber = numbers[0];

for (let i = 0; i < numbers.length; i++) {
    const element = numbers[i];
    for (let j = 1; j < numbers.length-1; j++) {
        const AllElement = numbers[j];
        if (element !== AllElement) {
           console.log(AllElement);
        }

        
        
    }
}
