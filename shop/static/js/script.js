$(function () {
  $('[data-toggle="popover"]').popover();
});

// checking if cart is empty
if (localStorage.getItem("card") == null) {
  let cart = {};
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
}

// updating cart
$(document).on("click", ".add_to_cart", function () {
  console.log("Add to cart clicked");
  let item_id = this.id.toString();
  console.log(item_id);
  if (cart[1] != undefined) {
    cart[item_id] = cart[item_id] + 1;
  } else {
    cart[item_id] = 1;
  }
  console.log(cart);

  // saving
  localStorage.setItem("cart", JSON.stringify(cart));
  // alert("Added to cart");
  alert("Item added to cart");

  // to show added itemcount in navbar
  document.getElementById("cart").innerHTML =
    "Cart (" + Object.keys(cart).length + ")";
});
