//home page js

//grab name from input
let name = document.getElementById("name")

async function fetchName () {
  
    console.log("button pressed for search") //test

    let response = await fetch('http://127.0.0.1:8000', {
      method: 'POST',
      body: JSON.stringify(name)
    });

    
    if (response.ok) {
      let json = response.json();
      console.log("Response:200"); 
    } else {
      alert("Reponse not ok" + response.status);
      console.log(response.status);
    }
     
}
