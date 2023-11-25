function inputValue(){
   let inputVal =  document.getElementById("inputField")
   let paseVal = parseInt(inputVal.value)
   inputVal.value = '';
   return paseVal

}
function getId(id){
return document.getElementById(id)
}
function depositBtn(){
    let inputVal = inputValue()
    const DepositTxt = getId("Deposit")
    let Deposit = parseInt(DepositTxt.innerText)
    console.log(Deposit);
    if(inputVal>0){
        Deposit += inputVal
        DepositTxt.innerText = Deposit
    }
    else{
        alert("Give a Valid amount")
    }

    const BalanceTxt = getId("Balance");
    let Balance = parseInt(BalanceTxt.innerText)
    if(inputVal>0){
        Balance += inputVal
        BalanceTxt.innerText = Balance
    }
}

function withdrawBTN(){
    let inputVal = inputValue()
    const withdrawTxt = getId("withdraw")
    let withdraw = parseInt(withdrawTxt.innerText)

    const BalanceTxt = getId("Balance");
    let Balance = parseInt(BalanceTxt.innerText)

    if(inputVal<Balance && inputVal>0){
        withdraw += inputVal
        withdrawTxt.innerText = withdraw
    }
    else{
        alert("Please Deposit first")
    }

    
    if(inputVal<Balance && inputVal>0){
        Balance -= inputVal
        BalanceTxt.innerText = Balance
    }

}