# A Simple LLM-to-SQL Pipeline

Building a basic prompt to sql pipeline, using the database tables given below.

### Model:
![LLM-to-SQL-Pipeline](model.png)

### Resources:
You can use either:
- LLM Model: llama-3.3-70b-versatile 
- Groq
- Using Python

### Requirements:
- Setup an account in Groq and create an apikey which can be used to further query the llm model of our choice. In this case llama-3.3-70b-versatile model is used

## Detailed Questions
Some of the questions which are used to test this model:

1. Which seller has delivered the most orders to customers in Rio de Janeiro? [string: seller_id]

2. What's the average review score for products in the 'beleza_saude' category? [float: score]

3. How many sellers have completed orders worth more than 100,000 BRL in total? [integer: count]

4. Which product category has the highest rate of 5-star reviews? [string: category_name]

5. What's the most common payment installment count for orders over 1000 BRL? [integer: installments]

6. Which city has the highest average freight value per order? [string: city_name]

7. What's the most expensive product category based on average price? [string: category_name]

8. Which product category has the shortest average delivery time? [string: category_name]

9. How many orders have items from multiple sellers? [integer: count]

10. What percentage of orders are delivered before the estimated delivery date? [float: percentage]

## Dataset and Schema
For this assignment we will use an open dataset [E-commerce dataset by Olist](https://www.kaggle.com/datasets/terencicp/e-commerce-dataset-by-olist-as-an-sqlite-database/data) from Kaggle.

```mermaid
erDiagram
    orders ||--o{ order_items : contains
    orders ||--o{ order_payments : has
    orders ||--o{ order_reviews : has
    orders }|--|| customers : placed_by
    order_items }|--|| products : includes
    order_items }|--|| sellers : sold_by
    orders {
        string order_id PK
        string customer_id FK
        string order_status
        datetime order_purchase_timestamp
        datetime order_approved_at
        datetime order_delivered_carrier_date
        datetime order_delivered_customer_date
        datetime order_estimated_delivery_date
    }
    order_items {
        string order_id FK
        int order_item_id PK
        string product_id FK
        string seller_id FK
        datetime shipping_limit_date
        float price
        float freight_value
    }
    order_payments {
        string order_id FK
        int payment_sequential
        string payment_type
        int payment_installments
        float payment_value
    }
    order_reviews {
        string review_id PK
        string order_id FK
        int review_score
        string review_comment_title
        string review_comment_message
        datetime review_creation_date
        datetime review_answer_timestamp
    }
    customers {
        string customer_id PK
        string customer_unique_id
        string customer_zip_code_prefix FK
        string customer_city
        string customer_state
    }
    sellers {
        string seller_id PK
        string seller_zip_code_prefix FK
        string seller_city
        string seller_state
    }
    products {
        string product_id PK
        string product_category_name
        int product_name_length
        int product_description_length
        int product_photos_qty
        float product_weight_g
        float product_length_cm
        float product_height_cm
        float product_width_cm
    }
```
