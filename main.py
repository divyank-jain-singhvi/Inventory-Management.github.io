from flask import Flask, render_template,request
from firebase import firebase

firebase=firebase.FirebaseApplication("https://inventory-management-9acd5-default-rtdb.firebaseio.com/",None)
app = Flask(__name__)
app = Flask(__name__, static_url_path='/static', static_folder='static')
email=None
password=None

@app.route('/', methods=['GET', 'POST'])
def index6():
    return render_template('index6.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/index1', methods=['GET', 'POST'])
def index1():
    global email
    email=email.replace('@gmail.com','')
    data=firebase.get('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email,'')
    
    if data==None:
        return render_template('index1.html')
    
    l2=[]
    for i in data:
        l1=[]
        
        for j in data[i]:
            l1.append(data[i][j])
        l2.append(l1)
        
    result=l2
    
    return render_template('index1.html',result=result)

@app.route('/index2', methods=['GET', 'POST'])
def index2():
    return render_template('index2.html')

@app.route('/index3', methods=['GET', 'POST'])
def index3():
    global email
    data=firebase.get('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email,'')
    if data==None:
        return render_template('index3.html')
    
    l2=[]
    for i in data:
        l1=[]
        
        for j in data[i]:
            l1.append(data[i][j])
        l2.append(l1)
        
    result=l2
    
    return render_template('index3.html',result=result)


@app.route('/index4', methods=['GET', 'POST'])
def index4():
    global email
    data=firebase.get('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email,'')
    if data==None:
        return render_template('index4.html')
    
    l2=[]
    for i in data:
        l1=[]
        
        for j in data[i]:
            l1.append(data[i][j])
        l2.append(l1)
        
    result=l2
    return render_template('index4.html',result=result)


@app.route('/index5', methods=['GET', 'POST'])
def index5():
    global email
    
    data=firebase.get('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email,'')
    if data==None:
        return render_template('index5.html')
    
    l2=[]
    for i in data:
        l1=[]
        
        for j in data[i]:
            l1.append(data[i][j])
        l2.append(l1)
        
    result=l2
    
    return render_template('index5.html',result=result)

@app.route('/add_product', methods=['GET','POST'])

def submit():
    global email
    serial_number = request.form['codedata']
    amount_data = request.form['amountdata']
    buy_cost = request.form['buycost']
    sell_cost=request.form['sellcost']
    product_name=request.form['product_name']
    product_buy=request.form['product_buy']
    
    
    data={
          'Serial Number':serial_number,
          'Product Name':product_name,
          'Quantity':amount_data,
          'Purchase Cost':buy_cost,
          'Selling Price':sell_cost,
          'From Where product Purchased':product_buy,
          }


    firebase.post('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email, data)
    data=firebase.get('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email,'')
    
    l2=[]
    for i in data:
        l1=[]
        
        for j in data[i]:
            l1.append(data[i][j])
        l2.append(l1)
        
    result=l2
    
    return render_template('index1.html',result=result)




@app.route('/find_product', methods=['GET','POST'])

def submit2():
    global email
    data=firebase.get('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email,'')
    
    if data==None:
        return render_template('index2.html')

    product_name=request.form['product_name2']
    serial_number=request.form['serial_number']
    dict1={}
    l4=[]
    for i in data:
        if product_name!='' or serial_number!='':
            temp_dict={}
            data_list=[]
            data_list.append(data[i]['Serial Number'])
            data_list.append(data[i]['Product Name'])
            temp_dict={i:data_list}
            dict1.update(temp_dict)
    print(product_name)
    
    
    for j in dict1:
        search_list=dict1[j]
        l3=[]
        if serial_number in search_list:
            if serial_number!='':
                data1=data[j]
                
                for p in data1:
                    l3.append(data1[p])
                
                l4.append(l3)
        if product_name in search_list:
            if product_name !='':
                data1=data[j]
                
                for p in data1:
                    l3.append(data1[p])
                l4.append(l3)
            
    for q in l4:
        q.pop(0)
    result=l4
    
    return render_template('index2.html',result=result)
    
@app.route('/sell_product', methods=['GET','POST'])

def submit3():
    global email
    
    data=firebase.get('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email,'')
    
    if data==None:
        return render_template('index3.html')
    
    product_name=request.form['product_name2']
    serial_number=request.form['serial_number']
    selling_quantity=request.form['selling_quantity']
    dict1={}
    l4=[]
    l5=[]
    for i in data:
        if product_name!='' or serial_number!='':
            temp_dict={}
            data_list=[]
            data_list.append(data[i]['Serial Number'])
            data_list.append(data[i]['Product Name'])
            temp_dict={i:data_list}
            dict1.update(temp_dict)
    print(product_name)
    
    
    for j in dict1:
        search_list=dict1[j]
        l3=[]
        if serial_number in search_list:
            if serial_number!='':
                data1=data[j]
                
                for p in data1:
                    l3.append(data1[p])
                
                l4.append(l3)
        if product_name in search_list:
            if product_name !='':
                data1=data[j]
                
                for p in data1:
                    l3.append(data1[p])
                l4.append(l3)
    
    for i in l4:
        l5.append(i[3])
        
    for key, value in data.items():
        if value.get('Serial Number') == serial_number:
            data_key=key
            break
    else:
        data_key = None
    
    firebase.put('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email+'/'+data_key, 'Quantity', str(int(l5[0])-int(selling_quantity)))
    
    
    data=firebase.get('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email,'')
    
    l2=[]
    for i in data:
        l1=[]
        
        for j in data[i]:
            l1.append(data[i][j])
        l2.append(l1)
        
    result=l2
    
    return render_template('index3.html',result=result)


@app.route('/update_product', methods=['GET','POST'])

def submit4():
    global email
    data=firebase.get('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email,'')
    
    if data==None:
        return render_template('index4.html')
    
    serial_number = request.form['codedata']
    amount_data = request.form['amountdata']
    buy_cost = request.form['buycost']
    sell_cost=request.form['sellcost']
    product_name=request.form['product_name']
    product_buy=request.form['product_buy']
    dict1={}
    l4=[]
    l5=[]
    for i in data:
        if product_name!='' or serial_number!='':
            temp_dict={}
            data_list=[]
            data_list.append(data[i]['Serial Number'])
            data_list.append(data[i]['Product Name'])
            temp_dict={i:data_list}
            dict1.update(temp_dict)
    
    
    for j in dict1:
        search_list=dict1[j]
        l3=[]
        if serial_number in search_list:
            if serial_number!='':
                data1=data[j]
                
                for p in data1:
                    l3.append(data1[p])
                
                l4.append(l3)
        if product_name in search_list:
            if product_name !='':
                data1=data[j]
                
                for p in data1:
                    l3.append(data1[p])
                l4.append(l3)

    for i in l4:
        l5.append(i[3])
        
    for key, value in data.items():
        if value.get('Serial Number') == serial_number:
            data_key=key
            break
        elif value.get('Product Name') == product_name:
            data_key=key
            break
    else:
        data_key = None
    
    if amount_data=='':
        amount_data=l4[0][3]
    if product_buy=='':
        product_buy=l4[0][0]
    if product_name=='':
        product_name=l4[0][1]
    if buy_cost=='':
        buy_cost=l4[0][2]
    if sell_cost=='':
        sell_cost=l4[0][4]
    
    
    keys=['Quantity','Purchase Cost','Selling Price','Product Name','From Where product Purchased']
    value=[amount_data,buy_cost,sell_cost,product_name,product_buy]
    list_index=0
    while True:
        firebase.put('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email+'/'+data_key,keys[list_index],value[list_index])
        list_index=list_index+1;
        if list_index==5:
            break
     
    
    data=firebase.get('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email,'')
    if data==None:
        return render_template('index4.html')
    
    l2=[]
    for i in data:
        l1=[]
        
        for j in data[i]:
            l1.append(data[i][j])
        l2.append(l1)
        
    result=l2
    
    return render_template('index4.html',result=result)

@app.route('/delete_product', methods=['GET','POST'])
def submit5():
    global email
    data=firebase.get('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email,'')
    
    if data==None:
        return render_template('index5.html')
    
    product_name=request.form['product_name']
    serial_number=request.form['serial_number']
    

    for key, value in data.items():
        if value.get('Serial Number') == serial_number:
            data_key=key
            break
        elif value.get('Product Name') == product_name:
            data_key=key
            break
    else:
        data_key = None
    
    firebase.delete('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email,data_key)
    data=firebase.get('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Products/'+email,'')
    if data==None:
        return render_template('index5.html')
    l2=[]
    for i in data:
        l1=[]
        
        for j in data[i]:
            l1.append(data[i][j])
        l2.append(l1)
        
    result=l2
    
    return render_template('index5.html',result=result)

@app.route('/login', methods=['GET','POST'])
def submit6():
    global email
    if request.method == 'POST':
        if 'login' in request.form:
            email=request.form['email']
            password = request.form['user_password']
            print(email,password)
            
            input_data={
                'Email':email,
                'Password':password
                }
            
            data=firebase.get('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Users','')
            if data==None:
                message='You dont have an account'
                return render_template('index6.html',message=message)
            for key,value in data.items():
                if value == input_data:
                    return render_template('index.html')
                
            message='You dont have an account'
            return render_template('index6.html',message=message)
        
        
        elif 'sign_in' in request.form:
            email=request.form['email']
            password = request.form['user_password']
            print(email,password)
            print(type(email))
            input_data={
                'Email':email,
                'Password':password
                }
            data=firebase.get('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Users','')
            try:
                for key,value in data.items():
                    if value == input_data:
                        message='Your Already Have An Account'
                        return render_template('index6.html',message=message)
                    else:
                        for key1,value1 in value.items():
                            print(value1,email)
                            if value1 == email:
                                message='incorrect password'
                                return render_template('index6.html',message=message)
                            else:
                                firebase.post('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Users', input_data)
                                return render_template('index.html')
                
            except AttributeError:   
                firebase.post('https://inventory-management-9acd5-default-rtdb.firebaseio.com/Users', input_data)
                return render_template('index.html')

    return render_template('index.html')
    
    
    
if __name__ == '__main__':
    app.run()
