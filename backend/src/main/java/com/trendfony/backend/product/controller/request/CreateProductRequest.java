package com.trendfony.backend.product.controller.request;

import lombok.Getter;
import lombok.Setter;
import lombok.NoArgsConstructor;

@Getter
@Setter
@NoArgsConstructor
public class CreateProductRequest {
    private String name;
    private String category;
    private String imageUrl;
    private Long rank;
    private Long categoryRank;
    private Long price;
    private Long reviewCnt;
    private Long rating;
    private int isSoldout;
    private String storeName;
}