package com.trendfony.backend.product.controller;

import com.trendfony.backend.product.model.Product;
import com.trendfony.backend.product.service.ProductService;
import com.trendfony.backend.product.controller.response.ProductInfoResponse;
import com.trendfony.backend.product.view.dto.*;

import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/amazon")
public class ProductController {
    private final ProductService productService;

    public ProductController(ProductService productService) {
        this.productService = productService;
    }

    // **Create**: 새로운 상품 추가
    @PostMapping()
    public ResponseEntity<Long> createProduct(@RequestBody CreateProductDto dto) {
        Long response = productService.createProduct(dto);

        return ResponseEntity.ok(response);
    }

    // **Update**: 상품 정보 업데이트
    @PutMapping("")
    public ResponseEntity<Void> updateProduct(@PathVariable Long id, @RequestBody UpdateProductDto dto) {
        productService.updateProduct(id, dto);
        return ResponseEntity.ok().build();
    }

    // **Read (Detail)**: 특정 ID로 상품 상세 정보 조회
    @GetMapping("/detail")
    public ResponseEntity<ProductInfoResponse> readProduct(@RequestParam Long id) {
        ProductInfoResponse response = productService.getProductById(id);
        return ResponseEntity.ok(response);
    }

    // **List**: 모든 상품 가져오기
    @GetMapping("/list")
    public ResponseEntity<List<ProductInfoResponse>> readAllProducts() {
        List<ProductInfoResponse> response = productService.getAllProducts();
        return ResponseEntity.ok(response);
    }

    // **Delete**: 상품 삭제
    @DeleteMapping("")
    public ResponseEntity<Void> deleteProduct(@RequestParam Long id) {
       productService.deleteProduct(id);
        return ResponseEntity.ok().build();
    }
}