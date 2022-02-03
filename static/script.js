
const sent_requests =() =>{
    $.ajax(
        {
            type:"GET",
            url:"/collabs",
            data:{
                retrieve:"sent"
            },
            success:function(e){
                data = JSON.parse(e);
                // console.log(e);
                message = `
                    <nav class=collab-title>
                        <h4 onclick="received_requests()">Received</h4>
                        <h4 onclick="sent_requests()" class="active">Sent</h4>
                    </nav>
                    <section class="requests">
                        <div class="sent">
                            <div class="requested-user-details">
                            <img src="${data['profile-url']}" alt="">
                                <div class="requested-user-name">
                                    <h5>${data['requested_user']}</h5>
                                    <i>@${data['requested_user']}</i>
                                </div>
                            </div>
                            <div class="project-detail">
                                <h3>Project :</h3>
                                <h4>${data['project_title']}</h4>
                            </div>
                        </div>
                    </section>
                `
                $(".collab-container").html(message);
            }
        }
    )
}
const received_requests =() =>{
    $.ajax(
        {
            type:"GET",
            url:"/collabs",
            data:{
                retrieve:"received"
            },
            success:function(e){
                data = JSON.parse(e);
                // console.log(data);
                message = `
                <nav class=collab-title>
                    <h4 onclick="received_requests()" class="active">Received</h4>
                    <h4 onclick="sent_requests()">Sent</h4>
                </nav>
                    <section class="requests">
                        <div class="received">
                            <div class="requesting-user-details">
                            <img src="${data['profile-url']}" alt="">
                                <div class="requested-user-name">
                                    <h5>${data['requesting_user']}</h5>
                                    <i>@${data['requesting_user']}</i>
                                </div>
                            </div>
                            <div class="project-detail">
                                <h3>Project :</h3>
                                <h4>${data['project_title']}</h4>
                            </div>
                        </div>
                    </section>
                `
                $(".collab-container").html(message);
            
            }
        }
    )
}

const opencomments = (id) =>{
    const comments = document.querySelector("#post-comment"+id);
    comments.classList.toggle("open");
}
const share_project =() =>{
    let section = document.getElementById("share-project-container");
    document.getElementById("container").style.filter = "blur(8px)";
    section.style.display = "flex";
    section.style.zIndex = "1";

}
const close_window = () =>{
    let section = document.getElementById("share-project-container");
    document.getElementById("container").style.filter = "blur(0px)";
    section.style.display = "none";
    section.style.zIndex = "-1";
}


const like =(id) => {
    $.ajax(
        {
            type:"GET",
            url:"/like-post/id:"+id,
            success:function(data){
                let likescount = document.getElementById("likes-count"+id);
                let icon = document.getElementById("like-dislike"+id);
                if(data.liked == true){
                    likescount.innerText = Number(likescount.innerText)+1;
                    icon.src ="/static/liked-icon.png";
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

const hamburger=(id)=>{
    let options = document.getElementById('options'+id);
    options.classList.toggle("visible");
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

