1.  SELECT DISTINCT country
    FROM Customers
    ORDER BY country ASC;

2.  SELECT DISTINCT age
    FROM Customers
    ORDER BY age ASC;

3.  SELECT item, amount
    FROM Orders;

4.  SELECT item, min(quantity)
    FROM Orders;

5.  SELECT item, SUM(quantity) AS total_quantity
    FROM orders
    GROUP BY item
    ORDER BY total_quantity DESC
    LIMIT 3;

6.  SELECT status, COUNT (*) as count
    FROM Shippings
    GROUP BY status;

7.  SELECT Singer, SUM(Sale) AS SumSales
    FROM albums
    GROUP BY Singer;

8.  SELECT Singer,  max(year) as MaxYear
    from albums
    GROUP BY Singer;