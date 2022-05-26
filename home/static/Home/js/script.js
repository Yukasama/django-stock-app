

//STICKY NAVBAR
const navbar = document.querySelector(".navbar");
eventHandler(window, navbar, "scroll", "show");



//SIDEBAR
const sidebar = document.querySelector(".sidebar");
const hamburger1 = document.querySelector(".hamburger1");
eventHandler(hamburger1, sidebar, "click", "window");

const side_header = document.querySelectorAll(".side_header")
activeLooper(side_header);

//HAMBURGER

var search_input = document.querySelector(".search_input");
search_input.addEventListener("click", () => {
    if($(search_input).is(':focus')) {
        $(search_input).cla
    } 
})



//CONTACT
const contact_link = document.querySelector(".contact_link");
const contact = document.querySelector(".contact");
const hamburger2 = document.querySelector(".hamburger2");
eventHandler(contact_link, contact, "click", "show");
eventHandler(hamburger2, contact, "click", "hide");



// INPUT
const emailinputField = document.querySelector(".emailinputField");
const email_input = document.querySelector(".email_input");

// if (document.activeElement === email_input) {
//     emailinputField.classList.add("active");
// }








// //SEARCHBAR
// const searchbar = document.querySelector(".searchbar");
// const search_input = document.querySelector(".search_input")
// searchbar.addEventListener("mouseover", () => {
//     document.getElementsByName("search_input")[0].placeholder = "New";
// })






// Functions you might need down the road //

//ELEMENT SLIDING
/*
const slideOptions = {
    threshhold: 0,
    rootMargin: "0px 0px -300px 0px"
};
const your_element = document.querySelectorAll(".your_element");
const slideOnScroll = new IntersectionObserver(function(
    entries,
    slideOnScroll
) {
    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            return;
        }
        else {
            entry.target.classList.add("slide");
            slideOnScroll.unobserve(entry.target);
        }
    })

}, slideOptions);

//ENTER YOUR ELEMENT
your_element.forEach(element => {
    slideOnScroll.observe(element);
});


//VANILLA TILT SETTINGS
VanillaTilt.init(document.querySelectorAll(".your_element"), {
    max: 25,
    speed: 400,
    scale: 1.07,
});


//AUTOMATIC TEXT REPLACING FUNCTION
const writer = document.querySelector(".main_writer");
function writing() {
    setTimeout(() => {
        writer.innerHTML = "Elements";
    }, 0000);
    setTimeout(() => {
        writer.innerHTML = "Containers";
    }, 4000);   //Time when item gets replaced
    setTimeout(() => {
        writer.innerHTML = "Wrappers";
    }, 8000);
    setTimeout(() => {
        writer.innerHTML = "Vision";
    }, 12000);
}
setInterval(writing, 16000);
writing();


// DRAGABLE ELEMENTS
function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id + "header")) {
    // if present, the header is where you move the DIV from:
    document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
  } else {
    // otherwise, move the DIV from anywhere inside the DIV:
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
  }
}

//dragElement(document.querySelector(".settings"));


//BUTTON CLICK FOR WEBSITE SCROLL
const main_icon = document.querySelector(".main_wave_icon");
main_icon.onclick = function() {
    window.style.transform = translateY( + window.scrollY + 1000);
};
*/