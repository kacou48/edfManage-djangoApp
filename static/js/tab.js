let dashNav = document.querySelector('.dashNav');
let menuOpenBtn = document.querySelector(".fa-align-justify");


menuOpenBtn.onclick = () =>{
    //menuOpenBtn.classList.toggle('fa-times');
    //menuOpenBtn.classList.toggle('fa-align-justify');
    dashNav.classList.toggle('show');

}


//help script
const aideContent = document.querySelectorAll('.aideContent');

aideContent.forEach((item, index) => {
    let header = item.querySelector('.tete');
    header.addEventListener('click', () => {
        item.classList.toggle('open');

        let reponse = item.querySelector('.reponse');
        console.log(reponse)
        if(item.classList.contains("open")){
            reponse.style.height = `${reponse.scrollHeight}px`;

            item.querySelector('i').classList.replace("fa-plus", "fa-minus");
        }else{
            reponse.style.height = "0px";
            item.querySelector('i').classList.replace("fa-minus", "fa-plus");
        }

    })
    console.log(item)
})

