package com.trendfony.backend.store.model;

import javax.persistence.*;

import lombok.Getter;
import lombok.Setter;

import com.trendfony.backend.common.BaseEntity;
import com.trendfony.backend.product.model.Product;
import com.trendfony.backend.detail.model.Detail;
import com.trendfony.backend.keyword.model.Keyword;

import java.util.List;

@Entity
@Getter
@Setter
public class Store extends BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String word;

    private Long count;
    @OneToMany(mappedBy = "store", cascade = CascadeType.ALL)
    private List<Detail> details;

    @OneToMany(mappedBy = "store", cascade = CascadeType.ALL)
    private List<Keyword> keywords;
}