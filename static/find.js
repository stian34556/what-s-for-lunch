function add_to_fav(num, name){
    var user = firebase.auth().currentUser;
    if (user) {
        
        const usersRef = firebase.firestore().collection("users").doc(user.uid)

        usersRef.get()
        .then((docSnapshot) => {
            if (!docSnapshot.exists) {
                usersRef.set({ Restaurant : [] })
            } 
        });

        if (num == 1) {
            title = document.getElementById("one").innerHTML;
            const FoodRef = firebase.firestore().collection("users").doc(user.uid)  
            .update({
                Restaurant: firebase.firestore.FieldValue.arrayUnion(title),
            })
            .then((ref) => {
                
          });
        } else if (num == 2) {
            title = document.getElementById("two").innerHTML;
            const FoodRef = firebase.firestore().collection("users").doc(user.uid)
            .update({
                Restaurant: firebase.firestore.FieldValue.arrayUnion(title),
            })
            .then((ref) => {
                
          });
        } else {
            title = document.getElementById("three").innerHTML;
            const FoodRef = firebase.firestore().collection("users").doc(user.uid)
            .update({
                Restaurant: firebase.firestore.FieldValue.arrayUnion(title),
            })
            .then((ref) => {
              
          });
        }      
    }
}
