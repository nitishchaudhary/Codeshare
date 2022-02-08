$("#image").click(function(e){
    let s = document.querySelector("#profile-image-upload");
    s.click();
})
const loadFile =()=>{
    var image = document.getElementById("image");
    image.src = URL.createObjectURL(event.target.files[0]);
}
let check=0;
const follow_user =(username)=>{
    $.ajax(
        {
            type:"GET",
            url:"/follow/user:"+username,
            data:{
                welcome:'true'
            },
            success:function(e){
                check++;
                if ($("#follow-user"+username).html() == "Follow"){
                    $("#follow-user"+username).html("Unfollow");
                }
                else{
                    $("#follow-user"+username).html("Follow");
                }
                if(check >=2){
                    $(".submit").css("display","unset");
                }
            }
        }
    )
    
}

