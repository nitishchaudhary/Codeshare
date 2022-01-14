
const user_name = document.getElementById("logged-in-user").value;
const other_user_name = document.querySelector('#receiver-user').value;

let loc = window.location
let wsStart = 'ws://'

if(loc.protocol === 'https'){
    wsStart = 'wss://'
}
let endpoint = wsStart + loc.host + loc.pathname
var socket = new WebSocket(endpoint)
console.log(user_name)
console.log(other_user_name)
socket.onopen = async function(e){
    console.log('open',e)
    $('#message-form').on('submit', function(e){
        e.preventDefault()
        let mes = $('#message').val();
        let data = {
            'message':mes,
            'sent_by':user_name,
            'sent_to':other_user_name,
            
        }
        data = JSON.stringify(data)
        socket.send(data)
        $(this)[0].reset()
        
    })
}
socket.onmessage = async function(e){
    console.log('message',e)    
    let data = JSON.parse(e.data)
    let message = data['message']
    let sent_by_user = data['sent_by']
    console.log(message)
    console.log(sent_by_user)
    if(sent_by_user == other_user_name){
        message_element = `
            <div class="show-received-message">
                <h4>${message}</h4>
            </div>
        `
    }
    if(sent_by_user == user_name){
        message_element = `
            <div class="show-sent-message">
                <h4>${message}</h4>
            </div>            
        `
    }
    else{
        message_element = `
            <div class="show-received-message">
                <h4>${message}</h4>
            </div>
        `       
    }
    let message_body = $('.messages-wrapper')
    message_body.append($(message_element))
    message_body.animate({
        scrollTop:$(document).height()
    },100)
}
socket.onerror = async function(e){
    console.log('error',e)
}
socket.onclose = async function(e){
    console.log('close',e)
}


