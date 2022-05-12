const button = document.querySelector("button.add-button");
const newPortfolioForm = document.querySelector(".form-container");
const mainContainer = document.querySelector(".content-container");
const cancelButton = document.querySelector(".cancel-button");


button.addEventListener('click', () => {
    console.log(newPortfolioForm);
    mainContainer.setAttribute("style", "opacity: 0.2");
    newPortfolioForm.setAttribute("style", "display: block");
});


cancelButton.addEventListener('click', () => { 
    mainContainer.setAttribute("style", "opacity: 1");
    newPortfolioForm.setAttribute("style", "display: none");
});
