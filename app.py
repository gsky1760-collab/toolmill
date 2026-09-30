from flask import Flask, request, redirect
import base64
app = Flask(__name__)
WHATSAPP_NUMBER = "233556023536"
PRODUCTS = [
    {"id":1,"name":"iPhone 15 Pro Max 256GB","price":18500,"old":21000,"cat":"Electronics","img":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400","stock":15},
    {"id":2,"name":"Samsung Galaxy A54","price":4200,"old":4800,"cat":"Electronics","img":"https://images.unsplash.com/photo-1610945265064-0e34e03294be?w=400","stock":20},
    {"id":3,"name":"GTP African Print 6 Yards","price":450,"old":550,"cat":"Fashion","img":"https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=400","stock":100},
    {"id":4,"name":"5kg Lele Rice","price":180,"old":220,"cat":"Food","img":"https://images.unsplash.com/photo-1536304929831-ee1ca9d44906?w=400","stock":50},
    {"id":5,"name":"Infinix Hot 40 Pro","price":2200,"old":2600,"cat":"Electronics","img":"https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400","stock":30},
    {"id":6,"name":"Adidas Sneakers","price":650,"old":850,"cat":"Fashion","img":"https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400","stock":40},
    {"id":7,"name":"Nasco 50 Inch Smart TV","price":3800,"old":4500,"cat":"Electronics","img":"https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400","stock":10},
    {"id":8,"name":"Ghana Black Soap 1kg","price":80,"old":100,"cat":"Beauty","img":"https://images.unsplash.com/photo-1600857544200-b2f666a9a2ec?w=400","stock":200},
    {"id":9,"name":"Straight dress","price":200,"old":300,"cat":"Fashion","img":"https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400","stock":20},
]

def base_html(title, content):
    html = "<!DOCTYPE html><html><head><title>"+title+"</title><meta name='viewport' content='width=device-width, initial-scale=1'><script src='https://cdn.tailwindcss.com'></script></head><body class='bg-gray-100'>"
    html += "<header class='bg-white shadow sticky top-0 z-50'><div class='bg-blue-700 text-white text-center py-1 text-xs'>Free Delivery Accra over GHS 500</div>"
    html += "<nav class='max-w-7xl mx-auto p-3 flex justify-between items-center'><a href='/' class='font-black text-xl text-blue-700'>ToolMill<span class='text-orange-500'>MALL</span>.GH</a><div class='flex gap-3 text-sm'><a href='/'>Home</a><a href='/cart'>Cart</a><a href='/admin?pwd=admin123' class='bg-black text-white px-3 py-1 rounded-full'>Admin</a></div></nav></header>"
    html += "<main class='max-w-7xl mx-auto p-3'>"+content+"</main></body></html>"
    return html

@app.route("/ads.txt")
def ads():
    return "google.com, pub-8472497143438792, DIRECT, f08c47fec0942fa0", 200, {'Content-Type':'text/plain'}

@app.route("/")
def home():
    grid = "<div class='bg-gradient-to-r from-blue-600 to-orange-500 text-white p-5 rounded-xl mb-4'><h1 class='text-2xl font-black'>GHANA'S BIGGEST MALL</h1></div><div class='grid grid-cols-2 md:grid-cols-4 gap-3'>"
    for p in PRODUCTS:
        grid += "<div class='bg-white rounded-xl shadow overflow-hidden'><img src='"+p['img']+"' class='w-full h-40 object-cover'><div class='p-3'><h3 class='font-bold text-xs'>"+p['name']+"</h3><b class='text-blue-700 text-sm'>GHS "+str(p['price'])+"</b><br><a href='/add/"+str(p['id'])+"' class='mt-2 inline-block bg-orange-500 text-white px-4 py-1 rounded-full text-xs'>Add to Cart</a></div></div>"
    grid += "</div>"
    return base_html("ToolMillMALL", grid)

@app.route("/add/<int:pid>")
def add_cart(pid):
    return "<script>let cart=JSON.parse(localStorage.getItem('tm_cart')||'[]');let products="+str(PRODUCTS).replace("'","\"")+";let p=products.find(x=>x.id=="+str(pid)+");cart.push(p);localStorage.setItem('tm_cart',JSON.stringify(cart));alert(p.name+' added!');window.location='/';</script>"

@app.route("/cart")
def cart_page():
    html = """
    <h1 class='font-bold'>Your Cart</h1><div id='list' class='bg-white p-4 rounded-xl mt-4'></div>
    <div class='bg-white p-4 rounded-xl mt-4'><input id='n' placeholder='Your Name' class='w-full p-3 border rounded mb-2'><input id='m' placeholder='MoMo Number' class='w-full p-3 border rounded mb-2'><input id='a' placeholder='Address' class='w-full p-3 border rounded mb-2'><button onclick='sendWA()' class='w-full bg-green-600 text-white py-3 rounded-full'>Order via WhatsApp to 0556023536</button></div>
    <script>
    let cart=JSON.parse(localStorage.getItem('tm_cart')||'[]');let el=document.getElementById('list');let tot=0;el.innerHTML='';if(cart.length==0){el.innerHTML='Empty'}else{cart.forEach(p=>{tot+=p.price;el.innerHTML+='<div>'+p.name+' - GHS '+p.price+'</div>'});el.innerHTML+='<b>Total: GHS '+tot+'</b>';}
    function sendWA(){let name=document.getElementById('n').value;let momo=document.getElementById('m').value;let addr=document.getElementById('a').value;let msg='*NEW ORDER*%0AName: '+name+'%0AMoMo: '+momo+'%0AAddr: '+addr+'%0A';cart.forEach(p=>{msg+='- '+p.name+'%0A'});window.open('https://wa.me/233556023536?text='+msg,'_blank');}
    </script>
    """
    return base_html("Cart", html)

@app.route("/admin/delete/<int:pid>")
def delete_prod(pid):
    if request.args.get("pwd") != "admin123":
        return "Wrong pwd"
    global PRODUCTS
    PRODUCTS = [p for p in PRODUCTS if p["id"] != pid]
    return redirect("/admin?pwd=admin123")

@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method=="POST":
        if request.form.get("pwd")!="admin123":
            return "Wrong password"
        name=request.form.get("name")
        price=request.form.get("price")
        cat=request.form.get("cat")
        img=request.form.get("img_url")
        file=request.files.get("file")
        if file and file.filename!="":
            data=file.read()
            b64=base64.b64encode(data).decode("utf-8")
            mime=file.mimetype or "image/jpeg"
            img="data:"+mime+";base64,"+b64
        if name and price:
            nid=max([p["id"] for p in PRODUCTS])+1 if PRODUCTS else 1
            PRODUCTS.append({"id":nid,"name":name,"price":int(price),"old":int(price)+100,"cat":cat,"img":img,"stock":20})
        return redirect("/admin?pwd=admin123&ok=1")
    ok=request.args.get("ok")
    msg="<div class='bg-green-100 p-2 rounded mb-2'>Added!</div>" if ok else ""
    rows=""
    for p in PRODUCTS[::-1]:
        rows+="<tr class='border-b text-xs'><td class='p-2'><img src='"+p["img"]+"' class='w-10 h-10'></td><td class='p-2'>"+p["name"][:20]+"</td><td class='p-2'>GHS "+str(p["price"])+"</td><td class='p-2'><a href='/admin/delete/"+str(p["id"])+"?pwd=admin123' class='bg-red-500 text-white px-2 py-1 rounded'>Delete</a></td></tr>"
    html=msg+"<h1 class='font-bold'>Admin - "+str(len(PRODUCTS))+" Products</h1><div class='bg-white p-4 rounded-xl mt-4'><form method='POST' enctype='multipart/form-data'><input type='hidden' name='pwd' value='admin123'><input name='name' placeholder='Name' class='w-full p-2 border rounded mb-2' required><input name='price' placeholder='Price' type='number' class='w-full p-2 border rounded mb-2' required><select name='cat' class='w-full p-2 border rounded mb-2'><option>Fashion</option><option>Electronics</option><option>Food</option><option>Beauty</option></select><input type='file' name='file' class='w-full mb-2'><input name='img_url' placeholder='OR paste image URL' class='w-full p-2 border rounded mb-2'><button class='w-full bg-black text-white py-2 rounded-full'>Add Product</button></form></div><div class='bg-white p-4 rounded-xl mt-4'><table class='w-full'>"+rows+"</table></div>"
    if not request.args.get("pwd"):
        html="<form method='POST'><input name='pwd' type='password' placeholder='admin123' class='w-full p-3 border rounded'><button class='w-full mt-2 bg-black text-white py-2 rounded'>Login</button></form>"
    return base_html("Admin", html)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=10000)
