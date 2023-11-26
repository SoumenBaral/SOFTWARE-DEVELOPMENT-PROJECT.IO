console.log("I am from js");

const dom = document.getElementById("dom")
dom.style.background="blue"

document.getElementById("dom").style.removeProperty("background")


const inText = document.getElementById('NNN');

const inP = document.getElementById("para")

inP.innerText =inText.innerText 

function vanish(){
    console.log("is it the button is working ");
    inText.innerText =""
}