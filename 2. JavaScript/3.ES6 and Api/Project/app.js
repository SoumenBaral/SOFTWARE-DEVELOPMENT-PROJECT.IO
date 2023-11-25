const getData=()=>{
    const inputMeal = document.getElementById("findMeal")
    const inpVal = inputMeal.value
    inputMeal.value =""
    return inpVal
}



const loadData=async()=>{
    const Search = getData();
    const Meal =[]
    const url = `https://www.themealdb.com/api/json/v1/1/search.php?s=${Search}`
     fetch(url)
    .then (res => res.json())
    .then (data =>displayData(data.meals))

}
const displayData = meals =>{
 console.log(meals);
    const MealContainer = document.getElementById('Container')
    const DIV = document.createElement("div")
    DIV.classList.add('w-[400px]','border', 'border-red-200', 'text-center', 'shadow-lg')
    DIV.innerHTML =`<img src="https://www.themealdb.com/images/media/meals/g046bb1663960946.jpg" alt="food" class="w-full h-[250px] p-3">
    <h1>name</h1>
    <p class="">Description:</p>
    <button class="btn px-4 bg-gray-600 hover:bg-gray-400 text-white m-4 py-2 rounded-md">Details</button>`

    MealContainer.appendChild(DIV)
}
const handleMeal=()=>{
   loadData()
}