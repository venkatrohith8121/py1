products=[
	{'id':1,'name':'Marker Pen', 'category':'st'},
	{'id':2,'name':'Sugar', 'category':'gr'},
	{'id':3,'name':'Pens', 'category':'st'},
	{'id':4,'name':'Millet', 'category':'gr'},
	{'id':5,'name':'Duster', 'category':'st'},
	{'id':6,'name':'Dal', 'category':'gr'}
]
st_products=[]
gr_products=[]

# def filterdata(product):
#     if product['category']=='st':
#         return True
#     else:
#         return False
# print(list(filter(filterdata,products)))
fil_obj=filter(lambda product:product['category']=='st',products)
st_products=list(fil_obj)
print(st_products)