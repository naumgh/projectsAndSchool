package com.cooksys.springMock.services;

import java.util.List;

import com.cooksys.springMock.dtos.AlbumRequestDto;
import com.cooksys.springMock.dtos.AlbumResponseDto;
import com.cooksys.springMock.dtos.TrackRequestDto;

public interface AlbumService {

	List<AlbumResponseDto> getAllAlbums();

	//AlbumResponseDto createAlbum();

	AlbumResponseDto createAlbum(AlbumRequestDto albumRequestDto);

	AlbumResponseDto addTrack(Long id, TrackRequestDto trackRequestDto);

}
