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

    const MealContainer = document.getElementById('Container') 
    MealContainer.innerHTML = ''
    meals&&meals.forEach(meal => {
        console.log(meal);
           const DIV = document.createElement("div")
           DIV.classList.add('w-[400px]','border', 'border-red-200', 'text-center', 'shadow-lg')
            DIV.innerHTML =`<img src=${meal.strMealThumb} alt="food" class="w-full h-[250px] p-3">
            <h1>Name : ${meal.strMeal}</h1>
            <p class="truncate p-3">Description: ${meal.strInstructions} </p>
            <button class="btn px-4 bg-gray-600 hover:bg-gray-400 text-white m-4 py-2 rounded-md">Details</button>`
            MealContainer.appendChild(DIV)
    });
    
    
    
    
}
const handleMeal=()=>{
   loadData()
}