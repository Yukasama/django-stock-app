//Loops through Elements to determine Active Element
function activeLooper(elements, loopType, views) {

  try {
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
  } catch {
      console.log(elements + " Element Error");
  }
}
