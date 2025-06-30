package com.cooksys.groupfinal.repositories;

import java.util.Set;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.cooksys.groupfinal.dtos.BasicUserDto;
import com.cooksys.groupfinal.dtos.CompanyDto;
import com.cooksys.groupfinal.entities.Company;

@Repository
public interface CompanyRepository extends JpaRepository<Company, Long> {

    Set<Company> findByEmployees_Id(Long userId);

}