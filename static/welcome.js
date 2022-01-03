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

        json_to_html_tag.innerHTML =  "<h3>Past Restaurants </h3><br> ";
        var li = document.createElement("li");
        var ul = document.getElementById("json_to_html_tag");
        for (var key of Object.keys(doc.data())) {
            for (var test of doc.data()[key]) {
                json_to_html_tag.innerHTML += "<li class=list-group-item>" + test + "</li>";

                //json_to_html_tag.innerHTML += test + "<br><br>";
            }

        }

        });


        document.getElementById("user").innerHTML = "Hello, " + user.email
    }
})


function logout(){
    firebase.auth().signOut()
}



