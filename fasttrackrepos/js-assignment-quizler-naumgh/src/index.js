import vorpal from 'vorpal'
import pkg from 'inquirer'
import {
  readFile,
  writeFile,
  chooseRandom,
  createPrompt,
  createQuestions
} from './lib.js'

const { prompt } = pkg

const cli = vorpal()

const askForQuestions = [
  {
    type: 'input',
    name: 'numQuestions',
    message: 'How many questions do you want in your quiz?',
    validate: input => {
      const pass = input.match(/^[1-9]{1}$|^[1-9]{1}[0-9]{1}$|^100$/)
      return pass ? true : 'Please enter a valid number!'
    }
  },
  {
    type: 'input',
    name: 'numChoices',
    message: 'How many choices should each question have?',
    validate: input => {
      const pass = input.match(/^(?:[2-4]|0[2-4]|4)$/)
      return pass ? true : 'Please enter a valid number!'
    }
  }
]

const createQuiz = title =>
  prompt(askForQuestions)
    .then(answer => Object.keys(answer).reduce((acc, key) => ({ ...acc, [key]: parseInt(answer[key])}), {}))
    .then(promptObj => createPrompt(promptObj))
    .then(promptArray => prompt(promptArray))
    .then(answer => createQuestions(answer))
    .then(quiz => writeFile(title, JSON.stringify(quiz)))
    .then(() => console.log('Quiz created successfully.'))
    .catch(err => console.log('Error creating the quiz.', err))

const takeQuiz = (title, output) =>
  readFile(title)
    .then(quizData => JSON.parse(quizData))
    .then(quiz => prompt(quiz))
    .then(answers => writeFile(output, JSON.stringify(answers)))
    .catch(err => console.log('Error taking the quiz', err))

const takeRandomQuiz = (quizzes, output, n) =>
  Promise.all(quizzes.map(quizName => readFile(quizName)))
    .then(quizDataArray => quizDataArray.flatMap(quizData => JSON.parse(quizData)))
    .then(questions => chooseRandom()(questions, n))
    .then(randomQuestions => {
      console.log(randomQuestions)
      return prompt(randomQuestions)
    })
    .then(answer => writeFile(output, JSON.stringify(answer)))
    .then(() => console.log('Random quiz answers saved successfully.'))
    .catch(err => console.log('Error creating the random quiz.', err))

cli
  .command(
    'create <fileName>',
    'Creates a new quiz and saves it to the given <fileName>.json. Automatically adds the file extension.'
  )
  .action(function (input, callback) {
    return createQuiz(`${input.fileName}.json`)
  })

cli
  .command(
    'take <fileName> <outputFile>',
    'Loads a quiz and saves the users answers to the given outputFile. Automatically adds file extensions to both inputs.'
  )
  .action(function (input, callback) {
    return takeQuiz(`${input.fileName}.json`, `${input.outputFile}.json`)
  })

cli
  .command(
    'random <outputFile> <fileNames...>',
    'Loads a quiz or' +
    ' multiple quizes and selects a random number of questions from each quiz.' +
    ' Then, saves the users answers to the given outputFile' +
    ' Automatically adds file extensions.'
  )
  .action(function (input, callback) {
    return takeRandomQuiz(input.fileNames.map(fileName => `${fileName}.json`), `${input.outputFile}.json`, Math.floor(Math.random() * 5))
  })

cli.delimiter(cli.chalk['yellow']('quizler>')).show()
