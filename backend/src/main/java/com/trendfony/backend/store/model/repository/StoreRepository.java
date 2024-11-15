package com.trendfony.backend.store.model.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

import com.trendfony.backend.store.model.Store;

public interface StoreRepository extends JpaRepository<Store, Long> {
}
