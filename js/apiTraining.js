

const list = []

const allelem = document.body.querySelectorAll('*');
allelem.forEach(elem => {
    list.push(elem);
});

console.log(list);

const apibutton = document.body.querySelector('#api')
console.log(apibutton)

let users = [
            {
                id: 1,
                username: 'username1',
                access: ['api', 'bo'],
            },
            {
                id: 2,
                username: 'username1',
                access: ['api', 'bo'],
            }
        ];

function showUser(users) {
    for (let user of users) {
        const h1 = document.createElement('h1');
        const p = document.createElement('p');
        h1.textContent = "j existe"
        p.textContent = "moi aussi"
        h1.id = user.username;
        for (let accss of user['access']) {
            p.classList.add(accss);
        }
        document.body.appendChild(h1);
        document.body.appendChild(p);
    }
}

showUser(users);

apibutton.insertAdjacentElement('afterend', document.createElement('hr'));

const specialp = document.createElement('h1');
specialp.textContent = "clickme"
specialp.style.cursor = "pointer"
document.body.appendChild(specialp);
specialp.onclick = function() {
    this.classList.toggle('data-clicked');
    if (this.classList.contains('data-clicked')) {
        this.style.color = "red";
    } else {
        this.style.color = "black";
    }
   
}