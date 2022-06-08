
//Event Handler => Takes charge of adding and removing classes to and from elements
function eventHandler(eventElement, showElement, event="mouseover", action="show") {
    eventElement.addEventListener(event, () => {

        if (event == "click" || event == "mouseover") {
            showElement.classList.toggle("show");
        }
        if (event == "scroll") {
            showElement.classList.toggle("scroll", window.scrollY > 50);
        }

        if (action == "hide") {
            showElement.classList.remove("show");
        }
        if (action == "window") {
            showElement.classList.toggle("scroll");
            eventElement.classList.toggle("scroll");
        }
    })
}


//loops through Elements to determine Active Element
function activeLooper(elements, loopType) {

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
}


// //Changes Hamburger to X and Backc
// function hamburgerChange(hamburger) {
//     const line1 = document.querySelector('.hamburger1 :nth-child(1)');
//     const line2 = document.querySelector('.hamburger1 :nth-child(2)');
//     const line3 = document.querySelector('.hamburger1 :nth-child(3)');

//     line1.classList.toggle("hamburger_line_active1");
// }