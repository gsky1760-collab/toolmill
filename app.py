from flask import Flask, request, redirect
app = Flask(__name__)

# REAL PRODUCTS WITH REAL IMAGES - Like Temu/Shopify
PRODUCTS = [
    {"id":1,"name":"iPhone 15 Pro Max 256GB","price":18500,"old":21000,"cat":"Electronics","img":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400","stock":15},
    {"id":2,"name":"Samsung Galaxy A54 8GB/256GB","price":4200,"old":4800,"cat":"Electronics","img":"https://images.unsplash.com/photo-1610945265064-0e34e03294be?w=400","stock":20},
    {"id":3,"name":"GTP African Print 6 Yards","price":450,"old":550,"cat":"Fashion","img":"https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=400","stock":100},
    {"id":4,"name":"5kg Lele Rice - Ghana Quality","price":180,"old":220,"cat":"Food","img":"https://images.unsplash.com/photo-1536304929831-ee1ca9d44906?w=400","stock":50},
    {"id":5,"name":"Infinix Hot 40 Pro","price":2200,"old":2600,"cat":"Electronics","img":"https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400","stock":30},
    {"id":6,"name":"Adidas Sneakers Original","price":650,"old":850,"cat":"Fashion","img":"https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400","stock":40},
    {"id":7,"name":"50 Inch Smart TV - Nasco","price":3800,"old":4500,"cat":"Electronics","img":"https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400","stock":10},
    {"id":8,"name":"Ghana Black Soap 1kg","price":80,"old":100,"cat":"Beauty","img":"https://images.unsplash.com/photo-1600857544200-b2f666a9a2ec?w=400","stock":200},
    {"id":9,"name":"Office Chair - Executive","price":1200,"old":1500,"cat":"Home","img":"https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=400","stock":15},
    {"id":10,"name":"Olonka Gari 5 Bags","price":300,"old":350,"cat":"Food","img":"https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400","stock":60},
    {"id":11,"name":"HP Laptop Core i5","price":6500,"old":7500,"cat":"Electronics","img":"https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400","stock":8},
    {"id":12,"name":"Men Kaftan - Senator","price":380,"old":450,"cat":"Fashion","img":"https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=400","stock":25},
    {"id":13,"name":"Non-Stick Pot Set 6pcs","price":890,"old":1100,"cat":"Home","img":"https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=400","stock":18},
    {"id":14,"name":"Office Table - Mahogany","price":2500,"old":3000,"cat":"Home","img":"https://images.unsplash.com/photo-1533090484-07cc94c8a6f2?w=400","stock":5},
    {"id":15,"name":"MTN WiFi Router 4G","price":350,"old":450,"cat":"Electronics","img":"https://images.unsplash.com/photo-1592899677977-9bb10ba7fd8b?w=400","stock":35},
    {"id":16,"name":"Shea Butter Original 2kg","price":120,"old":150,"cat":"Beauty","img":"https://images.unsplash.com/photo-1571781926291-c477ebfd024b?w=400","stock":80},
    {"id":17,"name":"Black Stars Jersey","price":180,"old":250,"cat":"Fashion","img":"https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400","stock":90},
    {"id":18,"name":"Deep Freezer 200L","price":2800,"old":3200,"cat":"Home","img":"https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400","stock":12},
    {"id":19,"name":"Indomie Box 40pcs","price":280,"old":320,"cat":"Food","img":"https://images.unsplash.com/photo-1612929633738-8fe44f7ec841?w=400","stock":70},
    {"id":20,"name":"Generator 2.5KVA","price":3200,"old":3800,"cat":"Electronics","img":"https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=400","stock":9},
]

def base_html(title, content):
    h = "<!DOCTYPE html><html><head><title>" + title + "</title>"
    h += '<meta name="viewport" content="width=device-width, initial-scale=1"><script src="https://cdn.tailwindcss.com"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"></head>'
    h += '<body class="bg-gray-100"><header class="bg-white shadow sticky top-0 z-50"><div class="bg-blue-700 text-white text-center py-1 text-xs">🚚 Free Delivery Accra over GHS 500 | 0302 123 456</div>'
    h += '<nav class="max-w-7xl mx-auto p-3 flex justify-between items-center"><a href="/" class="font-black text-xl text-blue-700">ToolMill<span class="text-orange-500">MALL</span>.GH</a>'
    h += '<div class="flex gap-4 text-sm"><a href="/">Home</a><a href="/cart">Cart (<span id="cartcount">0</span>)</a><a href="/admin" class="bg-black text-white px-3 py-1 rounded-full">Admin</a></div></nav>'
    h += '<div class="max-w-7xl mx-auto px-3 py-2 flex gap-2 text-xs overflow-x-auto"><a href="/cat/Electronics" class="bg-blue-100 px-3 py-1 rounded-full whitespace-nowrap">Electronics</a><a href="/cat/Fashion" class="bg-pink-100 px-3 py-1 rounded-full">Fashion</a><a href="/cat/Food" class="bg-green-100 px-3 py-1 rounded-full">Food</a><a href="/cat/Home" class="bg-yellow-100 px-3 py-1 rounded-full">Home</a><a href="/cat/Beauty" class="bg-purple-100 px-3 py-1 rounded-full">Beauty</a></div></header>'
    h += '<main class="max-w-7xl mx-auto p-3">' + content + '</main>'
    h += '<footer class="bg-black text-white mt-10 p-6 text-center text-xs">© 2026 ToolMillMALL.GH | pub-8472497143438792</footer>'
    h += """<script>let cart=JSON.parse(localStorage.getItem('tm_cart')||'[]');function updateCount(){let e=document.getElementById('cartcount');if(e)e.innerText=cart.length}function addToCart(id){let p=products.find(x=>x.id==id);cart.push(p);localStorage.setItem('tm_cart',JSON.stringify(cart));updateCount();alert(p.name+' added!')}updateCount();</script></body></html>"""
    return h

@app.route("/ads.txt")
def adstxt(): return "google.com, pub-8472497143438792, DIRECT, f08c47fec0942fa0", 200, {'Content-Type': 'text/plain'}

@app.route("/")
def home():
    js = str(PRODUCTS).replace("'", '"')
    grid = "<div class='bg-gradient-to-r from-blue-600 to-orange-500 text-white p-5 rounded-xl mb-4'><h1 class='text-2xl font-black'>GHANA BIGGEST MALL - TEMU LEVEL</h1><p class='text-sm'>Real photos | MoMo | Admin to add products</p></div><div class='grid grid-cols-2 md:grid-cols-4 gap-3'>"
    for p in PRODUCTS:
        disc = int((1-p['price']/p['old'])*100)
        grid += f"<div class='bg-white rounded-xl shadow overflow-hidden'><img src='{p['img']}' class='w-full h-32 object-cover'><div class='p-3'><h3 class='font-bold text-xs leading-tight h-8 overflow-hidden'>{p['name']}</h3><div class='flex gap-1 mt-2 items-center'><b class='text-blue-700 text-sm'>GHS {p['price']}</b><span class='text-xs line-through text-gray-400'>{p['old']}</span><span class='bg-red-500 text-white text-[10px] px-1 rounded'>-{disc}%</span></div><button onclick='addToCart({p['id']})' class='w-full mt-2 bg-orange-500 text-white py-2 rounded-full text-xs font-bold'>Add to Cart</button></div></div>"
    grid += f"</div><script>let products={js}</script>"
    return base_html("ToolMillMALL.GH - Ghana", grid)

@app.route("/cat/<cat>")
def catpage(cat):
    filt=[p for p in PRODUCTS if p['cat'].lower()==cat.lower()]
    js=str(PRODUCTS).replace("'",'"')
    grid=f"<h1 class='text-xl font-bold'>{cat} - {len(filt)} Products</h1><div class='grid grid-cols-2 md:grid-cols-4 gap-3 mt-4'>"
    for p in filt:
        grid+=f"<div class='bg-white rounded-xl shadow overflow-hidden'><img src='{p['img']}' class='w-full h-32 object-cover'><div class='p-3'><h3 class='font-bold text-xs'>{p['name']}</h3><p class='font-black text-blue-700 text-sm'>GHS {p['price']}</p><button onclick='addToCart({p['id']})' class='w-full mt-2 bg-orange-500 text-white py-2 rounded-full text-xs'>Add to Cart</button></div></div>"
    grid+=f"</div><script>let products={js}</script>"
    return base_html(cat, grid)

@app.route("/product/<int:pid>")
def prod(pid):
    p=next((x for x in PRODUCTS if x['id']==pid),None)
    js=str(PRODUCTS).replace("'",'"')
    html=f"<div class='bg-white rounded-xl shadow p-4 grid md:grid-cols-2 gap-4'><img src='{p['img']}' class='w-full h-64 object-cover rounded'><div><h1 class='text-xl font-black'>{p['name']}</h1><p class='text-2xl font-black text-blue-700 mt-3'>GHS {p['price']}</p><p class='text-sm mt-3'>✅ MoMo Pay<br>✅ Free Delivery Accra<br>✅ 7 Days Return</p><button onclick='addToCart({p['id']})' class='w-full mt-5 bg-orange-500 text-white py-3 rounded-full font-bold'>Add to Cart</button></div></div><script>let products={js}</script>"
    return base_html(p['name'], html)

@app.route("/cart")
def cart():
    html="""<h1 class='text-xl font-bold'>Cart</h1><div class='bg-white rounded-xl shadow p-4 mt-4'><div id='cartlist'></div><div class='mt-4 border-t pt-3'><p class='font-bold'>Total: GHS <span id='total'>0</span></p><input placeholder='MoMo 024XXX' class='w-full mt-3 p-3 border rounded'><button onclick='alert("Order received!")' class='w-full mt-2 bg-green-600 text-white py-3 rounded-full font-bold'>Checkout MoMo</button><button onclick='localStorage.clear();location.reload()' class='w-full mt-2 bg-gray-200 py-2 rounded-full text-sm'>Clear Cart</button></div></div><script>let cart=JSON.parse(localStorage.getItem('tm_cart')||'[]');let list=document.getElementById('cartlist');let total=0;if(cart.length==0)list.innerHTML='Empty';else cart.forEach(p=>{total+=p.price;list.innerHTML+='<div class="flex justify-between py-2 border-b text-sm"><span>'+p.name+'</span><b>GHS '+p.price+'</b></div>'});document.getElementById('total').innerText=total;</script>"""
    return base_html("Cart", html)

@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method=="POST":
        if request.form.get("pwd")!="admin123": return base_html("Admin","<p>Wrong password</p><a href='/admin'>Back</a>")
        name=request.form.get("name"); price=request.form.get("price"); old=request.form.get("old"); cat=request.form.get("cat"); img=request.form.get("img"); stock=request.form.get("stock")
        if name and price:
            nid=max([p['id'] for p in PRODUCTS])+1 if PRODUCTS else 1
            PRODUCTS.append({"id":nid,"name":name,"price":int(price),"old":int(old) if old else int(price)+200,"cat":cat,"img":img if img else "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400","stock":int(stock) if stock else 10})
            return redirect("/admin?ok=1&pwd=admin123")
    ok=request.args.get("ok")
    msg="<div class='bg-green-100 p-2 rounded mb-3 text-green-700'>✅ Added!</div>" if ok else ""
    rows=""
    for p in PRODUCTS[::-1][:20]: rows+=f"<tr class='border-b text-xs'><td class='p-2'>{p['id']}</td><td class='p-2'><img src='{p['img']}' class='w-8 h-8 object-cover inline'> {p['name'][:20]}</td><td class='p-2'>GHS {p['price']}</td><td class='p-2'><a href='/admin/delete/{p['id']}?pwd=admin123' class='text-red-600'>Del</a></td></tr>"
    html=f"<h1 class='text-xl font-black'>Admin - Add Real Products</h1>{msg}<div class='grid md:grid-cols-2 gap-4 mt-4'><div class='bg-white p-4 rounded-xl shadow'><h2 class='font-bold mb-3'>Add Product with Image URL</h2><form method='POST' class='space-y-2'><input type='hidden' name='pwd' value='admin123'><input name='name' placeholder='Name' class='w-full p-2 border rounded' required><input name='price' type='number' placeholder='Price GHS' class='w-full p-2 border rounded' required><input name='old' type='number' placeholder='Old Price' class='w-full p-2 border rounded'><select name='cat' class='w-full p-2 border rounded'><option>Electronics</option><option>Fashion</option><option>Food</option><option>Home</option><option>Beauty</option></select><input name='img' placeholder='Paste Image URL https://...' class='w-full p-2 border rounded' required><p class='text-[10px] text-gray-500'>Tip: Search on Google Images, copy image address</p><input name='stock' type='number' placeholder='Stock' class='w-full p-2 border rounded'><button class='w-full bg-black text-white py-2 rounded-full font-bold'>Add Product</button></form></div><div class='bg-white p-4 rounded-xl shadow'><h2 class='font-bold mb-3'>All Products ({len(PRODUCTS)})</h2><table class='w-full'><tr class='bg-gray-100 text-xs'><th>ID</th><th>Name</th><th>Price</th><th>Del</th></tr>{rows}</table><a href='/' class='block mt-4 text-center bg-blue-600 text-white py-2 rounded-full'>View Shop</a></div></div>"
    if not request.args.get("pwd") and request.method=="GET":
        html="<h1 class='font-black text-xl'>Admin Login</h1><div class='bg-white p-4 rounded-xl shadow mt-4 max-w-sm'><form method='POST'><input name='pwd' type='password' placeholder='Password' class='w-full p-3 border rounded' required><p class='text-xs mt-1'>Password: admin123</p><button class='w-full mt-3 bg-black text-white py-2 rounded-full'>Login</button></form></div>"
    return base_html("Admin", html)

@app.route("/admin/delete/<int:pid>")
def adel(pid):
    if request.args.get("pwd")!="admin123": return "No"
    global PRODUCTS; PRODUCTS=[p for p in PRODUCTS if p['id']!=pid]; return redirect("/admin?pwd=admin123")

@app.route("/tools")
def tools(): return base_html("Tools","<h1 class='font-bold'>Ghana Tools</h1><div class='grid grid-cols-2 gap-2 mt-3'><a href='/tool/land-calculator' class='bg-white p-4 rounded shadow'>Land Calculator</a><a href='/tool/momo-calculator' class='bg-white p-4 rounded shadow'>MoMo Calculator</a></div>")
@app.route("/tool/<n>")
def tool(n): return base_html(n,f"<div class='bg-white p-6 rounded shadow'><h1 class='font-bold'>{n.replace('-',' ').title()}</h1><p>Tool working. AdSense content here with 1000+ words for approval.</p></div>")

if __name__=="__main__": app.run(host="0.0.0.0", port=10000)
