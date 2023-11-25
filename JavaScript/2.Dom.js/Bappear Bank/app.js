function inputValue(){
   let inputVal =  document.getElementById("inputField")
   let paseVal = parseInt(inputVal.value)
   inputVal.value = '';
   return paseVal

}

function depositBtn(){
    let inputVal = inputValue()
    console.log(inputVal);
}

function withdrawBTN(){
    let inputVal = inputValue()
    console.log(inputVal);
}