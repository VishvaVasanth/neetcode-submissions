select name from Customers 
where id not in (select customer_id from Orders);
