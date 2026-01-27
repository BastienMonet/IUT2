let button = document.querySelector('button');
button.addEventListener('click', function(e){
    let paragraphe = document.querySelector('p');
    paragraphe.classList.toggle("design")
    
});

const exolist = document.querySelector('#list');
exolist.addEventListener('click', function(e){
    import('./listTraining.js');
    
});

const exoobj = document.querySelector('#obj');
exoobj.addEventListener('click', function(e){
    import('./objectTraining.js');
    
});

const tpobj = document.querySelector('#tpobj');
tpobj.addEventListener('click', function(e){
    import('./tpObject.js');
    
});


// output single object
const someObject = { str: "Some text", id: 5 };
console.log(someObject);

// Output multiple object
const car = "Dodge Charger";
const anotherObject = { str: "Some text", id: 5 };
console.info("My first car was a", car, ". The object is:", anotherObject);

// iterator / substition
for (let i = 0; i < 5; i++) {
  console.log("Hello, %s. You've called me %d times.", "Bob", i + 1);
}

console.log(typeof function(){} == "function")

// Stack trace
function foo() {
  function bar() {
      console.trace();
  }
  bar();
}
foo();



