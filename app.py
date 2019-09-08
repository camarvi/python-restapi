from flask import Flask, jsonify, request

from products import products

app = Flask(__name__)

#-----------------------------------------------------------------------

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Funcionando"})
#--------------------------------------------------------------------------
#------------       LISTAR TODOS LOS PRODUCTOS-----------------------------

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products_list" : products, "message": "Products list"})

#----------------------------------------------------------------------------
#------------       BUSCAR PRODUCTO POR NOMBRE ------------------------------

@app.route('/products/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name ]
    if (len(productsFound)>0):
        return jsonify({"product" : productsFound[0]})
    return jsonify({"message": "Product not found"})

#----------------------------------------------------------------------------------
#-----------  AÑADIR UN NUEVO PRODUCTO --------------------------------------------

@app.route('/products', methods=['POST'])
def addProduct():
    new_product ={
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message":"producto agregado","products":products})

#----------------------------------------------------------------------------------
#-----------          MODIFICAR UN PRODUCTO --------------------------------

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name ]
    if (len(productFound)>0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message" : "Product Update",
            "product" : productFound[0]
        })
    return jsonify({"message" : "Product Not Found"})

#--------------------------------------------------------------------
#--------------         ELIMINAR UN PRODUCTO ---------------------
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    ProductFoundDelete = [product for product in products if product['name'] == product_name]
    if (len(ProductFoundDelete) >0 ):
        products.remove(ProductFoundDelete[0])
        return jsonify({
            "message" : "Product Delete", 
            "products": products
            })

    return jsonify({"message" : "Product Not Found, not delete"})
#------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=4000)