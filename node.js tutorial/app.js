const EventEmmitter = require("events");
const eventEmmiter = new EventEmmitter();

const readline = require("readline");
const rl = readline.createInterface({input : process.stdin, output : process.stdout});

eventEmmiter.on("tutorial", (num1,num2)=>{
    console.log(num1 + num2);
    console.log("tutorial event has occurred");
});

eventEmmiter.emit("tutorial", 1, 2);

class Person extends EventEmmitter{
    constructor(name){
        super();
        this._name = name;
    
    }

    get name(){
        return this._name;
    }
}

let pedro = new Person("Pedro");
pedro.on("name", () =>{
    console.log("my name is " + pedro.name)
});

pedro.emit("name");


const tutorial = require("./tutorial");
console.log(tutorial.sum(1,1));
console.log(tutorial.PI);
console.log(new tutorial.SomeMathObject());
//console.log(tutorial(1,1));