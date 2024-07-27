USE alx_book_store;  
SELECT   
    COLUMN_NAME,   
    DATA_TYPE,    
    CHARACTER_MAXIMUM_LENGTH,   
    NUMERIC_PRECISION,   
    NUMERIC_SCALE,   
    IS_NULLABLE  
FROM   
    INFORMATION_SCHEMA.COLUMNS,
    COLUMN_TYPE,
    TABLE_SCHEMA = 'alx_book_store',
    TABLE_NAME = 'Books'
WHERE   
    TABLE_NAME = 'Books';
