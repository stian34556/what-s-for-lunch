
let id;

firebase.auth().onAuthStateChanged((user)=> {  
    if (!user) {
        location.replace("login.html")
    } else {
        const FoodRef = firebase
        .firestore()
        .collection("users")
        .doc(user.uid);

        id = user.uid;

        FoodRef.get().then((doc) => {
        if (!doc.exists) return;

        json_to_html_tag.innerHTML =  "<h3>Past Restaurants </h3><br> ";
        var li = document.createElement("li");
        var ul = document.getElementById("json_to_html_tag");

        var count = 0;

        for (var key of Object.keys(doc.data())) {
            for (var test of doc.data()[key]) {


                if (test.includes("add_to_fav(1)")) {
                    test = test.replace("add_to_fav(1)", "add_to_fav(" + count + ")");
                } else if (test.includes("add_to_fav(2)")) {
                    test = test.replace("add_to_fav(2)", "add_to_fav(" + count + ")");
                } else if (test.includes("add_to_fav(3)")) {
                    test = test.replace("add_to_fav(3)", "add_to_fav(" + count + ")");
                }

                
                test = test.replace(">Save<", ">delete<");
                json_to_html_tag.innerHTML += "<li class=list-group-item>" + test + "</li>";
                 
                count++;
            }

        }

        });

        document.getElementById("user").innerHTML = "Hello, " + user.email
    }
})


function logout(){
    firebase.auth().signOut()
}

function add_to_fav(num){
    
    var count = 0;

    const FoodRef = firebase
        .firestore()
        .collection("users")
        .doc(id)

    FoodRef.get().then((doc) => {

        var count = 0;
        var title;

        for (var key of Object.keys(doc.data())) {
            for (var test of doc.data()[key]) {

                if(count == num) {
                    title = test;
                    break;
                }

                count++;
            }
        }

        const FoodRef2 = firebase.firestore().collection("users").doc(id)  
        .update({
            Restaurant : firebase.firestore.FieldValue.arrayRemove(title),
        })
        .then((ref) => {
            location.replace("welcome.html")
           
        });
    });   
}

