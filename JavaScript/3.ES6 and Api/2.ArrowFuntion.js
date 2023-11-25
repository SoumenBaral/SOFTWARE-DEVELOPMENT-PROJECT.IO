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

 Number.forEach(element => {
    console.log(element);
    const h1  = document.createElement("h1");
    h1.innerText = element
    const add = document.getElementById('addMe')
    add.append(h1)
});

const loadData = async()=>{
    try{
        const res = await fetch("https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772")
        const data = await res.json()
        console.log(data);
    }
    catch(e){
        console.error(e);
    }
}


loadData()