package com.cooksys.quiz_api.dtos;

import java.sql.Timestamp;



import java.util.List;


import lombok.NoArgsConstructor;
import lombok.Data;
import lombok.AllArgsConstructor;



@NoArgsConstructor
@Data
@AllArgsConstructor
public class QuizResponseDto {

  private Long id;

  private String name;

  private Timestamp created;

  public List<QuestionResponseDto> questions;

}
