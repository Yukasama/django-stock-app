
//Event Handler => Takes charge of adding and removing classes to and from elements
function eventHandler(eventElement, showElement, event="mouseover", action="show") {
    eventElement.addEventListener(event, () => {

        if (event == "mouseover" && showElement == 0) {
            eventElement.classList.add("show"); 
        }
        else if (event == "mouseleave" && showElement == 0) {
            eventElement.classList.remove("show"); 
        }
        else if (event == "click" && action == "remove") {
            showElement.classList.remove("show");
        }
        else if (action == "hide") {
            showElement.classList.remove("show");
        }
        else if (action == "window") {
            showElement.classList.toggle("scroll");
            eventElement.classList.toggle("scroll");
        }
        else if (event == "click" || event == "mouseover") {
            showElement.classList.toggle("show");
        }
        else if (event == "scroll") {
            showElement.classList.toggle("scroll", window.scrollY > 50);
        }
    })
}


//loops through Elements to determine Active Element
function activeLooper(elements, loopType, views="") {

    if (loopType == "list") {
        elements.forEach(element => {
            element.addEventListener("click", () => {
                if(element.classList.contains("active")) {
                    element.classList.remove("active");
                } else { 
                    element.classList.add("active")
                }
            })
        })
    }

    else if (loopType == "navigation") {
        $(document).ready(function () {
            $(elements).click(function (){
              $(this).addClass("active").siblings().removeClass("active");
            });
        });               
    }

    else if (loopType == "navtabs") {
        elements.forEach(function(element, i) {
            element.addEventListener("click", () => {
                elements.forEach((element) => {
                    element.classList.remove("active");
                });
                views.forEach((view) => {
                    view.classList.remove("active");
                }); 
                elements[i].classList.add("active");
                views[i].classList.add("active");    
            })
        })
    }
}


function zero(eventElement) {
    if (eventElement.value.length == 0) {
        eventElement.classList.remove("show");
    } else {
        eventElement.classList.add("show");
    }
}


// //Changes Hamburger to X and Backc
// function hamburgerChange(hamburger) {
//     const line1 = document.querySelector('.hamburger1 :nth-child(1)');
//     const line2 = document.querySelector('.hamburger1 :nth-child(2)');
//     const line3 = document.querySelector('.hamburger1 :nth-child(3)');

//     line1.classList.toggle("hamburger_line_active1");
// }