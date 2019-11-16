$(document).ready(function () {
    var currentUser,message,textToAppend;
    var socket = io.connect("127.0.0.1");
    var socket_messages = io.connect("127.0.0.1:5000/message")
    $('#sendbutton').on('click', function (data) {
        message = $('#myMessage').val();
        currentUser = $('#Name').val();

        socket_messages.emit('message from user', {
            messages: message,
            names: currentUser
        });

    });
    $('#myMessage').focus((data)=>{
    socket_messages.emit('typing',{
        messages:message,
        names:currentUser
    })
    })
    $('#myMessage').focusout(()=>{
        $('#typingMessages').remove()
    })

    socket_messages.on('from flask', function (data) {
textToAppend = `<li id = "usermessage" ${currentUser == data['names'] ? 'style="background-color: #606770;border-radius:10px;width:200px;margin-bottom:20px;margin:10px;color:white;position:relative;left:60%;" >' : '>' } ${data['names']} : ${data['messages']}`
$('#messages').append(textToAppend)
});
socket_messages.on('data typing',function(data){

$('#typingMessages').append("<li>"+data['names']+"is typing"+"</li>")
})
})