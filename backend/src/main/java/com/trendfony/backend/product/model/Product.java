package com.trendfony.backend.product.model;

import javax.persistence.*;

import lombok.Getter;
import lombok.Setter;

import com.trendfony.backend.common.BaseEntity;
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

    @Column(name = "`rank`")
    private Long rank;

    private Long categoryRank;

    private Long price;

    private Long reviewCnt;

    private Long rating;

    private int isSoldout;

    private String storeName;

    @OneToMany(mappedBy = "product", cascade = CascadeType.ALL)
    private List<Keyword> keywords;
}