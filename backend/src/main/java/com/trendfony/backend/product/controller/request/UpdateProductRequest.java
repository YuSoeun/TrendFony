package com.trendfony.backend.product.controller.request;

import lombok.Getter;
import lombok.Setter;
import lombok.NoArgsConstructor;

@Getter
@Setter
@NoArgsConstructor
public class UpdateProductRequest {
    private String name;
    private Long rank;
    private Long categoryRank;
    private Long price;
    private Long reviewCnt;
    private float rating;
}