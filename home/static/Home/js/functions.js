
//Event Handler => Takes charge of adding and removing classes to and from elements
function eventHandler(eventElement, showElement, event="mouseover", action="show") {
    eventElement.addEventListener(event, () => {

        if (event == "click" || event == "mouseover") {
            showElement.classList.toggle("show");
        }
        if (action == "hide") {
            showElement.classList.remove("show");
        }
    })
}