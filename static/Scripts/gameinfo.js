// var socket = io.connect("http://localhost:8000/gameinfo");
//
// socket.on('connect', function(){
//   socket.emit('connected', {data: "Connection Received!"} );
// });
//
// socket.on('blah', function(data){
//   console.log(data['data']);
// });

var socket = io();
var Game

var connect = function(){
  socket.emit('connected', {data:user})
};
socket.on('connect', connect);

var retrieveGame = function(){
  Game = socket.emit('retrieve', {id: idnum});
}

$(document).ready(function(){
  $("#button").click(function(){
    console.log("hhi");
    socket.emit('clicked!!!', {data:"pls"});
  });
});

$("#testb").click(function(){
    $("#test").append($('<li>Hello</li>'));  
});
