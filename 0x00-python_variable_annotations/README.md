# Python - Variable Annotations

![](https://i.redd.it/y9y25tefi5401.png)

```
Variable annotations in Python allow you to specify the type of a variable without actually enforcing
it at runtime.
Variable annotations use the colon (:) followed by the type hint expression to indicate the expected type 
of the variable.
```

```
josephgreen@JosephGreen-Mugabi:~/alx-backend-python/0x00-python_variable_annotations$ cat 0-main.py 
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)josephgreen@JosephGreen-Mugabi:~/alx-backend-python/0x00-python_variable_annotations$
```
### Results after executing the main file
```
josephgreen@JosephGreen-Mugabi:~/alx-backend-python/0x00-python_variable_annotations$ ./0-main.py 
True
{'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
josephgreen@JosephGreen-Mugabi:~/alx-backend-python/0x00-python_variable_annotations$
```


