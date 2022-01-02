const db = firebase.firestore();

firebase.auth().onAuthStateChanged((user)=> {  
    if (!user) {
        location.replace("login.html")
    } else {
        const bookRef = firebase
        .firestore()
        .collection("users")
        .doc("test");

        bookRef.get().then((doc) => {
        if (!doc.exists) return;
        console.log("Document data:", doc.data());
        // Document data: { title: 'The Great Gatsby' }
        });


        document.getElementById("user").innerHTML = "Hello, " + user.email
    }
})


function logout(){
    firebase.auth().signOut()
}



