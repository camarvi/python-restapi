from flask import Flask, jsonify

from products import products

app = Flask(__name__)

#-----------------------------------------------------------------------

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Funcionando"})
#--------------------------------------------------------------------------

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products_list" : products, "message": "Products list"})
#----------------------------------------------------------------------------

@app.route('/products/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name ]
    if (len(productsFound)>0):
        return jsonify({"product" : productsFound[0]})
    return jsonify({"message": "Product not found"})

#----------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=4000)