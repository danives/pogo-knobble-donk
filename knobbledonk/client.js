//---------------------------------
//  Variables
//---------------------------------
var socket = new WebSocket(API_Socket);

//---------------------------------
//  Open Event
//---------------------------------
socket.onopen = function()
{
    // Format your Authentication Information
    var auth = {
        author: "Dan",
        website: "https://thedanives.com",
        api_key: API_Key,
        events: [
            "EVENT_DK_VOTES",
        ]
    }
    
    //  Send your Data to the server
    socket.send(JSON.stringify(auth));
};

//---------------------------------
//  Error Event
//---------------------------------
socket.onerror = function(error)
{
    //  Something went terribly wrong... Respond?!
    console.log("Error: " + error);
}

//---------------------------------
//  Message Event
//---------------------------------
socket.onmessage = function (message) 
{
    //  You have received new data now process it
    console.log(message.data);

    if (message.data) {
        var data = JSON.parse(message.data);
        if (data.event == 'EVENT_DK_VOTES') {
            var votes = JSON.parse(data.data);
            document.getElementById('donks').innerHTML = votes.donks;
            document.getElementById('knobbles').innerHTML = votes.knobbles;
        }
    }
}

//---------------------------------
//  Close Event
//---------------------------------
socket.onclose = function () 
{
    //  Connection has been closed by you or the server
    console.log("Connection Closed!");
}