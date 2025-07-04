package com.cooksys.quiz_api.dtos;

import java.util.List;
import lombok.Data;
import lombok.NoArgsConstructor;
import com.cooksys.quiz_api.dtos.QuestionRequestDto;



@Data
@NoArgsConstructor
public class QuizRequestDto {
	private String name;
	private List<QuestionRequestDto> questions;
}
