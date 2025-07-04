package com.cooksys.social_media_project.entities;

import java.sql.Timestamp;
import java.util.List;

import org.hibernate.annotations.CreationTimestamp;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.JoinTable;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.ManyToOne;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@NoArgsConstructor
@Data
public class Tweet {

	@Id
	@GeneratedValue
	private Long id;

	@CreationTimestamp
	private Timestamp posted;

	private boolean deleted;

	private String content;

	@ManyToOne
	@JoinColumn(name = "author")
	private User author;

	@ManyToOne
	@JoinColumn(name = "inReplyTo")
	private Tweet inReplyTo;

	@ManyToOne
	@JoinColumn(name = "repostOf")
	private Tweet repostOf;

	@ManyToMany(mappedBy = "likedTweets")
	private List<User> likedBy;

	@ManyToMany(mappedBy = "mentionedIn")
	private List<User> mentions;

	@ManyToMany
	@JoinTable(name = "tweet_hashtags", joinColumns = @JoinColumn(name = "tweet_id"), inverseJoinColumns = @JoinColumn(name = "hashtag_id"))
	private List<Hashtag> hashtags;

}
