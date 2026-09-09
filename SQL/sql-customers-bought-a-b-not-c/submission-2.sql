-- Write your query below
select distinct c.customer_id, c.customer_name from customers c
join Orders o on c.customer_id = o.customer_id
where o.customer_id not in (select customer_id from Orders where product_name = 'C' ) and o.customer_id in (select customer_id from Orders where product_name = 'A' )
and o.customer_id in (select customer_id from Orders where product_name = 'B' )
order by c.customer_name;
