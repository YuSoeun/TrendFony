package com.trendfony.backend.keyword.model.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

import com.trendfony.backend.keyword.Keyword;

public interface KeywordRepository extends JpaRepository<Keyword, Long> {
}
