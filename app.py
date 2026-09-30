from flask import Flask, request, redirect
import os, json, base64
app = Flask(__name__)

WHATSAPP = "233556023536"
PUB = "pub-8472497143438792"

PRODUCTS = [
  {"id":1,"name":"iPhone 15 Pro Max 256GB","price":18500,"old":21000,"cat":"Electronics","img":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400","desc":"Brand new iPhone 15 Pro Max 256GB Titanium original US warranty 48MP camera."},
  {"id":2,"name":"Samsung Galaxy A54 5G","price":4200,"old":4800,"cat":"Electronics","img":"https://images.unsplash.com/photo-1610945265064-0e34e03294be?w=400","desc":"Samsung A54 AMOLED 120Hz 50MP camera 5000mAh battery 2 years warranty."},
  {"id":3,"name":"GTP African Print 6 Yards","price":450,"old":550,"cat":"Fashion","img":"https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=400","desc":"Original GTP 6 yards 100 percent cotton no fading for funeral wedding."},
  {"id":4,"name":"Lele Rice 5kg Premium","price":180,"old":220,"cat":"Food","img":"https://images.unsplash.com/photo-1536304929831-ee1ca9d44906?w=400","desc":"Lele 5kg premium long grain rice clean stone free Ghana favorite."},
  {"id":5,"name":"Infinix Hot 40 Pro 256GB","price":2200,"old":2600,"cat":"Electronics","img":"https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400","desc":"Infinix Hot 40 Pro 256GB 8GB RAM 108MP camera 5000mAh battery."},
  {"id":6,"name":"Adidas Sneakers White","price":650,"old":850,"cat":"Fashion","img":"https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400","desc":"Original Adidas white sneakers comfortable breathable size 40 to 45."},
  {"id":7,"name":"Nasco 50 Inch Smart TV","price":3800,"old":4500,"cat":"Electronics","img":"https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400","desc":"Nasco 50 inch Smart TV UHD 4K Netflix YouTube 2 years warranty."},
  {"id":8,"name":"Ghana Black Soap 1kg","price":80,"old":100,"cat":"Beauty","img":"https://images.unsplash.com/photo-1600857544200-b2f666a9a2ec?w=400","desc":"Original Ghana black soap organic for skin glow acne natural."},
  {"id":9,"name":"Ladies Straight Dress Red","price":200,"old":300,"cat":"Fashion","img":"https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400","desc":"Ladies straight long dress red elegant office church wedding free size."},
  {"id":10,"name":"Mens Sneakers Black","price":350,"old":450,"cat":"Fashion","img":"https://images.unsplash.com/photo-1603808033587-9359428479d1?w=400","desc":"Classic mens black leather sneakers durable comfortable sizes 40-45."},
  {"id":11,"name":"Womens Handbag Brown","price":280,"old":350,"cat":"Fashion","img":"https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=400","desc":"Luxury womens handbag brown leather chain phone wallet imported."},
  {"id":12,"name":"School Bag Backpack","price":220,"old":280,"cat":"Fashion","img":"https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400","desc":"Durable school bag backpack waterproof JHS SHS University laptop space."},
  {"id":13,"name":"Bluetooth Speaker JBL","price":300,"old":400,"cat":"Electronics","img":"https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400","desc":"JBL Bluetooth speaker super bass 12 hours battery waterproof."},
  {"id":14,"name":"Ladies Wig 14 Inch","price":550,"old":700,"cat":"Beauty","img":"https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400","desc":"100 percent human hair wig 14 inch curly can be straightened dyed."},
  {"id":15,"name":"Mens T-Shirt 3-Pack","price":150,"old":200,"cat":"Fashion","img":"https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400","desc":"3 pieces mens cotton T-shirts black white gray original cotton."},
  {"id":16,"name":"Non-Stick Pot Set 6 Pcs","price":480,"old":600,"cat":"Home","img":"https://images.unsplash.com/photo-1585837070886-15dd8e8a54c5?w=400","desc":"6 pieces non stick pot set gas electric easy clean does not stick."},
  {"id":17,"name":"Perfume 100ml Unisex","price":120,"old":180,"cat":"Beauty","img":"https://images.unsplash.com/photo-1541643600914-78b084683601?w=400","desc":"100ml unisex perfume long lasting 24 hours Dubai imported nice."},
  {"id":18,"name":"Wireless Earbuds TWS","price":180,"old":250,"cat":"Electronics","img":"https://images.unsplash.com/photo-1572569511254-d8f925fe2cbb?w=400","desc":"TWS Pro 6 wireless earbuds charging case 30 hours battery."},
  {"id":19,"name":"Kids Sneakers 30-35","price":200,"old":260,"cat":"Fashion","img":"https://images.unsplash.com/photo-1514989940723-e8e51635b782?w=400","desc":"Kids light up sneakers size 30 to 35 beautiful colors comfortable."},
  {"id":20,"name":"Gas Cooker 2 Burner","price":650,"old":800,"cat":"Home","img":"https://images.unsplash.com/photo-1556911220-bff31c812dba?w=400","desc":"2 burner gas cooker stainless steel auto ignition strong burner."},
  {"id":21,"name":"Makeup Kit 12 Colors","price":250,"old":320,"cat":"Beauty","img":"https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400","desc":"Professional makeup kit 12 colors eyeshadow lipstick powder quality."},
  {"id":22,"name":"Office Chair Executive","price":950,"old":1200,"cat":"Home","img":"https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=400","desc":"Executive office chair leather adjustable height comfortable long hours."},
  {"id":23,"name":"Pen Drive 32GB SanDisk","price":90,"old":120,"cat":"Electronics","img":"https://images.unsplash.com/photo-1592899677977-9bb10ba128a5?w=400","desc":"SanDisk 32GB original pen drive high speed USB 3.0 phone laptop."},
  {"id":24,"name":"Bed Sheet 4x6 Cotton","price":180,"old":230,"cat":"Home","img":"https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?w=400","desc":"4x6 cotton bed sheet 2 pillow cases soft colorful no fading."},
  {"id":25,"name":"Mens Watch Gold","price":400,"old":550,"cat":"Fashion","img":"https://images.unsplash.com/photo-1523170335258-f5ed11844a49?w=400","desc":"Luxury mens gold watch leather strap water resistant date display."},
  {"id":26,"name":"Philips Steam Iron","price":320,"old":400,"cat":"Home","img":"https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400","desc":"Philips steam iron 2000W fast ironing non stick soleplate warranty."},
  {"id":27,"name":"Power Bank 20000mAh","price":250,"old":320,"cat":"Electronics","img":"https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=400","desc":"20000mAh power bank fast charge 4 phones LED display dual USB."},
  {"id":28,"name":"Molfix Diapers Size 3","price":180,"old":220,"cat":"Home","img":"https://images.unsplash.com/photo-1540479859555-17af45c78602?w=400","desc":"Molfix baby diapers size 3 6-10kg 60 pieces dry comfortable."},
  {"id":29,"name":"HP Laptop Core i5","price":4500,"old":5200,"cat":"Electronics","img":"https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400","desc":"HP Laptop 15 inch Core i5 8GB RAM 256GB SSD Windows 11 UK used neat."},
  {"id":30,"name":"Electric Kettle 1.5L","price":150,"old":200,"cat":"Home","img":"https://images.unsplash.com/photo-1585837070886-15dd8e8a54c5?w=400","desc":"Electric kettle 1.5L fast boiling auto cut stainless steel."},
]

def page(title, body):
    return f'<html><head><title>{title} - ToolMillMALL.GH</title><meta name="viewport" content="width=device-width, initial-scale=1"><script src="https://cdn.tailwindcss.com"></script></head><body class="bg-gray-100"><header class="bg-white shadow sticky top-0 z-50"><div class="bg-blue-700 text-white text-center py-1 text-xs">Free Delivery Accra over 500 | WhatsApp 0556023536</div><nav class="max-w-7xl mx-auto p-3 flex justify-between"><a href="/" class="font-black text-xl text-blue-700">ToolMill<span class="text-orange-500">MALL</span>.GH</a><div class="flex gap-2 text-xs"><a href="/">Home</a><a href="/about">About</a><a href="/contact">Contact</a><a href="/cart">Cart</a><a href="/admin?pwd=admin123" class="bg-black text-white px-3 py-1 rounded-full">Admin</a></div></nav></header><main class="max-w-7xl mx-auto p-3">{body}</main><footer class="bg-black text-white mt-10 p-6 text-center text-xs"><a href="/about" class="mx-2">About</a><a href="/contact" class="mx-2">Contact</a><a href="/privacy" class="mx-2">Privacy</a><a href="/shipping" class="mx-2">Shipping</a><a href="/terms" class="mx-2">Terms</a><p class="mt-3">ToolMillMALL.GH Ghana trusted mall since 2024. Accra Ghana. 0556023536 toolmillgh@gmail.com Delivery Accra Kumasi Takoradi Tamale.</p><p class="mt-2">© 2026 ToolMillMALL.GH</p></footer></body></html>'

@app.route("/ads.txt")
def ads_txt():
    return f"google.com, {PUB}, DIRECT, f08c47fec0942fa0", 200, {"Content-Type":"text/plain"}

@app.route("/")
def home():
    cards = ""
    for p in PRODUCTS:
        cards += f'<div class="bg-white rounded-xl shadow overflow-hidden"><a href="/product/{p["id"]}"><img src="{p["img"]}" class="w-full h-40 object-cover"></a><div class="p-3"><a href="/product/{p["id"]}"><h3 class="font-bold text-xs h-10 overflow-hidden">{p["name"]}</h3></a><p class="text-[10px] text-gray-500 h-8 overflow-hidden mt-1">{p["desc"]}</p><div class="mt-1"><b class="text-blue-700 text-sm">GHS {p["price"]}</b> <span class="line-through text-[10px] text-gray-400">GHS {p["old"]}</span></div><a href="/add/{p["id"]}" class="mt-2 block text-center bg-orange-500 text-white py-2 rounded-full text-xs font-bold">Add to Cart</a></div></div>'
    body = f'<div class="bg-gradient-to-r from-blue-600 to-orange-500 text-white p-6 rounded-xl mb-4"><h1 class="text-2xl font-black">GHANA BIGGEST ONLINE MALL - 30 PRODUCTS</h1><p class="text-sm mt-2">Original Products Pay on Delivery WhatsApp 0556023536</p></div><div class="grid grid-cols-2 md:grid-cols-4 gap-3">{cards}</div><div class="bg-white p-5 rounded-xl mt-6 text-sm leading-7"><h2 class="font-black">Why Shop ToolMillMALL.GH?</h2><p class="mt-2">ToolMillMALL.GH founded 2024 in Accra Greater Accra Ghana. We sell over 30 original products Electronics Fashion Food Beauty Home Appliances. Brands iPhone Samsung Infinix Nasco Adidas GTP Lele. All products with warranty. Pay on Delivery Cash Mobile Money MTN MoMo Vodafone Cash. Delivery Accra same day 1-2 days, Kumasi Takoradi Tamale 2-4 days. Free delivery Accra over GHS 500. 7 days return defective items. Customer support WhatsApp 0556023536 Mon-Sat 8am-6pm. Trusted by 1000+ Ghanaians. Mission make online shopping easy safe fast for every Ghanaian. Contact Accra Ghana toolmillgh@gmail.com 0556023536.</p></div>'
    return page("Home", body)

@app.route("/product/<int:pid>")
def prod(pid):
    p = next((x for x in PRODUCTS if x["id"]==pid), None)
    if not p: return redirect("/")
    b = f'<div class="bg-white rounded-xl p-4 md:flex gap-6"><img src="{p["img"]}" class="w-full md:w-1/2 h-80 object-cover rounded-xl"><div class="md:w-1/2 mt-4"><h1 class="font-black text-xl">{p["name"]}</h1><p class="text-xs text-gray-500 mt-1">{p["cat"]} In Stock</p><div class="flex gap-2 mt-3"><b class="text-2xl text-blue-700">GHS {p["price"]}</b><span class="line-through text-gray-400">GHS {p["old"]}</span></div><p class="text-sm leading-7 mt-4">{p["desc"]} 100 percent original from ToolMillMALL.GH with warranty fast delivery pay on delivery suitable for personal use or gift high quality durable tested delivery to Accra Kumasi all Ghana. Order now via WhatsApp 0556023536.</p><a href="/add/{p["id"]}" class="mt-6 block text-center bg-orange-500 text-white py-3 rounded-full font-bold">Add to Cart</a><a href="/" class="mt-3 block text-center bg-gray-200 py-2 rounded-full text-sm">Continue Shopping</a></div></div>'
    return page(p["name"], b)

@app.route("/add/<int:pid>")
def add(pid):
    j = json.dumps(PRODUCTS)
    return f'<script>let prods={j};let cart=JSON.parse(localStorage.getItem("tm_cart")||"[]");let p=prods.find(x=>x.id=={pid});cart.push(p);localStorage.setItem("tm_cart",JSON.stringify(cart));alert(p.name+" added");location="/cart";</script>'

@app.route("/cart")
def cart():
    b = '<h1 class="font-bold text-xl">Your Cart - Pay on Delivery</h1><div id="list" class="bg-white p-4 rounded-xl mt-4"></div><div class="bg-white p-4 rounded-xl mt-4"><input id="n" placeholder="Full Name" class="w-full p-3 border rounded mb-2"><input id="m" placeholder="MoMo 024XXXXXXX" class="w-full p-3 border rounded mb-2"><input id="a" placeholder="Address Madina Accra" class="w-full p-3 border rounded mb-2"><button onclick="sendWA()" class="w-full bg-green-600 text-white py-3 rounded-full font-bold">Order WhatsApp 0556023536</button></div><script>let cart=JSON.parse(localStorage.getItem("tm_cart")||"[]");let el=document.getElementById("list");let tot=0;if(cart.length==0){el.innerHTML="Cart Empty";}else{el.innerHTML="";cart.forEach((p,i)=>{tot+=p.price;el.innerHTML+="<div class=\\"flex justify-between py-2 border-b text-sm\\"><span>"+(i+1)+". "+p.name+"</span><b>GHS "+p.price+"</b></div>"});el.innerHTML+="<div class=\\"font-black pt-3\\">Total GHS "+tot+"</div>";}function sendWA(){let name=document.getElementById("n").value;let momo=document.getElementById("m").value;let addr=document.getElementById("a").value;let msg="*NEW ORDER ToolMillMALL*%0AName: "+name+"%0AMoMo: "+momo+"%0AAddr: "+addr+"%0A";let t=0;cart.forEach(p=>{t+=p.price;msg+="- "+p.name+" GHS "+p.price+"%0A";});msg+="TOTAL GHS "+t;window.open("https://wa.me/233556023536?text="+msg,"_blank");}</script>'
    return page("Cart", b)

@app.route("/about")
def about(): return page("About", '<div class="bg-white p-6 rounded-xl text-sm leading-8"><h1 class="font-black text-2xl">About ToolMillMALL.GH</h1><p class="mt-4">ToolMillMALL.GH founded 2024 in Accra Ghana mission make online shopping easy affordable trustworthy for every Ghanaian. Ghanaian owned company Accra. Started 5 products now 30+ original products Electronics Fashion Food Beauty Home. iPhones Samsung Infinix Laptops TVs GTP prints dresses sneakers Lele Rice black soap wigs perfumes pots gas cookers chairs bedsheets irons power banks diapers. Why choose us: 100 percent original warranty, Pay on Delivery Cash MoMo, Same Day Delivery Accra 24-72h outside, Free Delivery Accra over 500, 7 Days Return defective, Support WhatsApp 0556023536, 1000+ happy customers. Vision become Ghana most trusted mall like Jumia Amazon. Contact WhatsApp 0556023536 Email toolmillgh@gmail.com Location Accra Ghana Hours Mon-Sat 8am-6pm Sun 12pm-5pm.</p></div>')

@app.route("/contact")
def contact(): return page("Contact", '<div class="bg-white p-6 rounded-xl text-sm leading-8"><h1 class="font-bold text-2xl">Contact Us</h1><p class="mt-4">We reply fast on WhatsApp.</p><p class="mt-3"><b>WhatsApp:</b> 0556023536<br><b>Phone:</b> 0556023536<br><b>Email:</b> toolmillgh@gmail.com<br><b>Location:</b> Accra Greater Accra Ghana<br><b>Hours:</b> Mon-Sat 8am-6pm Sun 12pm-5pm</p><a href="https://wa.me/233556023536" class="mt-6 inline-block bg-green-600 text-white px-8 py-3 rounded-full font-bold">Chat WhatsApp 0556023536</a></div>')

@app.route("/privacy")
def privacy(): return page("Privacy", '<div class="bg-white p-6 rounded-xl text-sm leading-8"><h1 class="font-bold text-2xl">Privacy Policy</h1><p class="mt-3">Effective September 2026 At ToolMillMALL.GH w1p1.onrender.com we respect privacy. We collect only name phone MoMo delivery address for order delivery. No card data. We use localStorage for cart no tracking cookies. We never sell data only shared with riders to deliver order. You can request deletion via WhatsApp 0556023536. Contact toolmillgh@gmail.com Accra Ghana.</p></div>')

@app.route("/shipping")
def shipping(): return page("Shipping", '<div class="bg-white p-6 rounded-xl text-sm leading-8"><h1 class="font-bold text-2xl">Shipping and Returns</h1><p class="mt-3">Free delivery Accra over GHS 500. Standard GHS 30-50 Accra GHS 60-100 outside Accra Kumasi Takoradi Tamale. Delivery Time 1-2 days Accra 2-4 days other regions. Riders and DHL trusted. 7 days return defective wrong damaged must be unused original packaging receipt contact WhatsApp 0556023536 within 7 days pickup arranged refund MoMo 24h after receiving return. No return food after opening. After WhatsApp order 0556023536 we call confirm and send rider contact.</p></div>')

@app.route("/terms")
def terms(): return page("Terms", '<div class="bg-white p-6 rounded-xl text-sm leading-8"><h1 class="font-bold text-2xl">Terms of Service</h1><p class="mt-3">By using ToolMillMALL.GH you agree to terms. All products authentic with warranty where applicable. Prices GHS can change without notice. We can cancel orders due to stock issues. Payment Cash on Delivery or MoMo. Governed by laws of Ghana. Contact 0556023536.</p></div>')

@app.route("/admin/delete/<int:pid>")
def delete_prod(pid):
    if request.args.get("pwd")!="admin123": return "Wrong pwd"
    global PRODUCTS
    PRODUCTS = [p for p in PRODUCTS if p["id"]!=pid]
    return redirect("/admin?pwd=admin123")

@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method=="POST":
        if request.form.get("pwd")!="admin123": return page("Admin","Wrong pwd")
        name=request.form.get("name"); price=request.form.get("price"); cat=request.form.get("cat"); img=request.form.get("img_url"); desc=request.form.get("desc")
        f=request.files.get("file")
        if f and f.filename!="":
            d=f.read(); b64=base64.b64encode(d).decode("utf-8"); img=f"data:{f.mimetype};base64,{b64}"
        if name and price:
            nid=max([p["id"] for p in PRODUCTS])+1 if PRODUCTS else 1
            PRODUCTS.append({"id":nid,"name":name,"price":int(price),"old":int(price)+100,"cat":cat,"img":img or "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400","desc":desc or name})
        return redirect("/admin?pwd=admin123")
    rows=""
    for p in PRODUCTS[::-1]:
        rows+=f'<tr class="border-b text-xs"><td class="p-2"><img src="{p["img"]}" class="w-10 h-10 object-cover"></td><td class="p-2">{p["name"][:20]}</td><td class="p-2">GHS {p["price"]}</td><td class="p-2"><a href="/admin/delete/{p["id"]}?pwd=admin123" class="bg-red-500 text-white px-2 py-1 rounded">Delete</a></td></tr>'
    body=f'<h1 class="font-bold">Admin - {len(PRODUCTS)} Products Plenty</h1><div class="bg-white p-4 rounded-xl mt-4"><form method="POST" enctype="multipart/form-data"><input type="hidden" name="pwd" value="admin123"><input name="name" placeholder="Name" class="w-full p-2 border rounded mb-2" required><input name="price" type="number" placeholder="Price" class="w-full p-2 border rounded mb-2" required><textarea name="desc" placeholder="Description 20+ words" class="w-full p-2 border rounded mb-2"></textarea><select name="cat" class="w-full p-2 border rounded mb-2"><option>Fashion</option><option>Electronics</option><option>Food</option><option>Beauty</option><option>Home</option></select><input type="file" name="file" class="w-full mb-2"><input name="img_url" placeholder="OR image URL https://" class="w-full p-2 border rounded mb-2"><button class="w-full bg-black text-white py-2 rounded-full">Add</button></form></div><div class="bg-white p-4 rounded-xl mt-4"><table class="w-full">{rows}</table><a href="/" class="block mt-4 bg-blue-600 text-white text-center py-2 rounded-full">View Shop {len(PRODUCTS)} Products</a></div>'
    if not request.args.get("pwd"):
        body='<div class="bg-white p-6 rounded-xl max-w-sm mx-auto mt-10"><h1 class="font-bold">Admin Login</h1><form method="POST" class="mt-4"><input name="pwd" type="password" placeholder="admin123" class="w-full p-3 border rounded"><button class="w-full mt-3 bg-black text-white py-3 rounded-full">Login</button></form></div>'
    return page("Admin", body)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
