import axios from 'axios';

function executeRequest(method, endpoint, payload, successCallback, errorCallback){
    const TIMEOUT = 1000;
    var headers = {
        'Content-Type': 'application/json',
    }
    
    axios({
        method: method,
        url: endpoint,
        data: payload,
        headers: headers,
        timeout: TIMEOUT
      }).then(response=> {
        let status = response.status;
        let data = response.data;
        if(successCallback !== undefined)
            successCallback(data, status);

      }).catch(err=>{

        if(err.response){
            let status = err.response.status;
            console.debug("HTTP ERROR", status, endpoint)
        }
       
        if(errorCallback !== undefined)
            errorCallback(err);
      })
}

export function Get(endpoint, successCallback, errorCallback)
{
    executeRequest("get", endpoint, {}, successCallback, errorCallback);
}

export function Post(endpoint, payload, successCallback, errorCallback)
{
    executeRequest("post", endpoint, payload, successCallback, errorCallback);
}

export function Update(endpoint, payload, successCallback, errorCallback)
{
    executeRequest("put", endpoint, payload, successCallback, errorCallback);
}

export function Delete(endpoint, successCallback, errorCallback)
{
    executeRequest("delete", endpoint, {}, successCallback, errorCallback);
}