package com.trendfony.backend.product.model.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

import com.trendfony.backend.product.model.Product;
import com.trendfony.backend.store.model.Store;

public interface ProductRepository extends JpaRepository<Product, Long> {
    List<Product> findByStore(Store store);
}
