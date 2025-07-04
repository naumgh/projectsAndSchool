package com.cooksys.quiz_api.mappers;

import java.util.List;



import org.mapstruct.Mapper;

import com.cooksys.quiz_api.dtos.QuizRequestDto;
import com.cooksys.quiz_api.dtos.QuizResponseDto;
import com.cooksys.quiz_api.entities.Quiz;
import com.cooksys.quiz_api.services.impl.QuizServiceImpl;

@Mapper(componentModel = "spring", uses = { QuestionMapper.class })
public interface QuizMapper {

  QuizResponseDto entityToDto(Quiz entity);

  List<QuizResponseDto> entitiesToDtos(List<Quiz> entities);
  Quiz requestDtoToEntity(QuizRequestDto dto);
}
