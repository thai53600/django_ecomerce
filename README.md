## DJANGO REST API

Install django libraries <br />
```pip install -r requirement.txt```

Create enviroment variables, follow by .env.example <br />
```.env```

Create migrations <br />
```python manage.py makemigrations```

Apply migrations to migrate tables in database <br />
```python manage.py migrate```

Start server <br />
```python manage.py runserver```

To run python shell <br />
```python manage.py shell```

## Available Route support GET, POST, PUT, DELETE
### prefix: /api/v1/
```/category/```<br />
```/category/:id/```<br />

```/product/```<br />
```/product/:id/```<br />

```/product/:product_id/images/```<br />
```/product/:product_id/images/:image_id/```<br />

```/upload-image/``` (only GET, POST)<br />
```/upload-multiple-image/``` (only POST)<br />

To enable upload image from POSTMAN: <br />
*File -> Settings -> General -> Read files outside working directory OFF->ON*<br />

To test upload image from POSTMAN: <br />
*Method: POST -> form-data -> Key: uploadImage (type: File)*