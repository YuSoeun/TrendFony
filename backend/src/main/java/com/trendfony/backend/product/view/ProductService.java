package com.trendfony.backend.product.service;

import com.trendfony.backend.product.model.Product;
import com.trendfony.backend.product.model.repository.ProductRepository;
import com.trendfony.backend.product.controller.response.ProductInfoResponse;
import com.trendfony.backend.product.view.dto.*;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.Optional;
import java.util.List;

@Service
@RequiredArgsConstructor
public class ProductService {
    private final ProductRepository productRepository;

    @Transactional
    public Long createProduct(CreateProductDto createProductDto) {
        Product savedProduct = productRepository.save(new Product(createProductDto));

        return savedProduct.getId();
    }

    @Transactional
    public void updateProduct(Long id, UpdateProductDto updateProductDto) {
        // TODO: throw exception when product is not present
        Product productInfo = productRepository.findById(id).orElse(null);

        if (productInfo != null) {
            productInfo.setName(updateProductDto.getName());
            productInfo.setRank(updateProductDto.getRank());
            productInfo.setCategoryRank(updateProductDto.getCategoryRank());
            productInfo.setPrice(updateProductDto.getPrice());
            productInfo.setReviewCnt(updateProductDto.getReviewCnt());
            productInfo.setRating(updateProductDto.getRating());

            productRepository.save(productInfo);
        }

        return;
    }

    @Transactional
    public ProductInfoResponse getProductById(Long id) {
        ProductInfoResponse response = null;
        Optional<Product> product = productRepository.findById(id);

        if (product.isPresent()) {
            Product productInfo = product.get();
            response = new ProductInfoResponse(
                    productInfo.getId(), productInfo.getName(),
                    productInfo.getCategory(), productInfo.getImageUrl(),
                    productInfo.getRank(), productInfo.getCategoryRank(),
                    productInfo.getPrice(), productInfo.getReviewCnt(),
                    productInfo.getRating(), productInfo.getIsSoldout(),
                    productInfo.getStoreName(), productInfo.getCreatedAt());
        }
        // TODO: throw product not found exception
//        else {
//            throw new Exception();
//        }

        return response;
    }

    @Transactional
    public List<ProductInfoResponse> getAllProducts() {
        List<ProductInfoResponse> response = null;

        for (Product productInfo : productRepository.findAll()) {
            if (productInfo != null) {
                response.add(new ProductInfoResponse(
                        productInfo.getId(), productInfo.getName(),
                        productInfo.getCategory(), productInfo.getImageUrl(),
                        productInfo.getRank(), productInfo.getCategoryRank(),
                        productInfo.getPrice(), productInfo.getReviewCnt(),
                        productInfo.getRating(), productInfo.getIsSoldout(),
                        productInfo.getStoreName(), productInfo.getCreatedAt()));
            }
        }

        return response;
    }

    @Transactional
    public void deleteProduct(Long id) {
        Optional<Product> product = productRepository.findById(id);

        if (product.isPresent()) {
            Product productInfo = product.get();

            productInfo.setDeleted(true);
            productRepository.save(productInfo);
        }
        // TODO: throw product not found exception
//        else {
//            throw new Exception();
//        }

        return;
    }
}
