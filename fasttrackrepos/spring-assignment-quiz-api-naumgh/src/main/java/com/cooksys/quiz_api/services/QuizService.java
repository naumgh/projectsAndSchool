package com.cooksys.quiz_api.services;


import java.util.List;

import com.cooksys.quiz_api.dtos.QuestionRequestDto;
import com.cooksys.quiz_api.dtos.QuestionResponseDto;
import com.cooksys.quiz_api.dtos.QuizRequestDto;
import com.cooksys.quiz_api.dtos.QuizResponseDto;


public interface QuizService {

  List<QuizResponseDto> getAllQuizzes();
  QuizResponseDto createQuiz(QuizRequestDto quizRequestDto);
  QuizResponseDto deleteQuiz(Long id);
  QuizResponseDto getQuizById(Long id);
  QuizResponseDto renameQuizByName(String name, String newName);
  QuestionResponseDto getRandomQuestionByQuizName(String name);
  QuizResponseDto addQuestionToQuiz(String name, QuestionRequestDto questionRequestDto);
  QuestionResponseDto deleteQuestionFromQuiz(String name, Long questionId);

}
