create schema adventureworks;
use adventureworks;
create table adventureworks_calendar
(
    Date char(12) null
);

create table adventureworks_customers
(
    CustomerKey    int  null,
    Prefix         text null,
    FirstName      text null,
    LastName       text null,
    BirthDate      text null,
    MaritalStatus  text null,
    Gender         text null,
    EmailAddress   text null,
    AnnualIncome   text null,
    TotalChildren  text null,
    EducationLevel text null,
    Occupation     text null,
    HomeOwner      text null
);

create table adventureworks_product_categories
(
    ProductCategoryKey int  not null,
    CategoryName       text null,
    primary key (ProductCategoryKey)
);

create table adventureworks_product_subcategories
(
    ProductSubcategoryKey int      not null,
    SubcategoryName       char(50) null,
    ProductCategoryKey    int      null,
    primary key (ProductSubcategoryKey)
);

create table adventureworks_products
(
    ProductKey            int   not null,
    ProductSubcategoryKey int   null,
    ProductSKU            text  null,
    ProductName           text  null,
    ModelName             text  null,
    ProductDescription    text  null,
    ProductColor          text  null,
    ProductSize           text  null,
    ProductStyle          text  null,
    ProductCost           float null,
    ProductPrice          float null
);

create table adventureworks_returns
(
    ReturnDate     char(12) null,
    TerritoryKey   int      null,
    ProductKey     int      null,
    ReturnQuantity int      null
);

create table adventureworks_sales
(
    OrderDate     char(12) null,
    StockDate     char(12) null,
    OrderNumber   char(50) null,
    ProductKey    int      null,
    CustomerKey   int      null,
    TerritoryKey  int      null,
    OrderLineItem int      null,
    OrderQuantity int      null
);

create table adventureworks_territories
(
    SalesTerritoryKey int  null,
    Region            text null,
    Country           text null,
    Continent         text null
);

