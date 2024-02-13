
from Crow_app import db
from flask import render_template, redirect, request, url_for, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from Crow_app.models import Product
from Crow_app.products.forms import NewProduct
import os

def new_gallery(name):
    name = f"\{name}"
    location =os.path.abspath(os.path.dirname(__file__))+r"\static\uploads\products"+name
    os.mkdir(location)
    return location

productsr = Blueprint('products', __name__)



################# ROUTES ##################
@productsr.route("/products")
def products():
    products = Product.query.filter_by(status="public")
    return render_template("products.html", products = products)

@productsr.route("/remove-product/<id>")
def remove_product(id):
    product = Product.query.filter_by(id=id).first()
    print(product.name)
    
    db.session.delete(product)
    db.session.commit()

    return redirect(url_for('products.products'))

@productsr.route("/edit-product/<id>",methods=['POST','GET'])
def edit_product(id):
    form = NewProduct()
    product = Product.query.filter_by(id=id).first()

    if form.is_submitted():
        product.name = form.name.data
        if product.name != form.name.data:
            product.gallery = new_gallery(form.name.data)
        product.description = form.description.data
        product.part_id =form.part_id.data
        product.status = form.status.data
       
        
        if request.files['file'].filename !="":
            image = request.files['file']
            path = str(product.gallery + "/pic.png")
            product.main_photo = f"/static/uploads/products/{form.name.data}/pic.png"
            image.save(path)

        db.session.commit()
        return redirect(url_for('products.product', id=product.id, name= product.name ))

    return render_template("edit_product.html", form = form, product =product)



@productsr.route("/product/<name>/<id>")
def product(name, id):
    product = Product.query.get(id)
    return render_template("product.html", product=product)


@productsr.route("/new-products",methods=['POST','GET'])
def new_product():
    form = NewProduct()
    
    if form.is_submitted():
        
        
        product = Product(
            user_id=form.user_id.data,
            owner=form.owner.data,
            name=form.name.data,
            description=form.description.data,
            part_id=form.part_id.data,
            
            main_photo="",
            status=form.status.data)

        image = request.files['file']
        path = str(product.gallery + "/pic.png")
        product.main_photo = f"/static/uploads/products/{form.name.data}/pic.png"
        image.save(path)

        db.session.add(product)
        db.session.commit()
        
        return render_template("product.html", product = product)


    return render_template("new_product.html", form = form)
