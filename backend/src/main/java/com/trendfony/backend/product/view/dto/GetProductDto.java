package com.trendfony.backend.product.view.dto;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.AccessLevel;
import lombok.experimental.SuperBuilder;

@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class GetProductDto {
    private Long id;
    private String name;
    private String category;
    private String imageUrl;
    private Long rank;
    private Long categoryRank;
    private Long price;
    private Long reviewCnt;
    private float rating;
    private int isSoldout;
    private String storeName;
}