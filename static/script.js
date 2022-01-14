

const opencomments = (id) =>{
    const comments = document.querySelector("#post-comment"+id);
    comments.classList.toggle("open");
}

const like =(id) => {
    $.ajax(
        {
            type:"GET",
            url:"like-post/id:"+id,
            success:function(data){
                let likescount = document.getElementById("likes-count"+id);
                let icon = document.getElementById("like-dislike"+id);
                if(data.liked == true){
                    likescount.innerText = Number(likescount.innerText)+1;
                    icon.src ="/static/dislike-icon.png";
                    console.log("liked");
                }
                else{
                    likescount.innerText = Number(likescount.innerText)-1;
                    icon.src ="/static/like-icon.png";
                    console.log("disliked");
                }
            }
        }
    );
}


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
function selectImage(){
    let s = document.querySelector(".selectimage");
    s.click();
}

// var lk = document.getElementById("any");
// lk.addEventListener("click",like);

// function like(){
//     let href = $('#any').attr('data-url');
//     console.log(href);
//     const xhttp = new XMLHttpRequest();
//     xhttp.onload  = function(){
//         let res = xhttp.response;
//         const obj = JSON.parse(res);
//         if(obj.liked == true){
//             console.log("liked");
//             $('#likes-count').html(" {{user.username}} ");

//         }
//         else{
//             console.log("disliked");
//         }
//     }
//     xhttp.open("GET",href);
//     xhttp.send();
// }

