
alert("alerte au gogol");

console.log("hello world");


let tableauDesLangage = ["js", "CSS"]
tableauDesLangage.push("PHP");

const milieu = tableauDesLangage[+((tableauDesLangage.length - 1) / 2)];

console.log(milieu);

console.log(tableauDesLangage[0]);

tableauDesLangage.push("python");

let list = [];

let arg;

do {
    arg = prompt("ajouter a la liste");

    if (typeof Number(arg) === "number") {
        list.push(Number(arg));

        for (let key in list) {
        console.log("l'element " + key + " vaut " + list[key]);
        }
    }
} while (arg !== null);

let som = 0;
for (let arg of list) {
    som+=arg;
}
console.log(som);