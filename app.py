from flask import Flask, request, redirect
app = Flask(__name__)

PRODUCTS = [
    {"id":1,"name":"iPhone 15 Pro Max 256GB","price":18500,"old":21000,"cat":"Electronics","img":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400","stock":15},
    {"id":2,"name":"Samsung Galaxy A54","price":4200,"old":4800,"cat":"Electronics","img":"https://images.unsplash.com/photo-1610945265064-0e34e03294be?w=400","stock":20},
    {"id":3,"name":"GTP African Print 6 Yards","price":450,"old":550,"cat":"Fashion","img":"https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=400","stock":100},
    {"id":4,"name":"5kg Lele Rice","price":180,"old":220,"cat":"Food","img":"https://images.unsplash.com/photo-1536304929831-ee1ca9d44906?w=400","stock":50},
    {"id":5,"name":"Infinix Hot 40 Pro","price":2200,"old":2600,"cat":"Electronics","img":"https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400","stock":30},
    {"id":6,"name":"Adidas Sneakers","price":650,"old":850,"cat":"Fashion","img":"https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400","stock":40},
    {"id":7,"name":"50 Inch Smart TV - Nasco","price":3800,"old":4500,"cat":"Electronics","img":"https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400","stock":10},
    {"id":8,"name":"Ghana Black Soap 1kg","price":80,"old":100,"cat":"Beauty","img":"https://images.unsplash.com/photo-1600857544200-b2f666a9a2ec?w=400","stock":200},
    {"id":9,"name":"MTN WiFi Router 4G","price":350,"old":450,"cat":"Electronics","img":"https://images.unsplash.com/photo-1588436706487-9d55d73a39e3?w=400","stock":35},
    {"id":10,"name":"Shea Butter 2kg","price":120,"old":150,"cat":"Beauty","img":"https://images.unsplash.com/photo-1571781926291-c477ebfd024b?w=400","stock":80},
    {"id":11,"name":"Football Jersey - Black Stars","price":180,"old":250,"cat":"Fashion","img":"https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400","stock":90},
    {"id":12,"name":"Deep Freezer 200L","price":2800,"old":3200,"cat":"Home","img":"https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400","stock":12},
]

def base_html(title, content):
    h = "<!DOCTYPE html><html><head><title>" + title + "</title>"
    h += '<meta name="viewport" content="width=device-width, initial-scale=1"><script src="https://cdn.tailwindcss.com"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"></head>'
    h += '<body class="bg-gray-100"><header class="bg-white shadow sticky top-0 z-50"><div class="bg-blue-700 text-white text-center py-1 text-xs">Free Delivery Accra over GHS 500 | 0302 123 456</div>'
    h += '<nav class="max-w-7xl mx-auto p-3 flex justify-between items-center"><a href="/" class="font-black text-xl text-blue-700">ToolMill<span class="text-orange-500">MALL</span>.GH</a><div class="flex gap-4 text-sm"><a href="/">Home</a><a href="/cart">Cart (<span id="cartcount">0</span>)</a><a href="/admin" class="bg-black text-white px-3 py-1 rounded-full">Admin</a></div></nav></header>'
    h += '<main class="max-w-7xl mx-auto p-3">' + content + '</main><footer class="bg-black text-white mt-10 p-6 text-center text-xs">ToolMillMALL.GH | pub-8472497143438792</footer>'
    h += """<script>let cart=JSON.parse(localStorage.getItem('tm_cart')||'[]');function updateCount(){let e=document.getElementById('cartcount');if(e)e.innerText=cart.length}function addToCart(id){let p=products.find(x=>x.id==id);cart.push(p);localStorage.setItem('tm_cart',JSON.stringify(cart));updateCount();alert(p.name+' added!')}updateCount();</script></body></html>"""
    return h

@app.route("/ads.txt")
def adstxt(): return "google.com, pub-8472497143438792, DIRECT, f08c47fec0942fa0", 200, {'Content-Type': 'text/plain'}

@app.route("/")
def home():
    js = str(PRODUCTS).replace("'", '"')
    grid = "<div class='bg-gradient-to-r from-blue-600 to-orange-500 text-white p-5 rounded-xl mb-4'><h1 class='text-2xl font-black'>GHANA BIGGEST MALL - REAL PHOTOS</h1></div><div class='grid grid-cols-2 md:grid-cols-4 gap-3'>"
    for p in PRODUCTS:
        grid += f"<div class='bg-white rounded-xl shadow overflow-hidden'><img src='{p['img']}' class='w-full h-40 object-cover'><div class='p-3'><h3 class='font-bold text-xs h-8 overflow-hidden'>{p['name']}</h3><p class='font-black text-blue-700 text-sm'>GHS {p['price']}</p><button onclick='addToCart({p['id']})' class='w-full mt-2 bg-orange-500 text-white py-2 rounded-full text-xs font-bold'>Add to Cart</button></div></div>"
    grid += f"</div><script>let products={js}</script>"
    return base_html("ToolMillMALL.GH", grid)

@app.route("/cart")
def cart():
    return base_html("Cart", """<h1 class='font-bold text-xl'>Cart</h1><div class='bg-white p-4 rounded shadow mt-4'><div id='cartlist'></div><p class='font-bold mt-4'>Total GHS <span id='total'>0</span></p><input placeholder='MoMo 024XXX' class='w-full mt-3 p-3 border rounded'><button onclick='alert("Order received!")' class='w-full mt-2 bg-green-600 text-white py-3 rounded-full'>Checkout MoMo</button></div><script>let cart=JSON.parse(localStorage.getItem('tm_cart')||'[]');let list=document.getElementById('cartlist');let t=0;if(cart.length==0)list.innerHTML='Empty';else cart.forEach(p=>{t+=p.price;list.innerHTML+='<div class="flex justify-between py-2 border-b text-sm"><span>'+p.name+'</span><b>GHS '+p.price+'</b></div>'});document.getElementById('total').innerText=t;</script>""")

@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method=="POST":
        if request.form.get("pwd")!="admin123": return base_html("Admin","Wrong pwd <a href='/admin'>Back</a>")
        name=request.form.get("name"); price=request.form.get("price"); cat=request.form.get("cat"); img=request.form.get("img")
        if name and price:
            nid=max([p['id'] for p in PRODUCTS])+1 if PRODUCTS else 1
            PRODUCTS.append({"id":nid,"name":name,"price":int(price),"old":int(price)+200,"cat":cat,"img":img,"stock":10})
            return redirect("/admin?ok=1&pwd=admin123")
    msg="<div class='bg-green-100 p-2 rounded mb-3'>Added!</div>" if request.args.get("ok") else ""
    rows="".join([f"<tr class='border-b text-xs'><td class='p-2'><img src='{p['img']}' class='w-8 h-8 object-cover'></td><td class='p-2'>{p['name'][:15]}</td><td class='p-2'>GHS {p['price']}</td><td class='p-2'><a href='/admin/delete/{p['id']}?pwd=admin123' class='text-red-600'>Del</a></td></tr>" for p in PRODUCTS[::-1]])
    html=f"<h1 class='font-black text-xl'>Admin - Real Photos</h1>{msg}<div class='grid md:grid-cols-2 gap-4 mt-4'><div class='bg-white p-4 rounded-xl shadow'><form method='POST' class='space-y-2'><input type='hidden' name='pwd' value='admin123'><input name='name' placeholder='Name' class='w-full p-2 border rounded' required><input name='price' type='number' placeholder='Price' class='w-full p-2 border rounded' required><select name='cat' class='w-full p-2 border rounded'><option>Electronics</option><option>Fashion</option><option>Food</option><option>Home</option><option>Beauty</option></select><input name='img' placeholder='Image URL https://...' class='w-full p-2 border rounded' required><button class='w-full bg-black text-white py-2 rounded-full'>Add Product</button></form></div><div class='bg-white p-4 rounded-xl shadow'><table class='w-full'>{rows}</table></div></div>"
    if not request.args.get("pwd") and request.method=="GET": html="<div class='bg-white p-4 rounded-xl shadow max-w-sm'><form method='POST'><input name='pwd' type='password' placeholder='Password admin123' class='w-full p-3 border rounded' required><button class='w-full mt-3 bg-black text-white py-2 rounded-full'>Login</button></form></div>"
    return base_html("Admin", html)

@app.route("/admin/delete/<int:pid>")
def adel(pid):
    if request.args.get("pwd")!="admin123": return "No"
    global PRODUCTS; PRODUCTS=[p for p in PRODUCTS if p['id']!=pid]; return redirect("/admin?pwd=admin123")

@app.route("/product/<int:pid>")
def prod(pid):
    p=next((x for x in PRODUCTS if x['id']==pid),None)
    js=str(PRODUCTS).replace("'",'"')
    return base_html(p['name'], f"<div class='bg-white p-4 rounded shadow grid md:grid-cols-2 gap-4'><img src='{p['img']}' class='w-full h-64 object-cover rounded'><div><h1 class='font-black text-xl'>{p['name']}</h1><p class='text-2xl font-black text-blue-700 mt-3'>GHS {p['price']}</p><button onclick='addToCart({p['id']})' class='w-full mt-5 bg-orange-500 text-white py-3 rounded-full font-bold'>Add to Cart</button></div></div><script>let products={js}</script>")

if __name__=="__main__": app.run(host="0.0.0.0", port=10000)
