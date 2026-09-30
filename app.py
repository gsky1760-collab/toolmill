from flask import Flask, request, redirect
import json, base64
app = Flask(__name__)
WHATSAPP_NUMBER = "233556023536"
PUB_ID = "pub-8472497143438792"

PRODUCTS = [
    {"id":1,"name":"iPhone 15 Pro Max 256GB","price":18500,"old":21000,"cat":"Electronics","img":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400","desc":"Brand new iPhone 15 Pro Max 256GB Titanium. Original US with warranty. 48MP camera, Face ID, fast delivery Accra."},
    {"id":2,"name":"Samsung Galaxy A54 5G 128GB","price":4200,"old":4800,"cat":"Electronics","img":"https://images.unsplash.com/photo-1610945265064-0e34e03294be?w=400","desc":"Samsung A54 5G AMOLED 120Hz display, 50MP camera, 5000mAh battery, 2 years warranty Ghana."},
    {"id":3,"name":"GTP African Print 6 Yards","price":450,"old":550,"cat":"Fashion","img":"https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=400","desc":"Original GTP African Print 6 yards 100 percent cotton, no fading, for funeral wedding church."},
    {"id":4,"name":"Lele Rice 5kg Premium","price":180,"old":220,"cat":"Food","img":"https://images.unsplash.com/photo-1536304929831-ee1ca9d44906?w=400","desc":"Lele 5kg premium long grain rice clean stone free best for Jollof and Fried Rice Ghana favorite."},
    {"id":5,"name":"Infinix Hot 40 Pro 256GB","price":2200,"old":2600,"cat":"Electronics","img":"https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400","desc":"Infinix Hot 40 Pro 256GB 8GB RAM 108MP camera Helio G99 5000mAh free pouch."},
    {"id":6,"name":"Adidas Sneakers White","price":650,"old":850,"cat":"Fashion","img":"https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400","desc":"Original Adidas white sneakers running casual comfortable breathable size 40 to 45."},
    {"id":7,"name":"Nasco 50 Inch Smart TV","price":3800,"old":4500,"cat":"Electronics","img":"https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400","desc":"Nasco 50 inch Smart TV UHD 4K Netflix YouTube HDMI USB 2 years warranty free bracket."},
    {"id":8,"name":"Ghana Black Soap 1kg","price":80,"old":100,"cat":"Beauty","img":"https://images.unsplash.com/photo-1600857544200-b2f666a9a2ec?w=400","desc":"Original Ghana black soap 1kg organic for skin glow acne dark spots natural made in Ghana."},
    {"id":9,"name":"Ladies Straight Dress Red","price":200,"old":300,"cat":"Fashion","img":"https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400","desc":"Ladies straight long dress red elegant for office church wedding free size M to XL quality."},
    {"id":10,"name":"Mens Sneakers Black Leather","price":350,"old":450,"cat":"Fashion","img":"https://images.unsplash.com/photo-1603808033587-9359428479d1?w=400","desc":"Classic mens black leather sneakers durable comfortable sizes 40 to 45 Accra shop."},
    {"id":11,"name":"Womens Handbag Luxury Brown","price":280,"old":350,"cat":"Fashion","img":"https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=400","desc":"Luxury womens handbag brown leather chain fits phone makeup wallet imported quality."},
    {"id":12,"name":"School Bag Backpack","price":220,"old":280,"cat":"Fashion","img":"https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400","desc":"Durable school bag backpack waterproof JHS SHS University laptop space many compartments."},
    {"id":13,"name":"Bluetooth Speaker JBL Bass","price":300,"old":400,"cat":"Electronics","img":"https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400","desc":"JBL Bluetooth speaker super bass 12 hours battery waterproof Bluetooth 5.0 clear sound."},
    {"id":14,"name":"Ladies Wig Human Hair 14 Inch","price":550,"old":700,"cat":"Beauty","img":"https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400","desc":"100 percent human hair wig 14 inch curly can be straightened dyed free wig cap soft natural."},
    {"id":15,"name":"Mens T-Shirt 3-Pack Cotton","price":150,"old":200,"cat":"Fashion","img":"https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400","desc":"3 pieces mens cotton T-shirts black white gray original cotton no fading sizes M to XXL."},
    {"id":16,"name":"Non-Stick Pot Set 6 Pcs","price":480,"old":600,"cat":"Home","img":"https://images.unsplash.com/photo-1585837070886-15dd8e8a54c5?w=400","desc":"6 pieces non stick pot set gas electric compatible easy clean does not stick cooking."},
    {"id":17,"name":"Perfume 100ml Long Lasting","price":120,"old":180,"cat":"Beauty","img":"https://images.unsplash.com/photo-1541643600914-78b084683601?w=400","desc":"100ml unisex perfume long lasting 24 hours nice fragrance men women Dubai imported."},
    {"id":18,"name":"Wireless Earbuds TWS Pro 6","price":180,"old":250,"cat":"Electronics","img":"https://images.unsplash.com/photo-1572569511254-d8f925fe2cbb?w=400","desc":"TWS Pro 6 wireless earbuds charging case 30 hours battery clear sound touch control."},
    {"id":19,"name":"Kids Sneakers Light Up 30-35","price":200,"old":260,"cat":"Fashion","img":"https://images.unsplash.com/photo-1514989940723-e8e51635b782?w=400","desc":"Kids light up sneakers size 30 to 35 beautiful colors comfortable school playing."},
    {"id":20,"name":"Gas Cooker 2 Burner","price":650,"old":800,"cat":"Home","img":"https://images.unsplash.com/photo-1556911220-bff31c812dba?w=400","desc":"2 burner gas cooker stainless steel auto ignition strong burner home outdoor cooking."},
    {"id":21,"name":"Makeup Kit 12 Colors","price":250,"old":320,"cat":"Beauty","img":"https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400","desc":"Professional makeup kit 12 colors eyeshadow lipstick powder beginners pros quality."},
    {"id":22,"name":"Office Chair Executive","price":950,"old":1200,"cat":"Home","img":"https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=400","desc":"Executive office chair leather adjustable height comfortable long hours imported."},
    {"id":23,"name":"Pen Drive 32GB SanDisk","price":90,"old":120,"cat":"Electronics","img":"https://images.unsplash.com/photo-1592899677977-9bb10ba128a5?w=400","desc":"SanDisk 32GB original pen drive high speed USB 3.0 phone laptop TV fast."},
    {"id":24,"name":"Bed Sheet 4x6 Cotton","price":180,"old":230,"cat":"Home","img":"https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?w=400","desc":"4x6 cotton bed sheet 2 pillow cases soft colorful no fading after washing quality."},
    {"id":25,"name":"Mens Watch Luxury Gold","price":400,"old":550,"cat":"Fashion","img":"https://images.unsplash.com/photo-1523170335258-f5ed11844a49?w=400","desc":"Luxury mens gold watch leather strap water resistant date display classy office."},
    {"id":26,"name":"Philips Steam Iron 2000W","price":320,"old":400,"cat":"Home","img":"https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400","desc":"Philips steam iron 2000W fast ironing non stick soleplate 2 years warranty original."},
    {"id":27,"name":"Ladies Slippers Soft","price":120,"old":160,"cat":"Fashion","img":"https://images.unsplash.com/photo-1603808033176-4a1c5d6a5a4a?w=400","desc":"Ladies soft slippers home outdoor comfortable sole many colors available Ghana."},
    {"id":28,"name":"Power Bank 20000mAh","price":250,"old":320,"cat":"Electronics","img":"https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=400","desc":"20000mAh power bank fast charge 4 phones LED display dual USB original quality."},
    {"id":29,"name":"Molfix Diapers Size 3 60pcs","price":180,"old":220,"cat":"Home","img":"https://images.unsplash.com/photo-1540479859555-17af45c78602?w=400","desc":"Molfix baby diapers size 3 6 to 10kg 60 pieces dry comfortable no leakage."},
    {"id":30,"name":"HP Laptop Core i5 8GB","price":4500,"old":5200,"cat":"Electronics","img":"https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400","desc":"HP Laptop 15 inch Core i5 8GB RAM 256GB SSD Windows 11 school office UK used neat."},
]

def base_html(title, body):
    return f"""<!DOCTYPE html><html><head><title>{title} - ToolMillMALL.GH</title><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="Ghana biggest online mall Electronics Fashion Food Beauty Home. Delivery Accra Kumasi. WhatsApp 0556023536"><script src="https://cdn.tailwindcss.com"></script></head><body class="bg-gray-100">
<header class="bg-white shadow sticky top-0 z-50"><div class="bg-blue-700 text-white text-center py-1 text-xs">Free Delivery Accra over GHS 500 | WhatsApp 0556023536 | Pay on Delivery</div>
<nav class="max-w-7xl mx-auto p-3 flex justify-between items-center"><a href="/" class="font-black text-xl text-blue-700">ToolMill<span class="text-orange-500">MALL</span>.GH</a><div class="flex gap-2 text-xs items-center"><a href="/">Home</a><a href="/about">About</a><a href="/contact">Contact</a><a href="/cart">Cart</a><a href="/admin?pwd=admin123" class="bg-black text-white px-3 py-1 rounded-full">Admin</a></div></nav></header>
<main class="max-w-7xl mx-auto p-3">{body}</main>
<footer class="bg-black text-white mt-10 p-6 text-center text-xs"><div class="flex justify-center gap-3 mb-3"><a href="/about">About</a><a href="/contact">Contact</a><a href="/privacy">Privacy</a><a href="/shipping">Shipping</a><a href="/terms">Terms</a></div><p>ToolMillMALL.GH Ghana trusted online marketplace since 2024. Location Accra Ghana. Email toolmillgh@gmail.com WhatsApp 0556023536. Delivery across Ghana Accra Kumasi Takoradi Tamale.</p><p class="mt-2">© 2026 ToolMillMALL.GH - All Rights Reserved</p></footer></body></html>"""

@app.route("/ads.txt")
def ads():
    return f"google.com, {PUB_ID}, DIRECT, f08c47fec0942fa0", 200, {'Content-Type':'text/plain'}

@app.route("/")
def home():
    json_products = json.dumps(PRODUCTS)
    cards = ""
    for p in PRODUCTS:
        cards += f"""<div class="bg-white rounded-xl shadow overflow-hidden"><a href="/product/{p['id']}"><img src="{p['img']}" class="w-full h-40 object-cover"></a><div class="p-3"><a href="/product/{p['id']}"><h3 class="font-bold text-xs h-10 overflow-hidden">{p['name']}</h3></a><p class="text-[10px] text-gray-500 h-8 overflow-hidden mt-1">{p['desc'][:65]}...</p><div class="flex gap-2 mt-1"><b class="text-blue-700 text-sm">GHS {p['price']}</b><span class="text-[10px] line-through text-gray-400">GHS {p['old']}</span></div><a href="/add/{p['id']}" class="mt-2 block text-center bg-orange-500 text-white py-2 rounded-full text-xs font-bold">Add to Cart</a></div></div>"""
    body = f"""<div class="bg-gradient-to-r from-blue-600 to-orange-500 text-white p-6 rounded-xl mb-4"><h1 class="text-2xl font-black">GHANA BIGGEST ONLINE MALL</h1><p class="text-sm mt-2">30 Original Products | Pay on Delivery | 0556023536</p><p class="text-xs mt-1">Accra Kumasi Takoradi Tamale - Same Day Delivery Accra</p></div><div class="grid grid-cols-2 md:grid-cols-4 gap-3">{cards}</div>
    <div class="bg-white p-5 rounded-xl mt-6 text-sm leading-7"><h2 class="font-black text-lg">Why Shop from ToolMillMALL.GH in Ghana?</h2><p class="mt-3">ToolMillMALL.GH is your one-stop online shopping destination in Ghana founded 2024 in Accra. We provide over 30 original products across Electronics, Fashion, Food, Beauty, Home Appliances. All products come with warranty and you can pay on delivery with Cash or Mobile Money MTN MoMo Vodafone Cash. Delivery team covers Accra, Kumasi, Takoradi, Cape Coast, Tamale within 24 to 72 hours. Customer service on WhatsApp 0556023536 Mon-Sat 8am-6pm. Free delivery Accra over GHS 500 and 7 days return for defective items. Trusted by 1000+ Ghanaians. Our mission is to make online shopping easy safe fast for every Ghanaian.</p></div>
    <script>let products={json_products}; localStorage.setItem('tm_products', JSON.stringify(products));</script>"""
    return base_html("Home", body)

@app.route("/product/<int:pid>")
def product_detail(pid):
    p = next((x for x in PRODUCTS if x["id"]==pid), None)
    if not p:
        return redirect("/")
    body = f"""<div class="bg-white rounded-xl shadow p-4 md:flex gap-6"><img src="{p['img']}" class="w-full md:w-1/2 h-80 object-cover rounded-xl"><div class="md:w-1/2 mt-4"><h1 class="font-black text-xl">{p['name']}</h1><p class="text-xs text-gray-500 mt-1">{p['cat']} | In Stock | Ghana</p><div class="flex gap-2 mt-3 items-center"><b class="text-2xl text-blue-700">GHS {p['price']}</b><span class="line-through text-gray-400">GHS {p['old']}</span><span class="bg-red-500 text-white text-xs px-2 py-1 rounded">-{int((1-p['price']/p['old'])*100)}% OFF</span></div><p class="text-sm leading-7 mt-4">{p['desc']} This product is 100 percent original from ToolMillMALL.GH. We offer warranty, fast delivery, and pay on delivery. Suitable for personal use or gift. High quality, durable, tested. Delivery to Accra Kumasi and all Ghana. Order now via WhatsApp 0556023536.</p><p class="text-xs text-gray-600 mt-4">✅ Pay on Delivery<br>✅ Free delivery Accra over GHS 500<br>✅ 7 days return policy<br>✅ WhatsApp Support 0556023536</p><a href="/add/{p['id']}" class="mt-6 block text-center bg-orange-500 text-white py-3 rounded-full font-bold">Add to Cart & Order on WhatsApp</a><a href="/" class="mt-3 block text-center bg-gray-200 py-2 rounded-full text-sm">Continue Shopping</a></div></div>"""
    return base_html(p["name"], body)

@app.route("/add/<int:pid>")
def add_cart(pid):
    prod_json = json.dumps(PRODUCTS)
    return f"""<script>let products={prod_json};let cart=JSON.parse(localStorage.getItem('tm_cart')||'[]');let p=products.find(x=>x.id=={pid});if(p){{cart.push(p);localStorage.setItem('tm_cart',JSON.stringify(cart));alert(p.name+' added!');}}window.location='/cart';</script>"""

@app.route("/cart")
def cart():
    body = """<h1 class="font-bold text-xl">Your Cart - Pay on Delivery Ghana</h1><div id="list" class="bg-white p-4 rounded-xl mt-4"></div><div class="bg-white p-4 rounded-xl mt-4"><h2 class="font-bold mb-2">Delivery Details</h2><input id="n" placeholder="Your Full Name" class="w-full p-3 border rounded mb-2"><input id="m" placeholder="MoMo Number 024XXXXXXX" class="w-full p-3 border rounded mb-2"><input id="a" placeholder="Delivery Address Madina Accra" class="w-full p-3 border rounded mb-2"><button onclick="sendWA()" class="w-full bg-green-600 text-white py-3 rounded-full font-bold">Order via WhatsApp 0556023536</button><p class="text-xs text-gray-500 mt-2 text-center">We call you to confirm before delivery</p></div>
    <script>let cart=JSON.parse(localStorage.getItem('tm_cart')||'[]');let el=document.getElementById('list');let tot=0;if(cart.length==0){el.innerHTML='Cart Empty - Add products from Home';}else{el.innerHTML='';cart.forEach((p,i)=>{tot+=p.price;el.innerHTML+='<div class="flex justify-between py-2 border-b text-sm"><span>'+(i+1)+'. '+p.name+'</span><b>GHS '+p.price+'</b></div>'});el.innerHTML+='<div class="font-black pt-3 text-lg">Total: GHS '+tot+' + Delivery</div>';}
    function sendWA(){let name=document.getElementById('n').value;let momo=document.getElementById('m').value;let addr=document.getElementById('a').value;if(!name||!momo){alert('Enter name and MoMo');return;}let msg='*NEW ORDER ToolMillMALL*%0AName: '+name+'%0AMoMo: '+momo+'%0AAddr: '+addr+'%0A%0AProducts:%0A';let tot=0;cart.forEach(p=>{tot+=p.price;msg+='- '+p.name+' GHS '+p.price+'%0A';});msg+='%0ATOTAL: GHS '+tot;window.open('https://wa.me/233556023
