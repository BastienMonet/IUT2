

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
                username: 'username3',
                access: ['api', 'bo', 'bu', 'bi'],
            }
        ];

function findid(id){
    for (let user of users) {
        if (user['id'] === id) {
            return user;
        }
    }
}

function showUser(users) {
    for (let user of users) {
        const h1 = document.createElement('h1');
        const p = document.createElement('p');
        
        
        h1.id = user.username;
        h1.textContent = h1.id
        for (let accss of user['access']) {
            p.classList.add(accss);
        }
        p.textContent = p.classList.value;
        p.style.visibility = "hidden";
        document.body.appendChild(h1);
        document.body.appendChild(p);


        // show the access by 2 different ways
        h1.addEventListener('click', function(e) {
            // with visibility hidden
            e.target.nextSibling.style.visibility = "visible"; //shit
            
            // creating a new p with the correct access 
            const new_p = document.createElement('p'); // better, i guess
            new_p.textContent = findid(user.id).access;
            e.target.insertAdjacentHTML('afterend', new_p.textContent);
        })
    }
}

showUser(users);

apibutton.insertAdjacentElement('afterend', document.createElement('hr'));

const specialp = document.createElement('h1');
specialp.textContent = "clickme";
specialp.style.cursor = "pointer";
document.body.appendChild(specialp);
specialp.onclick = function() {
    this.classList.toggle('data-clicked');
    if (this.classList.contains('data-clicked')) {
        this.style.color = "red";
    } else {
        this.style.color = "black";
    }
   
}

