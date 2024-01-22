

// Sticky Navbar Js
const header = document.querySelector('header');
window.addEventListener("scroll", function () {
    if (document.documentElement.scrollTop > 70) {
        header.classList.add("sticky");
    }
    else {
        header.classList.remove("sticky");
    }
})
// Sticky Navbar Js


//FAQ JAVASCRIPT
const items = document.querySelectorAll(".accordion-btn");
function toggleAccordion() {
  const itemToggle = this.getAttribute('aria-expanded');

  for (i = 0; i < items.length; i++) {
    items[i].setAttribute('aria-expanded', 'false');
  }

  if (itemToggle == 'false') {
    this.setAttribute('aria-expanded', 'true');
  }
}
items.forEach(item => item.addEventListener('click', toggleAccordion));

// FAQ JAVASCRIPT

// UP BUTTON JAVASCRIPT
// Get the button
let mybutton = document.getElementById("myUpButton");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 60 || document.documentElement.scrollTop > 60) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;

}
//Go back to top JS  End here
// UP BUTTON JAVASCRIPT

//logın Signin modal START HERE JS
// Get the modal
var modal = document.getElementById('id01');


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
//logın Signin modal  END JS



//Navbar User After login Arrow */
function userSettings() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
              openDropdown.classList.remove('show');
          }
      }

  }
}
//Navbar User After login Arrow */

//Prıcıng Modal Start Here

var modal = document.getElementById('pricing-modal');
var pricingButton = document.getElementById('priceOpenModal');
var closeModal = document.getElementById('close-pricing-modal');

var basic = document.getElementById('pricing-modal-basic');
var priceOpenModalbasic = document.getElementById('priceOpenModalbasic')
var closeModalbasic = document.getElementById('close-pricing-modal-basic');

var premium = document.getElementById('pricing-modal-premium');
var priceOpenModalpremium = document.getElementById('priceOpenModalpremium')
var closeModalpremium = document.getElementById('close-pricing-modal-premium');



pricingButton.onclick = function(){
    modal.style.display = "block";
}
closeModal.onclick = function() {
    modal.style.display = "none";
}
window.onclick = function(event){
    if(event.target == modal){
        modal.style.display = "none";

    }else if(event.target == basic){
        basic.style.display = "none";
    }else if(event.target == premium){
        premium.style.display = "none";
    }
}
//Prıcıng Modal End Here

priceOpenModalpremium.onclick = function(){
    premium.style.display = "block";
}
closeModalpremium.onclick = function() {
    premium.style.display = "none";
}

priceOpenModalbasic.onclick = function(){
    basic.style.display = "block";
}
closeModalbasic.onclick = function() {
    basic.style.display = "none";
}

const mainMenu = document.querySelector('.mainMenu');
const closeMenu = document.querySelector('.closeMenu');
const openMenu = document.querySelector('.openMenu');
const menu_items = document.querySelectorAll(' .mainMenu  li a');

openMenu.addEventListener('click',show);
closeMenu.addEventListener('click',close);

// close menu when you click on a menu item
menu_items.forEach(item => {
    item.addEventListener('click',function(){
        close();
    })
})

function show(){
    mainMenu.style.display = 'flex';
    mainMenu.style.top = '0';
}
function close(){
    mainMenu.style.top = '-100%';
}



function formsend(){
    alert("Contact Request Sent Successfully")
}

