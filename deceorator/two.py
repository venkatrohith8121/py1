def login_requried(func):
    def inner(name,is_login):
        if is_login==False:
            print('login is required')
        else:
            func(name,is_login)
    return inner

def home_page(name,login):
    print('home page')
def about_page(name,login):
    print('about page')
def product_page(name,login):
    print('product page')
@login_requried
def order_page(name,login):
    print('order page')
    
home_page('rahul',False)
about_page('rahul',False)
product_page('rahul',False)
order_page('rahul',False) 