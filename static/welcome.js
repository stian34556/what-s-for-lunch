firebase.auth().onAuthStateChanged((user)=> {  
    if (!user) {
        location.replace("login.html")
    } else {
        const FoodRef = firebase
        .firestore()
        .collection("users")
        .doc(user.uid);

        FoodRef.get().then((doc) => {
        if (!doc.exists) return;

        json_to_html_tag.innerHTML =  "Fav Restaurant <br><br>";

        for (var key of Object.keys(doc.data())) {
            console.log(key + " -> " + doc.data()[key])
            for (var test of doc.data()[key]) {
                json_to_html_tag.innerHTML += "Restaurant Name: " + test + "<br><br>";
            
            
            }

        }

        });


        document.getElementById("user").innerHTML = "Hello, " + user.email
    }
})


function logout(){
    firebase.auth().signOut()
}



