//home page js

//grab name from input in home.html
let inputString = document.getElementById('_name').innerHTML;

//function triggered by html button
async function fetchName () {
  
  let response = await fetch('http://127.0.0.1:8000', {
    method: 'POST',
    body: JSON.stringify(inputString)
  });


  //response is good or bad, ie connection good or bad  
  if (response.ok) {
    let json = response.json();
    console.log("Good Response:200" + json); 
  } else {
    alert("Reponse not ok" + response.status);
    console.log(response.status);
  }
    
}

console.log(JSON.stringify(inputString));