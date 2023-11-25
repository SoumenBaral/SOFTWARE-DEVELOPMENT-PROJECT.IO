function inputValue(){
   let inputVal =  document.getElementById("inputField")
   let paseVal = parseInt(inputVal.value)
   inputVal.value = '';
   return paseVal

}

function depositBtn(){
    let inputVal = inputValue()
    const DepositTxt = document.getElementById("Deposit")
    let Deposit = parseInt(DepositTxt.innerText)
    console.log(Deposit);
    if(inputVal>0){
        Deposit += inputVal
        DepositTxt.innerText = Deposit
    }
    else{
        alert("Give a Valid amount")
    }

    const BalanceTxt = document.getElementById("Balance");
    let Balance = parseInt(BalanceTxt.innerText)
    if(inputVal>0){
        Balance += inputVal
        BalanceTxt.innerText = Balance
    }
}

function withdrawBTN(){
    let inputVal = inputValue()
    console.log(inputVal);

}