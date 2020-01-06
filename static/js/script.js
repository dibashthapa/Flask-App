
$(document).ready(function () {
    var currentUser,message,textToAppend;
    var socket = io.connect("https://flaskstudentapp.herokuapp.com");
    var socket_messages = io.connect("https://flaskstudentapp.herokuapp.com/message")
    $('#sendbutton').on('click', function (data) {
        message = $('#myMessage').val();
        currentUser = $('#Name').val();

        socket_messages.emit('message from user', {
            messages: message,
            names: currentUser
        });

    });
    socket_messages.on('from flask', function (data) {
textToAppend = `<li id = "usermessage" ${currentUser == data['names'] ? 'style="background-color: #606770;list-style:none;height:20px;width:200px;margin-bottom:20px;margin:10px;color:white;position:relative;left:60%;" >' : '>' } ${data['names']} : ${data['messages']}`
$('#messages').append(textToAppend)
})
});
function follow(e){
    if (e.value=='follow'){
        e.value='following'

    }
    else{
        e.value='follow'
    }

}
