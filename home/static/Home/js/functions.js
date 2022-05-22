
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
            eventElement.classList.toggle("scroll");
            showElement.classList.toggle("scroll");
            document.body.classList.toggle("scroll");
        }
    })
}


//loops through Elements to determine Active Element
function activeLooper(elements) {
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
