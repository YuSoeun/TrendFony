package com.trendfony.backend.product.model.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

import com.trendfony.backend.product.model.Product;
import com.trendfony.backend.keyword.model.Keyword;

public interface ProductRepository extends JpaRepository<Product, Long> {
    List<Keyword> findByProductId(Long productId);
    List<Keyword> findByStoreId(Long storeId);
}
