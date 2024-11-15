package com.trendfony.backend.keyword.model;

import javax.persistence.*;

import lombok.Getter;
import lombok.Setter;

import com.trendfony.backend.common.BaseEntity;
import com.trendfony.backend.product.Product;
import com.trendfony.backend.store.Store;

import java.util.List;

@Entity
@Getter
@Setter
public class Keyword extends BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String word;

    private Long count;

    @ManyToOne
    @JoinColumn(name = "product_id")
    private Product product;

    @ManyToOne
    @JoinColumn(name = "store_id")
    private Store store;
}