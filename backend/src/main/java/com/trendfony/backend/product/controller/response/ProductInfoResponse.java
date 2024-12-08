package com.trendfony.backend.product.controller.response;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDateTime;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class ProductInfoResponse {
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
    private LocalDateTime createdAt;
}