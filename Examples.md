## Examples for BestBuy API



| API Call                                                     | Info                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| /v1/products/8880044.xml?apiKey=<YourApiKey>                 | Get product information for sku 8880044; display as XML      |
| /v1/stores/187.json?apiKey=<YourApiKey>                      | Get information for store 187; display as JSON               |
| /v1/products?apiKey=<YourApiKey>                             | Get all products; show the first 10, sorted by name, display default attributes, formatted as xml |
| /v1/products?facet=manufacturer,10&apiKey=<YourApiKey>       | Get all products; show the first 10, sorted by name, display default attributes, formatted as xml, and display up to 10 facets based on the \"manufacturer\" field. |
| /v1/products?pageSize=50&page=4&apiKey=<YourApiKey>          | Get page 4 of all products, 50 products per page             |
| /v1/products?show=sku,name,salePrice&apiKey=<YourApiKey>     | Get all products, display only sku, name, and SalePrice for each |
| /v1/products?sort=regularPrice.desc&apiKey=<YourApiKey>      | Get all products, sort descending by regular price (most expensive first) |
| /v1/products(manufacturer=canon)?apiKey=<YourApiKey>         | Get all products manufactured by Canon                       |
| /v1/products(salePrice<299.99)?apiKey=<YourApiKey>           | Get all products whose sale price is less than $299.99       |
| /v1/products(manufacturer=canon&salePrice<299.99)?apiKey=<YourApiKey> | Get Canon products with sale price less than $299.99         |

