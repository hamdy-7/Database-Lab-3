USE library_db;

INSERT INTO AUTHOR (author_id, name, country, photo_url) VALUES 
(1, 'Naguib Mahfouz', 'Egypt', NULL),
(2, 'Taha Hussein', 'Egypt', NULL),
(3, 'William Shakespeare', 'UK', NULL);

INSERT INTO BOOK (book_id, title, price, author_id, cover_url) VALUES 
(1, 'Palace Walk', 15.50, 1, NULL),
(2, 'Sugar Street', 18.00, 1, NULL),
(3, 'The Days', 12.00, 2, NULL),
(4, 'The Future of Culture in Egypt', 14.25, 2, NULL),
(5, 'Hamlet', 20.00, 3, NULL),
(6, 'Macbeth', 22.50, 3, NULL);