from flask import Flask, render_template, request, redirect, url_for, flash
from product import product



app = Flask(__name__) 
app.secret_key = 'pass'

@app.route('/')
def index():
    return render_template('index.html', product = product )

# Добавление товара
@app.route('/admin/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Получение данных из формы
        name = request.form.get('name')
        image_url = request.form.get('image_url')
        price = request.form.get('price')
        wholesale_price = request.form.get('wholesale_price')
        description = request.form.get('description')
        category = request.form.get('category')
        quantity = request.form.get('quantity')

        # Создание нового товара
        new_product = {
            'id': len(products) + 1,
            'name': name,
            'image_url': image_url,
            'price': float(price),
            'wholesale_price': float(wholesale_price),
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
            return render_template('admin.html', product=product)
        else:
            flash('Не правельный логин или пароль!', 'error'), 407
    return render_template('login.html',product=product)

def find_product_by_id(product_id):
    for product in product:
        if product['id'] == product_id:
            return product
    return None

@app.route('/delete_card', methods=['POST'])
def delete_card():
    id = request.form['id']
    for card in product :
        print(str(id))
        if str(card['id']) == str(id):
            product.remove(card)
    return redirect('/admin')

# Поиск товара по ID в списке products
@app.route('/admin/edit_product/<int:product_id>', methods=['GET'])
def edit_product(product_id):
    # Поиск товара по ID
    product=find_product_by_id(product_id)

    if product:
        return render_template('edit_product.html', product=product)
    else:
        flash('Product not found.', 'error')
        return redirect(url_for('admin'))


# Обработка формы редактирования товара
@app.route('/admin/update_product/<int:product_id>', methods=['POST'])
def update_product(product_id):
    # Получение данных из формы
    name = request.form.get('name')
    image_url = request.form.get('image_url')
    price = float(request.form.get('price'))
    wholesale_price = request.form.get('wholesale_price')
    description = request.form.get('description')
    category = request.form.get('category')
    date = int(request.form.get('date'))

    # Поиск товара по ID
    product = find_product_by_id(product_id)

    if product:
        # Обновление данных товара
        product['name'] = name
        product['image_url'] = image_url
        product['price'] = price
        product['description'] = description
        product['wholesale_price'] = wholesale_price
        product['category'] = category
        product['date'] = date

        flash('Product updated successfully.', 'success')
    else:
        flash('Product not found.', 'error')

    # Перенаправление на страницу админки
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)