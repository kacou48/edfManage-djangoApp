let menu = document.querySelector('#menu-btn');
let close = document.querySelector('#close-btn');
let navbar = document.querySelector('.navbar');


window.addEventListener('scroll', function(){
	var header = document.querySelector('.header');
	header.classList.toggle('stiky', window.scrollY > 0);
});

menu.onclick = () =>{
    menu.classList.toggle('hiddenP');
    close.classList.toggle('visibleP');
    navbar.classList.toggle('active-navbar');

}
close.onclick = () =>{
    menu.classList.toggle('hiddenP');
    close.classList.toggle('visibleP');
    navbar.classList.toggle('active-navbar');

}



//api contact
var formC = document.getElementById("formC")

csrftoken = formC.getElementsByTagName('input')[0].value

document.getElementById('contactNous').addEventListener('click', function(e){
    submitFormDataP()
    console.log('it work!!')
})

function submitFormDataP(){
    console.log("nous contacter")

    var contactFormDataP = {
        'nom':null,
        'prenom':null,
        'email':null,
        'phone':null,
        'message':null,
    }

    contactFormDataP.nom = formC.nom.value
    contactFormDataP.prenom = formC.prenom.value
    contactFormDataP.email = formC.email.value
    contactFormDataP.phone = formC.phone.value
    contactFormDataP.message = formC.message.value


    var url = '/envoie-de-message/'
    fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
    },
        body:JSON.stringify({'form':contactFormDataP}),
   })
   .then((response) => response.json())
   .then((data) => {
    console.log('Success:', data);

    //window.location.href = "/"
   })   
}  




let  butt = document.querySelector(".tab");

document.getElementById('close').addEventListener('click', function(e){
    butt.classList.add("hiddenMess")
})



/*
window.onscroll = () =>{
    menu.classList.remove('hiddenP');
    close.classList.remove('visibleP');
    navbar.classList.toggle('active-navbar');

}*/

