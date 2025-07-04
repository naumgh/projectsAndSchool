package com.cooksys.social_media_project.entities;

import jakarta.persistence.Embeddable;
import lombok.Data;
import lombok.NoArgsConstructor;

@Embeddable
@NoArgsConstructor
@Data
public class Profile {

	String firstName;
	
	String lastName;
	
	String email;
	
	String phone;
	
}
