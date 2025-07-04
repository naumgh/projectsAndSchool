package com.cooksys.quiz_api.controllers;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
//import org.springframework.web.bind.annotation.DeleteMapping;


import com.cooksys.quiz_api.dtos.*;

import com.cooksys.quiz_api.services.QuizService;
import lombok.RequiredArgsConstructor;





@RestController
@RequiredArgsConstructor
@RequestMapping("/quiz")
public class QuizController {

  private final QuizService quizService;

  @GetMapping
  public List<QuizResponseDto> getAllQuizzes() {
    return quizService.getAllQuizzes();
  }
  
  @GetMapping("/{id}")
  public QuizResponseDto getQuizByID(@PathVariable Long id) {
	  return quizService.getQuizById(id);
  }
 
  @PatchMapping("/{name}/rename/{newName}")
  public QuizResponseDto renameQuiz(@PathVariable String name, @PathVariable String newName) {
	  return quizService.renameQuizByName(name,newName);
  }

  @GetMapping("/{name}/random")
  public QuestionResponseDto getRandomQuestionByQuizName(@PathVariable String name) {
      return quizService.getRandomQuestionByQuizName(name);
  }
  
  @PatchMapping("/{name}/add")
  public QuizResponseDto addQuestiontoQuiz(@PathVariable String name, @RequestBody QuestionRequestDto questionRequestDto) {
	  return quizService.addQuestionToQuiz(name, questionRequestDto);
  }
  
  
  @PostMapping
  public QuizResponseDto createQuiz(@RequestBody QuizRequestDto quizRequestDto) {
	  return quizService.createQuiz(quizRequestDto);
  }
  
  @DeleteMapping("/{name}/delete/{questionId}")
  public QuestionResponseDto deleteQuestionFromQuiz(
          @PathVariable String name,
          @PathVariable Long questionId) {
      return quizService.deleteQuestionFromQuiz(name, questionId);
  }
  
  @DeleteMapping("/{id}")
  public QuizResponseDto deleteQuiz(@PathVariable Long id) {
	  return quizService.deleteQuiz(id);
  }
  // TODO: Implement the remaining 6 endpoints from the documentation.

}
