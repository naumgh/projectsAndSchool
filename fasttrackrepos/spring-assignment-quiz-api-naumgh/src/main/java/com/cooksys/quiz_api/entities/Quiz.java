package com.cooksys.quiz_api.entities;

import java.sql.Timestamp;
import java.util.List;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.SQLRestriction;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@NoArgsConstructor
@Data
public class Quiz {

  @Id
  @GeneratedValue
  private Long id;

  private String name;

  @CreationTimestamp
  private Timestamp created;

  private boolean deleted = false;

  @OneToMany(mappedBy = "quiz")
  @SQLRestriction("deleted = false") // This annotation ensures that no deleted questions are pulled from the
                                     // database
  private List<Question> questions;

}
