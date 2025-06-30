package com.cooksys.springMock.services.impl;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.cooksys.springMock.dtos.AlbumRequestDto;
import com.cooksys.springMock.dtos.AlbumResponseDto;
import com.cooksys.springMock.dtos.TrackRequestDto;
import com.cooksys.springMock.entities.Album;
import com.cooksys.springMock.entities.Track;
import com.cooksys.springMock.mappers.AlbumMapper;
import com.cooksys.springMock.mappers.TrackMapper;
import com.cooksys.springMock.repositories.AlbumRepository;
import com.cooksys.springMock.repositories.TrackRepository;
import com.cooksys.springMock.services.AlbumService;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class AlbumServiceImpl implements AlbumService {
	
	private final AlbumRepository albumRepository;
	private final AlbumMapper albumMapper;
	private final TrackRepository trackRepository;
	private final TrackMapper trackMapper;

	@Override
	public List<AlbumResponseDto> getAllAlbums() {
		return albumMapper.entitiesToDtos(albumRepository.findAll());
	}
	
	@Override
	public AlbumResponseDto createAlbum(AlbumRequestDto albumRequestDto) {
		//grab ablum first, make sure album and artist name is the same
		Album albumCreated = albumRepository.saveAndFlush(albumMapper.dtoToEntity(albumRequestDto));
		for(Track track: albumCreated.getTracks()) {
			track.setAlbum(albumCreated);
			track.setArtist(albumCreated.getArtist());
		}
		
		trackRepository.saveAll(albumCreated.getTracks());
		return albumMapper.entityToDto(albumCreated);
		
	}
	
	@Override
	public AlbumResponseDto addTrack(Long id, TrackRequestDto trackRequestDto) {
		//find album based on name, make sure album and artist name is the same returns an object
		Optional<Album> optionalAlbum = albumRepository.findById(id);
		//get actual individual album
		//extract actual entity from Optional<Album>
		//get from object
		Album albumCreated = optionalAlbum.get();
		Track track = trackMapper.dtoToEntity(trackRequestDto);
		track.setAlbum(albumCreated);
		track.setArtist(albumCreated.getArtist());
		//adding to a list
		//albumCreated.getTracks().add(track);
		trackRepository.saveAndFlush(track);
	    return albumMapper.entityToDto(albumCreated);
		
	}
	
	//post and patch for different dataset thursday

}
