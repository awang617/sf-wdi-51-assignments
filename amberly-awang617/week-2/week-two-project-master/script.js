// Global variables

// Buttons for the page
let buttons = document.querySelectorAll(".categories button");
let clearCart = document.querySelector("#clearCart");

// Empty image tags from HTML
let emptyImages = document.querySelectorAll(".pictures img");

// Image sources for the items
let teaImages = ["images/tea/lavender-tea.jpg", "images/tea/black-tea.jpg", "images/tea/green-tea.jpg", "images/tea/white-tea.jpg", "images/tea/blue-tea.jpg", "images/tea/herbal-tea.jpg"];
let floweringTeaImages = ["images/flowering-tea/jasmine-lotus.jpg","images/flowering-tea/blueberry.jpg", "images/flowering-tea/harmony.jpg", "images/flowering-tea/rising-flower.jpg", "images/flowering-tea/lychee.jpg", "images/flowering-tea/milky.jpg"];
let teaSetImages = ["images/tea-set/vintage.jpg", "images/tea-set/black-magic.jpg", "images/tea-set/black-and-white.jpeg", "images/tea-set/blue-porcelain.jpg", "images/tea-set/butterfly-set.jpg", "images/tea-set/flamingo-set.jpg"];

// Names for the items
let teaNames = ["Lavender Tea", "Black Tea", "Green Tea", "White Tea", "Blue Tea", "Herbal Tea"];
let floweringTeaNames = ["Jasmine Lotus Flowering Tea", "Blueberry Flowering Tea", "Harmony Flowering Tea", "Rising Flower Flowering Tea", "Lychee Flowering Tea", "Milky Flowering Tea"];
let teaSetNames = ["Vintage Blue Rose Tea Set","Black Magic Tea Set", "Black and White Tea Set", "Blue Porcelain Tea Set", "Butterfly Tea Set", "Flamingo Tea Set"];

// Prices


// Empty p tags and ul tag to fill in with image names
let itemNames = document.querySelectorAll(".pictures button")
let cartList = document.querySelector(".shoppingList");

// Image sources and names for cart arrays for reassignment
let imageSources = [];
let namesForCart = [];

// Make images appear. Takes the button id and matches it to corresponding array of image sources
let appear = function() {
  for (var i=0; i<emptyImages.length; i++) {
    emptyImages[i].addEventListener('click', showName);
    itemNames[i].addEventListener('click', showName);
    if (this.getAttribute('id') === "tea") {
      emptyImages[i].src = teaImages[i];
      itemNames[i].innerText = teaNames[i];
      imageSources = teaImages;
      namesForCart = teaNames;
    } else if (this.getAttribute('id') === "floweringTea") {
      emptyImages[i].src = floweringTeaImages[i];
      itemNames[i].innerText = floweringTeaNames[i];
      imageSources = floweringTeaImages
      namesForCart = floweringTeaNames
    } else if (this.getAttribute('id') === "teaSets") {
      emptyImages[i].src = teaSetImages[i];
      itemNames[i].innerText = teaSetNames[i];
      imageSources = teaSetImages;
      namesForCart = teaSetNames;
    };
  };
  document.querySelector(".pictures").style.display = "flex";
};

// Adds a list item to the shopping list
let showName = function() {
  var newListItem = document.createElement('li');
  for (var i=0; i < imageSources.length; i++) {
    if (this.getAttribute('src') === imageSources[i] || this.innerText === namesForCart[i]) {
    newListItem.innerHTML = namesForCart[i];
    };
  }
  cartList.appendChild(newListItem);
}

// Clear the shopping list
let clearShoppingCart = function() {
  cartList.innerHTML = "";
}

for (var i=0; i< buttons.length; i++) {
  buttons[i].addEventListener('click', appear);
}

clearCart.addEventListener('click', clearShoppingCart);
