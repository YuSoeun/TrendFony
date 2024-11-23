package com.trendfony.backend.product.model;

import javax.persistence.*;

import lombok.Getter;
import lombok.Setter;

import com.trendfony.backend.common.BaseEntity;
import com.trendfony.backend.store.model.Store;
import com.trendfony.backend.detail.model.Detail;
import com.trendfony.backend.keyword.model.Keyword;

import java.util.List;

@Entity
@Getter
@Setter
public class Product extends BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    private String url;

    @ManyToOne
    @JoinColumn(name = "store_id")
    private Store store;

    @OneToMany(mappedBy = "store", cascade = CascadeType.ALL)
    private List<Detail> details;

    @OneToMany(mappedBy = "store", cascade = CascadeType.ALL)
    private List<Keyword> keywords;
}