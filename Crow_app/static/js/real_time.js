function getBMEData()
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "/real_time/get_status", false ); // false for synchronous request
    xmlHttp.send( null );
    
    return JSON.parse(xmlHttp.response);
}


function deploy(){
    const data = getBMEData()
    console.log(data)
    document.getElementById("temperature").innerText = data.temperature
    document.getElementById("humidity").innerText = data.humidity
    document.getElementById("pressure").innerText = data.pressure
}

setInterval(deploy, 2000);
getBMEData()