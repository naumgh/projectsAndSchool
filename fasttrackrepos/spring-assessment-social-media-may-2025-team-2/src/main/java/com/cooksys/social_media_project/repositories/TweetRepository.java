package com.cooksys.social_media_project.repositories;

import java.util.List;
import java.util.Optional;

import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.cooksys.social_media_project.entities.Tweet;
import com.cooksys.social_media_project.entities.User;

@Repository
public interface TweetRepository extends JpaRepository<Tweet, Long> {
	
	List<Tweet> findAllByDeletedFalse(Sort sort);
	
	Optional<Tweet> findByIdAndDeletedFalse(Long id);
	List<Tweet> findAllByRepostOfAndDeletedFalse(Tweet repostOf);
	@Query("SELECT t FROM Tweet t JOIN t.mentions m WHERE m.credentials.username = :username AND t.deleted = false ORDER BY t.posted DESC")
	List<Tweet> findAllMentioningUser(@Param("username") String username);
	List<Tweet> findAllByAuthorCredentialsUsernameAndDeletedFalseOrderByPostedDesc(String username);
	List<Tweet> findAllByAuthorInAndDeletedFalseOrderByPostedDesc(List<User> authors);
	List<Tweet> findAllByInReplyToAndDeletedFalse(Tweet inReplyTo);
	List<Tweet> findAllByInReplyTo(Tweet inReplyTo);

}
