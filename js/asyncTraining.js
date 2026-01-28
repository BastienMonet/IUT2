console.log("test");

function loadScript(src, callback) {
  // crée une balise <script> et l'ajoute à la page
  // ceci fait que le script avec la src donnée commence à se charger et s'exécute une fois terminé.
  let script = document.createElement('script');
  script.src = src;
  

  script.onload = () => callback();
  // onload est asynchrone

  document.head.append(script);
}

loadScript('/my/script.js', () => {
    myFunction();
}); // le script a "function myFunction()" il faut que cette fonction soit synchrone




function createPromiseMathRandom(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
             let m = Math.random() 
            m > 0.5 ? resolve(m) : reject(m);
        }, 5000);
    });
}

for (let i = 0; i < 6; i++) {
    setTimeout(() => {
    console.log(`${i} secondes se sont écoulées`);
}, i * 1000);
}


const promise = createPromiseMathRandom();

promise.then(
    (result) => console.log("Success:", result),
    (error) => console.log("Error:", error)
)

function asyncLoadScript(src, i){
    const promise = new Promise((resolve, reject) => {
        let script = document.createElement('script');
        script.src = src;
        document.head.append(script);
        script.onload = () => { 
            const fn = window[`myFunction${i}`]; 
            if (typeof fn === 'function') {
                fn();
                resolve('oui');
            } else {
                reject('aieaieaie')
            }
            
        }; 
        }
        ); 
    return promise;
}


async function loadFile(srcs) {
    for (let i in srcs) {
        const promise = asyncLoadScript(srcs[i], Number(i)+1)
        const result = await promise;
    }
}


loadFile(['/my/1.js', '/my/2.js', '/my/3.js']);
    
        
async function fetchUrl() {

    const name =  prompt("Entrez un nom d'utilisateur:");
    const url = `https://jsonplaceholder.typicode.com/users?username=${name}`
    const promise2leretour = fetch(url);
    const response = await promise2leretour;
    if (response.ok) {
        const data = await response.json();
        console.log(data)
    } else {
        console.log(response.status);
    }
    
}

fetchUrl();








