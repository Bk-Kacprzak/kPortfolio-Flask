// const button = document.querySelector("button.add-button");
// const newPortfolioForm = document.querySelector(".form-container");
const mainContainer = document.querySelector(".content-container");
const cancelButton = document.querySelector(".cancel-button");

const showForm = (formToOpenClass, anotherFormClass = null) => { 
    if (anotherFormClass != null) { 
        anotherForm = document.querySelector(anotherFormClass);
        if (anotherForm.style.display == "block") 
            return;
    }
  
    form = document.querySelector(formToOpenClass) 
    mainContainer.setAttribute("style", "opacity: 0.2");
    form.setAttribute("style", "display: block");
}

const hideForm = (formClasses) => { 
    formClasses.forEach((value)=> { 
        form = document.querySelector(value) 
        form.setAttribute("style", "display: none");
    })
    // form = document.querySelector(formClass) 
    mainContainer.setAttribute("style", "opacity: 1");
}