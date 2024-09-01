use adventureworks;
# ACHAR O ProductCategoryKey DA TABELA DE CATEGORIAS PARA BICICLETAS
# RETORNA 1
SELECT ProductCategoryKey AS KEY_CATEGORIA_PRODUTOS_BICICLETA
FROM adventureworks_product_categories
WHERE CategoryName = 'Bikes';

# ACHAR OS VALORES DE ProductSubcategoryKey DERIVADOR DA CATEGORIA DE BICICLETAS
# RETORNA-RA 1, 2 e 3
SELECT ProductSubcategoryKey AS KEY_SUBCATEGORIA_PRODUTOS_BICICLETA
FROM adventureworks_product_subcategories
WHERE ProductCategoryKey IN (
    SELECT ProductCategoryKey
    FROM adventureworks_product_categories
    WHERE CategoryName = 'Bikes'
);

# ACHAR OS VALORES DE ProductKey DERIVADOR DAS SUB CATEGORIAS DE BICICLETAS
SELECT ProductKey AS KEY_PRODUTOS
FROM adventureworks_products
WHERE ProductSubcategoryKey IN (
    SELECT ProductSubcategoryKey
    FROM adventureworks_product_subcategories
    WHERE ProductCategoryKey IN (
        SELECT ProductCategoryKey
        FROM adventureworks_product_categories
        WHERE CategoryName = 'Bikes'
    )
);

# CONSULTA FINAL DIVIDIDA EM ProductKey, ANO e QUANTIDADE_VENDIDA
# SOMANDO OS VALORES DE OrderQuantity,
# FILTRANDO OS RESULTADOS A PARTIR DE ProductKey E ANO DENTRO DO INTERVALO DE 2016 e 2017,
# AGRUPANDO POR ProductKey E ANO,
# ORDENANDO POR QUANTIDADE_VENDIDA DE FORMA DECRECENTE
# E LIMITANDO OS VALORES AOS 10 PRIMEIROS
SELECT (
    SELECT ProductName
    FROM adventureworks_products
    WHERE adventureworks_sales.ProductKey = adventureworks_products.ProductKey
    ) as NOME
    , YEAR(STR_TO_DATE(OrderDate, '%m/%d/%Y')) as ANO, SUM(OrderQuantity) as QUANTIDADE_VENDIDA
FROM adventureworks_sales
WHERE ProductKey IN (
    SELECT ProductKey
    FROM adventureworks_products
    WHERE ProductSubcategoryKey IN (
        SELECT ProductSubcategoryKey
        FROM adventureworks_product_subcategories
        WHERE ProductCategoryKey IN (
            SELECT ProductCategoryKey
            FROM adventureworks_product_categories
            WHERE CategoryName = 'Bikes'
        )
    )
)
AND YEAR(STR_TO_DATE(OrderDate, '%m/%d/%Y'))
        IN (2016,2017)
GROUP BY NOME, ANO
ORDER BY QUANTIDADE_VENDIDA DESC
LIMIT 10
;
