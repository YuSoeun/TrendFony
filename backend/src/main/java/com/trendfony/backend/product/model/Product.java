package com.trendfony.backend.product.model;

import javax.persistence.*;

import lombok.Getter;
import lombok.Setter;

import com.trendfony.backend.common.BaseEntity;

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

    @OneToMany(mappedBy = "store", cascade = CascadeType.ALL)
    private List<Detail> details;

    @OneToMany(mappedBy = "store", cascade = CascadeType.ALL)
    private List<Keyword> keywords;
}