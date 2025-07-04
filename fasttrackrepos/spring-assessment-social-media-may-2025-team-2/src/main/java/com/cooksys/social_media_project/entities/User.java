package com.cooksys.social_media_project.entities;

import java.sql.Timestamp;
import java.util.List;

import org.hibernate.annotations.CreationTimestamp;

import jakarta.persistence.Embedded;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.JoinTable;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
import lombok.Data;
import lombok.NoArgsConstructor;

@Table(name = "user_table")
@Entity
@NoArgsConstructor
@Data
public class User {

	@Id
	@GeneratedValue
	private Long id;

	@CreationTimestamp
	private Timestamp joined;

	private boolean deleted;

	@Embedded
	private Credentials credentials;

	@Embedded
	private Profile profile;

	@OneToMany(mappedBy = "author")
	private List<Tweet> tweets;

	@ManyToMany
	@JoinTable(name = "user_likes", joinColumns = @JoinColumn(name = "user_id"), inverseJoinColumns = @JoinColumn(name = "tweet_id"))
	private List<Tweet> likedTweets;

	@ManyToMany
	@JoinTable(name = "user_mentions", joinColumns = @JoinColumn(name = "user_id"), inverseJoinColumns = @JoinColumn(name = "tweet_id"))
	private List<Tweet> mentionedIn;

	@ManyToMany
	@JoinTable(name = "followers_following", joinColumns = @JoinColumn(name = "follower_id"), inverseJoinColumns = @JoinColumn(name = "following_id"))
	private List<User> following;

	@ManyToMany(mappedBy = "following")
	private List<User> followers;

}
