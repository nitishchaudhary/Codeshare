//animatinng the navbar to hide when scroling down and
//to show when scroling up
// var prevScrollpos = window.pageYOffset;
// //var navbar = document.getElementById("navbar");
// window.onscroll = function(){
//     var currentScrollpos = window.pageYOffset;
//     if(prevScrollpos > currentScrollpos){
//         document.getElementById("nav").style.top = "0";
//     }
//     else{
//         document.getElementById("nav").style.top = "-50px";
//     }
//     prevScrollpos = currentScrollpos;
// }

var join = document.getElementById("join-community");
var form = document.getElementById("sign-up-form");
join.addEventListener("click" , ()=>{
    form.style.zIndex = "1";
    form.style.opacity = "1";
    document.getElementById("main-container").style.filter = "blur(8px)";
})

function Menu(){
    const navMenu = document.querySelector(".nav-menu");
    navMenu.classList.toggle("active");   
}
const navLinks = document.querySelectorAll(".nav-link");
navLinks.forEach(n => n.addEventListener("click" , closeMenu));
function closeMenu(){
    const navMenu = document.querySelector(".nav-menu");
    navMenu.classList.remove("active");
}
