package com.trendfony.backend.detail.model;

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
public class Detail extends BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Long rank;

    private Long categoryRank;

    private Long price;

    private Long reviewCnt;

    private Long rating;

    private int isSoldout;

    @ManyToOne
    @JoinColumn(name = "product_id")
    private Product product;

    @ManyToOne
    @JoinColumn(name = "store_id")
    private Store store;
}