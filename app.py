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
]
def base_html(title, content):
    h = f"<!DOCTYPE html><html><head><title>{title}</title><meta name='viewport' content='width=device-width, initial-scale=1'><script src='https://cdn.tailwindcss.com'></script><link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css'></head>"
    h += '<body class="bg-gray-100"><header class="bg-white shadow sticky top-0 z-50"><div class="bg-blue-700 text-white text-center py-1 text-xs">Free Delivery Accra over GHS 500</div>'
    h += '<nav class="max-w-7xl mx-auto p-3 flex justify-between items-center"><a href="/" class="font-black text-xl text-blue-700">ToolMill<span class="text-orange-500">MALL</span>.GH</a><div class="flex gap-3 text-sm items-center"><a href="/">Home</a><a href="/cart">Cart (<span id="cartcount">0</span>)</a><a href="/admin" class="bg-black text-white px-3 py-1 rounded-full">Admin</a></div></nav></header>'
    h += f'<main class="max-w-7xl mx-auto p-3">{content}</main><footer class="bg-black text-white mt-10 p-6 text-center text-xs">© 2026 ToolMillMALL.GH</footer>'
    h += """<script>let cart=JSON.parse(localStorage.getItem('tm_cart')||'[]');function updateCount(){let e=document.getElementById('cartcount');if(e)e.innerText=cart.length}function addToCart(id){let p=products.find(x=>x.id==id);cart.push(p);localStorage.setItem('tm_cart',JSON.stringify(cart));updateCount();alert(p.name+' added!');}updateCount();</script></body></html>"""
    return h
@app.route("/ads.txt")
def ads(): return "google.com, pub-8472497143438792, DIRECT, f08c47fec0942fa0", 200, {'Content-Type':'text/plain'}
@app.route("/")
def home():
    js = str(PRODUCTS).replace("'", '"')
    grid = "<div class='bg-gradient-to-r from-blue-600 to-orange-500 text-white p-5 rounded-xl mb-4'><h1 class='text-2xl font-black'>GHANA'S BIGGEST MALL</h1></div><div class='grid grid-cols-2 md:grid-cols-4 gap-3'>"
    for p in PRODUCTS:
        disc = int((1-p['price']/p['old'])*100) if p['old']>0 else 0
        grid += f"<div class='bg-white rounded-xl shadow overflow-hidden'><img src='{p['img']}' class='w-full h-40 object-cover'><div class='p-3'><h3 class='font-bold text-xs h-8 overflow-hidden'>{p['name']}</h3><div class='flex gap-1 mt-2 items-center'><b class='text-blue-700 text-sm'>GHS {p['price']}</b><span class='text-[10px] line-through text-gray-400'>GHS {p['old']}</span></div><button onclick='addToCart({p['id']})' class='w-full mt-2 bg-orange-500 text-white py-2 rounded-full text-xs font-bold'>Add to Cart</button></div></div>"
    grid += f"</div><script>let products={js}</script>"
    return base_html("ToolMillMALL.GH", grid)
@app.route("/cart")
def cart_page():
    html = f"""
    <h1 class='text-xl font-bold'>Your Cart</h1>
    <div class='bg-white rounded-xl shadow p-4 mt-4'><div id='cartlist'></div>
    <div class='mt-6 border-t pt-4'><p class='font-black text-xl'>Total: GHS <span id='total'>0</span></p>
    <input id='custname' placeholder='Your Name' class='w-full mt-3 p-3 border rounded'>
    <input id='custmomo' placeholder='MoMo 024XXXXXXX' class='w-full mt-2 p-3 border rounded'>
    <input id='custaddr' placeholder='Delivery Address' class='w-full mt-2 p-3 border rounded'>
    <button onclick='checkoutWA()' class='w-full mt-4 bg-green-600 text-white py-3 rounded-full font-bold'>Order via WhatsApp</button>
    <button onclick='localStorage.clear();location.reload()' class='w-full mt-3 bg-gray-200 py-2 rounded-full text-sm'>Clear Cart</button>
    </div></div>
    <script>
    let cart=JSON.parse(localStorage.getItem('tm_cart')||'[]');let list=document.getElementById('cartlist');let total=0;
    if(cart.length==0){{list.innerHTML='<p>Cart empty</p>';}}else{{cart.forEach(p=>{{total+=p.price; list.innerHTML+='<div class="flex justify-between py-2 border-b text-sm"><span>'+p.name+'</span><b>GHS '+p.price+'</b></div>';}});}}
    document.getElementById('total').innerText=total;
    function checkoutWA(){{let name=document.getElementById('custname').value;let momo=document.getElementById('custmomo').value;let addr=document.getElementById('custaddr').value;if(cart.length==0){{alert('Cart empty');return;}}let msg='*NEW ORDER*%0AName: '+name+'%0AMoMo: '+momo+'%0AAddr: '+addr+'%0A';cart.forEach(p=>{{msg+='- '+p.name+' GHS '+p.price+'%0A';}});msg+='TOTAL: GHS '+total;window.open('https://wa.me/{WHATSAPP_NUMBER}?text='+msg,'_blank');}}
    </script>
    """
    return base_html("Cart", html)
@app.route("/admin/delete/<int:pid>")
def delete_product(pid):
    pwd = request.args.get("pwd")
    if pwd!= "admin123":
        return "Wrong password"
    global PRODUCTS
    PRODUCTS = [p for p in PRODUCTS if p['id']!= pid]
    return redirect(f"/admin?pwd=admin123")
@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method=="POST":
        if request.form.get("pwd")!="admin123": return base_html("Admin","Wrong password")
        name=request.form.get("name"); price=request.form.get("price"); old=request.form.get("old"); cat=request.form.get("cat"); img=request.form.get("img_url")
        file = request.files.get('file')
        if file and file.filename!='':
            data = file.read()
            b64 = base64.b64encode(data).decode('utf-8')
            mime = file.mimetype or 'image/jpeg'
            img = f"data:{mime};base64,{b64}"
        if name and price:
            nid=max([p['id'] for p in PRODUCTS])+1 if PRODUCTS else 1
            PRODUCTS.append({"id":nid,"name":name,"price":int(price),"old":int(old) if old else int(price)+300,"cat":cat,"img":img if img else "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400","stock":20})
            return redirect("/admin?ok=1&pwd=admin123")
    ok=request.args.get("ok")
    msg="<div class='bg-green-100 p-3 rounded mb-3'>✅ Added!</div>" if ok else ""
    rows="".join([f"<tr class='border-b text-xs'><td class='p-2'><img src='{p['img']}' class='w-10 h-10 object-cover'></td><td class='p-2'>{p['name
