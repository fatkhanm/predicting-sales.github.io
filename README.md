# Tubes_SIL

##File Stack
### backend
Untuk menyimpan file - file yang menangani model learningnya dan melakukan prediksi pada tingkat penjualan suatu produk
```
app.py : runner dari flask app
predict.py : controller API predict
env : folder env untuk deployment API
```
### frontend
Untuk menghasilkan tampilan website
```
index.html : kode program html
back3.webp : file gambar untuk background
tamplate form : https://www.w3docs.com/learn-html/html-form-templates.html
```

## API Documentation
```
https://heroku-sil.herokuapp.com/predict

body:
{
    "item_weight":9.30,
    "item_visibility":0.016047,
    "item_mrp":249.8092,
    "fat_content":"low fat",
    "item_type":"meat",
    "outlet_size":"small",
    "outlet_location":"tier 1",
    "outlet_store":"grocery store"
}

response
Int (item sales predicting )
```
