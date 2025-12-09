-- Таблица букеты
CREATE TABLE bouquets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price NUMERIC(10,2),
    image_url TEXT
);

-- Таблица клиентов
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20)
);

-- Таблица заказов
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount NUMERIC(10,2) NOT NULL
);

-- Таблица товаров в заказе
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    bouquet_id INT NOT NULL REFERENCES bouquets(id) ON DELETE CASCADE,
    quantity INT NOT NULL,
    price NUMERIC(10,2) NOT NULL
);


-- Букеты
INSERT INTO bouquets (name, description, price, image_url) VALUES
('Rose Bouquet', 'A beautiful bouquet of red roses', 29.99, 'rose.jpg'),
('Tulip Bouquet', 'Bright tulips for any occasion', 19.99, 'tulip.jpg'),
('Sunflower Bouquet', 'Sunny sunflowers to brighten your day', 24.99, 'sunflower.jpg');

-- Клиенты
INSERT INTO customers (first_name, last_name, email, phone) VALUES
('Alice', 'Smith', 'alice@example.com', '1234567890'),
('Bob', 'Johnson', 'bob@example.com', '0987654321');

-- Заказы
INSERT INTO orders (customer_id, order_date, total_amount) VALUES
(1, '2025-12-01 10:00:00', 49.98),
(2, '2025-12-02 15:30:00', 29.99);

-- Товары в заказе
INSERT INTO order_items (order_id, bouquet_id, quantity, price) VALUES
(1, 1, 1, 29.99),
(1, 2, 1, 19.99),
(2, 1, 1, 29.99);
