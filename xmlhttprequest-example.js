var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

var oReq = new XMLHttpRequest();
var url = 'https://www.google.com/';
oReq.responseType = 'text';
oReq.onload = function (){
    if (oReq.readyState === oReq.DONE) {
        if (oReq.status === 200) {
            console.log(oReq.response);
            console.log(oReq.responseText);
        }
    }
};
oReq.open("get", url, true);
oReq.send(null);