from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Sample products
products = [
    {'id': 1, 'name': 'Product 1', 'price': 29.99},
    {'id': 2, 'name': 'Product 2', 'price': 49.99},
    {'id': 3, 'name': 'Product 3', 'price': 19.99},
]

# Simple in-memory shopping cart
cart = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products")
def product_list():
    return render_template("product_list.html", products=products)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template("product_detail.html", product=product)

@app.route("/cart")
def cart_view():
    return render_template("cart.html", cart_items=cart)

@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)  # Add the product to the cart
    return redirect(url_for('cart_view'))

# New route for removing an item from the cart
@app.route("/remove_from_cart/<int:item_id>")
def remove_from_cart(item_id):
    global cart
    # Remove the item with the matching ID from the cart
    cart = [item for item in cart if item['id'] != item_id]  # Keep all items that don't match the ID
    return redirect(url_for('cart_view'))  # Redirect back to the cart view

@app.route("/checkout", methods=["POST"])
def checkout():
    return render_template("error.html")

@app.errorhandler(404)  # Customized error handling for 404
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5001)
