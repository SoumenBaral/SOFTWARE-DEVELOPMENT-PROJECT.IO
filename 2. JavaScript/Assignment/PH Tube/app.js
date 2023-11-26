

const getCat =()=>{
    fetch('https://openapi.programming-hero.com/api/videos/categories')
    .then(res => res.json())
    .then(data=>displayData(data.data))
}
const displayData = Categories=>{
    const CatCnT = document.getElementById("category") 
    Categories.forEach(cat => {
        const DIV = document.createElement('div');
        DIV.innerHTML = `
        <div class = "bg-black bg-opacity-25">
            <button id=${cat.category_id} class="btn  text-opacity-100 fw-medium" onclick="GetProducts('${cat.category_id}')">${cat.category}</button>
        </div>`
        CatCnT.appendChild(DIV);
    });
    
}
getCat()

let lastClickedButton = document.getElementById(1000);
const GetProducts=async(id)=>{
   
    if (lastClickedButton) {
        lastClickedButton.style.backgroundColor = ""; 
    }
    const clickedButton = document.getElementById(id);
    clickedButton.style.backgroundColor ="red";
   lastClickedButton = clickedButton;


   try {
    const Url = `https://openapi.programming-hero.com/api/videos/category/${id}`
        const response = await fetch(Url);
        const data = await response.json();
        if (!data.status) {
           Display404()
        }
        else{
            displayProducts(data.data);
            
        }
    } 
    catch(err){
            console.log(err);
        };

}

const displayProducts= products =>{

 function Converter(seconds) {
    const convert = new Date(seconds * 1000).toISOString().substr(11, 8);
    return convert;
}
   const displayContainer = document.getElementById("displayContainer")
   displayContainer.innerHTML = ''
   products && products.forEach(product => {
        const DIV = document.createElement('div');
        DIV.classList.add("col-md-6","col-lg-3","col-sm-12");
        DIV.innerHTML = `
        <div class=" mx-auto ">
            <div class="card h-100 " style="width: 17rem;">
                <img src="${product.thumbnail}" class="card-img-top" style="width: 100%; height: 250px; object-fit: cover;" alt="${product.title}">
                <div class="card-body">
                    <div class="d-flex">
                        <img src="${product.authors[0].profile_picture}" style="width: 80px; height: 80px; padding:10px;" class="rounded-circle" alt="${product.authors[0].profile_name}">
                        <div class="card-img-overlay ">
                        <div class="d-flex" >
                            <h5 class="card-title text-white bg-dark" style="display: inline; margin-right: 5px; align-self: flex-end;">${product.others.posted_date !== '' ? Converter(product.others.posted_date) : ''}</h5>
                        </div>
                        </div>
                        <div>
                        
                            <h5 class="card-title">${product.title.slice(0,13)}</h5>
                            <div class="d-flex">
                                <p class="card-text">${product.authors[0].profile_name.slice(0,10)}</p>
                                <p class=" px-3">${product.authors[0].verified ? '<i class="bi bi-patch-check-fill text-primary fw-bold"></i>' : ''}</p>
                            </div>
                            <p class="card-text">${product.others.views}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>`;

        displayContainer.appendChild(DIV)
   });


}


const Display404 =()=>{
        const container = document.getElementById('displayContainer')
        container.innerHTML = ''
        const  DIV = document.createElement("div")
        DIV.innerHTML =`
        <div class="d-flex align-items-center justify-content-center" style="height: 80vh;">
        <div class="mx-auto text-center" style="width: 10rem;">
            <img src="./IMG/Icon.png" class="card-img-top" alt="...">
            <div class="py-3">
                <h5 class="text-sm">Oops!! Sorry, There is no content here</h5>
            </div>
        </div>
    </div>
    `
    container.appendChild(DIV);
}


const Sort = async() =>{
   try{
   const url ="https://openapi.programming-hero.com/api/videos/category/1000"
   const res = await fetch(url)
   const data = await res.json();
   
   const Convert = data.data.map(val=>{
            const views = parseFloat(val.others.views.replace('k', '')) *1000 ;
            return { ...val, others: { ...val.others, views } }
        })
   const ShortedVies = Convert.sort((a, b) => b.others.views - a.others.views);
   displayProducts(ShortedVies)
   }
   catch(er){
    console.error(er);
   }
   
}