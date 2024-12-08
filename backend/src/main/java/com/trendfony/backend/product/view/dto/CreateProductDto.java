package com.trendfony.backend.product.view.dto;

import lombok.Getter;
import lombok.Setter;
import lombok.NoArgsConstructor;
import lombok.AccessLevel;
import lombok.experimental.SuperBuilder;

@Getter
@Setter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class CreateProductDto {
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