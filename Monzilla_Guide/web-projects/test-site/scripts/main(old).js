const myHeading = document.querySelector('h1');
myHeading.textContent = 'hello world!';

let myVariable; 
myVariable = "bob";
let myVariable2 = "bob";
myVariable = "steve";
/*
Everything imbetween here is a comment 
*/
//this is also a comment 
// === return true or false if strcitly equal 
let iceCream = "chocolate";
if (iceCream === "chocolate"){
    alert("Yay, I love chocolate ice cream !");
} else {
    alert("Awwww, but chocolate is my faviorate... ");
}

function multiply(num1,num2) {
    let result = num1 * num2;
    return result;
}

multiply(4,7)
multiply(20,20)
multiply(0.5,3)

document.querySelector("html").addEventListener("click",function() {
    alert("Ouch! Stop poking me!");
});

//this is equivalent to 

let myHTML =document.querySelector("html");
myHTML.addEventListener("click", function() {
    alert("Ouch! Stop poking me!");
});

//we can use arrow functions () => instead of function () 

document.querySelector("html").addEventListener("click", () => {
    alert("Ouch! stop poking me!");
});



