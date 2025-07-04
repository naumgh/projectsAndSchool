package com.cooksys.quiz_api.dtos;

import java.sql.Timestamp;

import java.util.List;
import com.cooksys.quiz_api.dtos.*;
import lombok.NoArgsConstructor;
import lombok.Data;

@NoArgsConstructor
@Data
public class QuestionResponseDto {

  private Long id;

  private String text;

  private Timestamp created;

  private List<AnswerResponseDto> answers;

}
