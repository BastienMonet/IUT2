let admin;
let name = "Geoffroy";
admin = name;

// alert(admin)

let name1 = "Ilya";
// alert( `hello ${1}` ); // hello 1
// alert( `hello ${"name"}` ); // hello name
// alert( `hello ${name}` ); // hello Gef
// let age = prompt('How old are you?', '');
// console.log(age)


function deFoo(num,exp) {
    return num ** exp;
}

console.log(deFoo(3,5));    

let doOof = (a,b) => a+b/b+a; 

console.log(doOof(2,3));