package com.cooksys.social_media_project.repositories;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.cooksys.social_media_project.entities.Hashtag;

@Repository
public interface HashtagRepository extends JpaRepository<Hashtag, Long> {

	boolean existsByLabelIgnoreCase(String label);
	
	Optional<Hashtag> findByLabel(String label);
	
	Optional<Hashtag> findByLabelIgnoreCase(String label);
	
}


