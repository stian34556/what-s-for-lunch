function add_to_fav(location, rate, price){
    // add to db
    const FoodRef = firebase
    .firestore()
    .collection("users")
    .doc(user.uid)
    .add({
        location: rate,
      })
    .then((ref) => {
        console.log("Added doc with ID: ", ref.id);
    });
}