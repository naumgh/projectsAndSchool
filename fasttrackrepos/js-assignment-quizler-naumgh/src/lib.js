import fs from 'fs'

const randomIndex = (max) => Math.floor(Math.random() * max)

const chooseRandom = (randFn = randomIndex) => {
    // TODO implement the chooseRandom function.
    // This function should return a function with two parameters: array and numitems
    //array should defaulf to an empty array
    return (array =[], numItems) => {
        //if array of length 0 or 1, return a copy of the array (return array)
        if (array.length === 0 || array.length === 1) return [...array];
        //numitems should be a number, within range of arrays.length
        if (typeof numItems !== 'number' || numItems < 1 || numItems > array.length) {
            numItems = randFn(array.length) + 1; //DEFAULT to number between 1 and length of array
        }

        const res = [];
        const copy = [...array]; // Create a copy of the array to avoid modifying the original
        while(res.length < numItems && copy.length > 0){

         // While the result array has less than numItems and copy is not empty
            const index = randFn(copy.length); // Get a random index from the copy
            res.push(copy[index]); // Push the item at that index to the result array
            copy.splice(index, 1); // Remove the item from the copy to avoid duplicates
        
        }
        return res; // Return the result array containing the randomly chosen items

    }
    
}

const createPrompt = ({numQuestions = 1, numChoices = 2} = {}) => {

    // TODO implement the chooseRandom function.
    const promptArray = [];
    for (let i = 1; i <= numQuestions; i++) {
        const question = {
            type: 'input',
            name: `question-${i}`,
            message: `Enter question ${i}`
        };
        promptArray.push(question);
        for (let j = 1; j <= numChoices; j++) {
          const choice = {
            type: 'input',
            name: `question-${i}-choice-${j}`,
            message: `Enter answer choice ${j} for question ${i}`,
          }; 
          promptArray.push(choice);
        }
        
    }
    return promptArray;
}

const createQuestions = (input = {}) => {
    // TODO implement the chooseRandom function.
    const questions = [];
    Object.keys(input).forEach((key) => {
        if (key.startsWith('question-') && !key.includes('choice')) {
          const questionName = key;
          const questionText = input[key];
          const choices = [];
          Object.keys(input).forEach((choiceKey) => {
            if (choiceKey.startsWith(`${questionName}-choice-`)) {
              choices.push(input[choiceKey]);
            }
          });
          questions.push({
            type: 'list',
            name: questionName,
            message: questionText,
            choices: choices,
            
          })
        }
    });
    return questions;
}

const readFile = path =>
  new Promise((resolve, reject) => {
    fs.readFile(path, (err, data) => (err ? reject(err) : resolve(data)))
  })

const writeFile = (path, data) =>
  new Promise((resolve, reject) => {
    fs.writeFile(path, data, err =>
      err ? reject(err) : resolve('File saved successfully')
    )
  })

export { chooseRandom, createPrompt, createQuestions, readFile, writeFile }