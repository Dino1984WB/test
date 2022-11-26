//home page js

//grab name from input in home.html
let inputString = document.getElementById("namePerson").innerHTML;

//function triggered by html button
async function fetchName () {
  
  let response = await fetch('http://127.0.0.1:8000', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
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
  
  
  console.log(inputString); //prints empty string :(

}


//found the culprit!!!!!! is reading the first line in home.html
//and determining it is not valid json for some reason
