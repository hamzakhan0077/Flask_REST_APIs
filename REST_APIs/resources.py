from flask_restful import Resource, reqparse, fields, marshal_with, abort
from REST_APIs import api, db, app
from REST_APIs.models import Customer
import uuid
import http

# Request parser makes sure that the required data is sent with the request
customer_args = reqparse.RequestParser()
customer_args.add_argument("name", type=str, help="Customer name is required", required=True)
customer_args.add_argument("email", type=str, help="Customer email required", required=True)
customer_args.add_argument("note", type=str, help="Leave an optional note ")

# update parser, so a user can update some specific info
customer_update_args = reqparse.RequestParser()
# no required attribute as args are optional
customer_update_args.add_argument("name", type=str, help="Customer name is required")
customer_update_args.add_argument("email", type=str, help="Customer email required")
customer_update_args.add_argument("note", type=str, help="Leave an optional note ")

# Serializing the db instance
# Resource fields is a way of defining how an object should be serialized
# @marshall_with decorator, when we return, take the return value and serialize it with the resource field
cust_resource_fields = {

    'id': fields.String,
    'name': fields.String,
    'email': fields.String,
    'note': fields.String

}


class Customers_By_Id(Resource):
    @marshal_with(cust_resource_fields)
    def get(self, id):
        res = Customer.query.filter_by(id=id).first()
        if not res:
            abort(http.HTTPStatus.NOT_FOUND, message="Customer not found")
        return res

        # data = []
        # for cust in Customer.query.all():
        #     data.append({'id': cust.id,'name':cust.name,'email':cust.email,"note":cust.note})
        # return data

    def post(self):
        return {"data": "data Posted"}


    @marshal_with(cust_resource_fields)
    def patch(self, id):
        args = customer_update_args.parse_args()
        res = Customer.query.filter_by(id=id).first()
        if not res:
            abort(http.HTTPStatus.NOT_FOUND, message="Customer not found")

        for arg in args:
            if args[arg]:
                # setattr allows to manipulate the data in an object
                # it is handy in preventing this object.arg which is not possible. Because arg comes from the loop
                setattr(res, arg, args[arg])
                # db.session.add(res)
                db.session.commit()
        return res

    @marshal_with(cust_resource_fields)
    def delete(self, id):
        res = Customer.query.filter_by(id=id).first()
        if not res:
            abort(http.HTTPStatus.NOT_FOUND, message="Customer not found")
        db.session.delete(res)
        db.session.commit()
        return '',http.HTTPStatus.NO_CONTENT


class Customers(Resource):
    @marshal_with(cust_resource_fields)
    def put(self):
        args = customer_args.parse_args()
        cust = Customer(id=str(uuid.uuid4()), name=args['name'], email=args['email'], note=args['note'])

        db.session.add(cust)
        db.session.commit()
        return cust, http.HTTPStatus.OK
    
    @marshal_with(cust_resource_fields)
    def get(self):
        res = Customer.query.all()
        return res
       


api.add_resource(Customers_By_Id, "/customers/<string:id>")
api.add_resource(Customers,"/customers")
