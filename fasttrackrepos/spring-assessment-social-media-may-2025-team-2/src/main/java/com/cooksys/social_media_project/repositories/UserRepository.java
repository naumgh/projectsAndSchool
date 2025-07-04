package com.cooksys.social_media_project.repositories;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.cooksys.social_media_project.entities.User;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {

	List<User> findAllByDeletedFalse();

    Optional<User> findByCredentials_Username(String username);
    
    Optional<User> findByCredentials_UsernameAndDeletedFalse(String username);
	
}
