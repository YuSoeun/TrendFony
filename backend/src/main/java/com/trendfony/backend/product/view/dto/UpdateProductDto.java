package com.trendfony.backend.product.view.dto;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import lombok.AccessLevel;
import lombok.experimental.SuperBuilder;

import com.trendfony.backend.product.controller.request.UpdateProductRequest;

@Getter
@AllArgsConstructor
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class UpdateProductDto {
    private String name;
    private Long rank;
    private Long categoryRank;
    private Long price;
    private Long reviewCnt;
    private Long rating;

    public static UpdateProductDto from(UpdateProductRequest request) {
        return new UpdateProductDto(request.getName(), request.getRank(), request.getCategoryRank(),
                request.getPrice(), request.getReviewCnt(), request.getRating());
    }
}