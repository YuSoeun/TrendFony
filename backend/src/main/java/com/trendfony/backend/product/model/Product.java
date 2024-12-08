package com.trendfony.backend.product.model;

import javax.persistence.*;

import lombok.Getter;
import lombok.Setter;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.Where;

import com.trendfony.backend.common.BaseEntity;
import com.trendfony.backend.keyword.model.Keyword;
import com.trendfony.backend.product.view.dto.CreateProductDto;


import java.util.List;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Where(clause = "deleted=false")
public class Product extends BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    private String category;

    private String imageUrl;

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

    public Product(CreateProductDto createProductDto) {
        this.name = createProductDto.getName();
        this.category = createProductDto.getCategory();
        this.imageUrl = createProductDto.getImageUrl();
        this.rank = createProductDto.getRank();
        this.categoryRank = createProductDto.getCategoryRank();
        this.price = createProductDto.getPrice();
        this.reviewCnt = createProductDto.getReviewCnt();
        this.rating = createProductDto.getRating();
        this.isSoldout = createProductDto.getIsSoldout();
        this.storeName = createProductDto.getStoreName();
        this.setDeleted(false);
    }
}