from flask import Flask, render_template, request, redirect, url_for, flash
from products import products 



app = Flask(__name__) 
app.secret_key = 'pass'

@app.route('/')
def index():
    return render_template('index.html', products = products )

# Добавление товара
@app.route('/admin/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Получение данных из формы
        name = request.form.get('name')
        image_url = request.form.get('image_url')
        price = request.form.get('price')
        description = request.form.get('description')
        category = request.form.get('category')
        quantity = request.form.get('quantity')

        # Создание нового товара
        new_product = {
            'id': len(products) + 1,
            'name': name,
            'image_url': image_url,
            'price': float(price),
            'description': description,
            'category': category,
            'quantity': int(quantity)
        }

        # Добавление нового товара в список
        products.append(new_product)

        flash('Product added successfully.', 'success')
        return redirect(url_for('admin'))

    return render_template('add_product.html')

# Админка
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Проверка логина и пароля
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'milk_admin' and password == 'Atmosphere29567':
            return render_template('admin.html', products=products)
        else:
            flash('Не правельный логин или пароль!', 'error'), 407
    return render_template('login.html',products=products)

def find_product_by_id(products_id):
    for products in products:
        if products['id'] == products_id:
            return products
    return None

@app.route('/delete_card', methods=['POST'])
def delete_card():
    id = request.form['id']
    for card in products :
        print(str(id))
        if str(card['id']) == str(id):
            products .remove(card)
    return redirect('/admin')

# Поиск товара по ID в списке products
@app.route('/admin/edit_product/<int:product_id>', methods=['GET'])
def edit_product(products_id):
    # Поиск товара по ID
    products = find_product_by_id(products_id)

    if products:
        return render_template('edit_product.html', products=products)
    else:
        flash('Product not found.', 'error')
        return redirect(url_for('admin'))


# Обработка формы редактирования товара
@app.route('/admin/update_product/<int:product_id>', methods=['POST'])
def update_product(products_id):
    # Получение данных из формы
    name = request.form.get('name')
    image_url = request.form.get('image_url')
    price = float(request.form.get('price'))
    description = request.form.get('description')
    category = request.form.get('category')
    quantity = int(request.form.get('quantity'))

    # Поиск товара по ID
    products = find_product_by_id(products_id)

    if products:
        # Обновление данных товара
        products['name'] = name
        products['image_url'] = image_url
        products['price'] = price
        products['description'] = description
        products['category'] = category
        products['quantity'] = quantity

        flash('Product updated successfully.', 'success')
    else:
        flash('Product not found.', 'error')

    # Перенаправление на страницу админки
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)