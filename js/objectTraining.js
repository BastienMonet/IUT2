let user = {
    username: 'Bastien',
    access: ['user', 'edito'],
    isAdmin: false,
    profil: function() {
        console.log(`Username is ${this.username} and acces are ${this.access}.`);
    },
    hasAccessOf: (str) => {
        for (let a of user.access) {
            if (a === str) {
                return true;
            }
        }
        return false;
    }

}

console.log(Object.getPrototypeOf(user));
console.log(user.hasAccessOf('user'));

console.log(typeof user);
console.log(user.profil());

function User(name, nickname) {
    this.name = name;
    this.nickname = nickname;
    this.getNom = function() {
        return this.name;
    }
}

let object = new User('parameter1', 'parameter2');


let person = {
    whoIs() {
        return `${this.firstname} ${this.lastname}`;
    }
}

let employee = {
    __proto__: person,
    firstname: 'employee',
    lastname: 'employee'
}

console.log(employee.whoIs());



class User2 {
    name = '';
    #nickname = '';
    
    constructor(name, nickname) {
        this.name = name;
        this.nickname = nickname;
    }

    get nom() {
        return this.name;
    }

    set nom(name) {
        this.name = name;
    }
}

let user1 = new User2('name1', 'nick1');
console.log(user1.nom);
user1.nom = 'name2';
console.log(user1.nom);