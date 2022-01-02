function add_to_fav(num){
    var user = firebase.auth().currentUser;
    if (user) {
        if (num == 1) {
            title = document.getElementById("one").innerHTML;
            const FoodRef = firebase.firestore().collection("users").doc(user.uid)
            .add({
                title: "",
            })
            .then((ref) => {
                console.log("Added doc with ID: ", ref.id);
          });
        } else if (num == 2) {
            title = document.getElementById("two").innerHTML;
            const FoodRef = firebase.firestore().collection("users").doc(user.uid)
            .add({
                title: "",
            })
            .then((ref) => {
                console.log("Added doc with ID: ", ref.id);
          });
        } else {
            title = document.getElementById("three").innerHTML;
            const FoodRef = firebase.firestore().collection("users").doc(user.uid)
            .add({
                title: "",
            })
            .then((ref) => {
                console.log("Added doc with ID: ", ref.id);
          });
        }      
    }
}
