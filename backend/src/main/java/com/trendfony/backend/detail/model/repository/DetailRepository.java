package com.trendfony.backend.detail.model.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

import com.trendfony.backend.detail.model.Detail;
import com.trendfony.backend.keyword.model.Keyword;

public interface DetailRepository extends JpaRepository<Detail, Long> {
    List<Keyword> findByProductId(Long productId);
    List<Keyword> findByStoreId(Long storeId);
}
