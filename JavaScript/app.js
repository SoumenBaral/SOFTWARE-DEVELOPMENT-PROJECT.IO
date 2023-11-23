let x = 343.23223232
// We need to take 2 number after decimal point 

console.log(x.toFixed(2));

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
console.log(Object.keys(person) );
console.log(Object.values(person.shuvo_Activity) );
console.log(Object.entries(person))