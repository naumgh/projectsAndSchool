const sum = (num1,num2) => num1 + num2;
const PI = 3.14
class SomeMathObject{
    constructor(){
        console.log("objects created");
        }
}
module.exports = {sum : sum, PI : PI, SomeMathObject : SomeMathObject}


//module.exports.PI = PI;
//module.exports.SomeMathObject = SomeMathObject