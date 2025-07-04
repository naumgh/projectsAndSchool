package com.cooksys.quiz_api.services.impl;

import java.util.List;
import java.util.Optional;
import java.util.Random;

import org.springframework.data.crossstore.ChangeSetPersister.NotFoundException;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import com.cooksys.quiz_api.dtos.QuizResponseDto;
import com.cooksys.quiz_api.entities.Question;
import com.cooksys.quiz_api.entities.Quiz;
import com.cooksys.quiz_api.mappers.QuestionMapper;
import com.cooksys.quiz_api.mappers.QuizMapper;
import com.cooksys.quiz_api.services.QuizService;
import com.cooksys.quiz_api.dtos.QuestionRequestDto;
import com.cooksys.quiz_api.dtos.QuestionResponseDto;
import com.cooksys.quiz_api.dtos.QuizRequestDto;
import com.cooksys.quiz_api.repositories.QuestionRepository;
import com.cooksys.quiz_api.repositories.QuizRepository;
import com.cooksys.quiz_api.mappers.QuizMapper;



import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class QuizServiceImpl implements QuizService {

  private final QuizRepository quizRepository;
  private final QuizMapper quizMapper;
  private final QuestionRepository questionRepository;
  private final QuestionMapper questionMapper;

  
  
  private Quiz getQuiz(Long id) {
	  Optional<Quiz> optionalQuiz = quizRepository.findByIdAndDeletedFalse(id);
	  if(optionalQuiz.isEmpty()) {
		  throw new ResponseStatusException(HttpStatus.NOT_FOUND, "No quiz found with id: " + id);
	  }
	  return optionalQuiz.get();
  }

  @Override
  public List<QuizResponseDto> getAllQuizzes() {
    // Get all non-deleted quizzes from the repository.
    // Map the quizzes to DTOs and return them.
    return quizMapper.entitiesToDtos(quizRepository.findAllByDeletedFalse());
  }
  @Override
  public QuizResponseDto createQuiz(QuizRequestDto quizRequestDto) {
	  Quiz quizToSave = quizMapper.requestDtoToEntity(quizRequestDto);
	  return quizMapper.entityToDto(quizRepository.saveAndFlush(quizToSave));
  }
  @Override
  public QuizResponseDto deleteQuiz(Long id) {
	  Quiz quizToDelete = getQuiz(id);
	  quizToDelete.setDeleted(true);
	  return quizMapper.entityToDto(quizRepository.saveAndFlush(quizToDelete));
	  
  }
  
  @Override
  public QuizResponseDto renameQuizByName(String name, String newName) {
	  Optional<Quiz> optionalQuiz = quizRepository.findByNameAndDeletedFalse(name);
	  if (optionalQuiz.isEmpty()) {
		  throw new ResponseStatusException(HttpStatus.NOT_FOUND, "No quiz found with name: " + name);
	  }
	  
	  Quiz quiz = optionalQuiz.get();
	  quiz.setName(newName);
	  return quizMapper.entityToDto(quizRepository.saveAndFlush(quiz));
  }
  
  @Override
  public QuestionResponseDto getRandomQuestionByQuizName(String name) {
	  List<Question> questions = questionRepository.findAllByQuizNameAndDeletedFalse(name);
	  if(questions.isEmpty()) {
	        throw new ResponseStatusException(HttpStatus.NOT_FOUND, "No non-deleted questions found for quiz: " + name);
	  }
	  //I had to use the new keyword and im ashamed
	  Question random = questions.get(new Random().nextInt(questions.size()));
	  return questionMapper.entityToDto(random);
  }

  @Override
  public QuizResponseDto getQuizById(Long id) {
	  return quizMapper.entityToDto(getQuiz(id));
  }
  
  @Override
  public QuizResponseDto addQuestionToQuiz(String name, QuestionRequestDto questionRequestDto) {
	  Optional<Quiz> optionalQuiz = quizRepository.findByNameAndDeletedFalse(name);
	  if(optionalQuiz.isEmpty()) {
		  throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Quiz does not eqist, cannot add a question: " + name); 
	  }
	  Quiz quiz = optionalQuiz.get();
	  Question question = questionMapper.requestDtoToEntity(questionRequestDto);
	  question.setQuiz(quiz);
	  quiz.getQuestions().add(question);
	  
	  //return quizMapper.entityToDto(quizRepository.saveAndFlush(quiz));
	  questionRepository.saveAndFlush(question);
	  
	 return quizMapper.entityToDto(quiz);
	  
  }
  
  
  @Override
  public QuestionResponseDto deleteQuestionFromQuiz(String name, Long questionId) {
	  Optional<Quiz> optionalQuiz = quizRepository.findByNameAndDeletedFalse(name);
	  if(optionalQuiz.isEmpty()) {
		  throw new ResponseStatusException(HttpStatus.NOT_FOUND, "quiz not found:  " + name); 
	  }
	  Quiz quiz = optionalQuiz.get();
	  
	  Optional<Question> optionalQuestion = questionRepository.findById(questionId);
	  if (optionalQuestion.isEmpty()) {
	      throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Question not found: ID " + questionId);
	  }
	  Question question = optionalQuestion.get();
	  if(question.isDeleted() || !question.getQuiz().equals(quiz)) {
		  throw new ResponseStatusException(HttpStatus.NOT_FOUND, "question is already deleted in, or doesnt exist in: " + name);
	  }
	  
	  //return quizMapper.entityToDto(quizRepository.saveAndFlush(quiz));
	  question.setDeleted(true);
	  questionRepository.saveAndFlush(question);
	  return questionMapper.entityToDto(question);
	  
  }
  

}
