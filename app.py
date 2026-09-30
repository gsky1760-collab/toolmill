from flask import Flask, request, redirect
import base64
app = Flask(__name__)

# YOUR WHATSAPP NUMBER FOR ORDERS - CHANGE THIS TO YOUR NUMBER
WHATSAPP_NUMBER = "233556023536" # e.g. 233556023536

PRODUCTS = [
    {"id":1,"name":"iPhone 15 Pro Max 256GB","price":18500,"old":21000,"cat":"Electronics","img":"https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400","stock":15},
    {"id":2,"name":"Samsung Galaxy A54 8GB/256GB","price":4200,"old":4800,"cat":"Electronics","img":"https://images.unsplash.com/photo-1610945265064-0e34e03294be?w=400","stock":20},
    {"id":3,"name":"GTP African Print 6 Yards","price":450,"old":550,"cat":"Fashion","img":"https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=400","stock":100},
    {"id":4,"name":"5kg Lele Rice - Ghana Quality","price":180,"old":220,"cat":"Food","img":"https://images.unsplash.com/photo-1536304929831-ee1ca9d44906?w=400","stock":50},
    {"id":5,"name":"Infinix Hot 40 Pro 8/256GB","price":2200,"old":2600,"cat":"Electronics","img":"https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400","stock":30},
    {"id":6,"name":"Adidas Sneakers Original","price":650,"old":850,"cat":"Fashion","img":"https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400","stock":40},
    {"id":7,"name":"Nasco 50 Inch Smart TV","price":3800,"old":4500,"cat":"Electronics","img":"https://images.unsplash.com/photo-1593784991095-a205069470b6?w=400","stock":10},
    {"id":8,"name":"Ghana Black Soap 1kg","price":80,"old":100,"cat":"Beauty","img":"https://images.unsplash.com/photo-1600857544200-b2f666a9a2ec?w=400","stock":200},
    {"id":9,"name":"MTN 4G WiFi Router","price":350,"old":450,"cat":"Electronics","img":"https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=500","stock":35},
    {"id":10,"name":"Shea Butter Original 2kg","price":120,"old":150,"cat":"Beauty","img":"https://images.unsplash.com/photo-1571781926291-c477ebfd024b?w=400","stock":80},
    {"id":11,"name":"Black Stars Jersey 2026","price":180,"old":250,"cat":"Fashion","img":"https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400","stock":90},
    {"id":12,"name":"Deep Freezer 200L - Nasco","price":2800,"old":3200,"cat":"Home","img":"https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?w=400","stock":12},
    {"id":13,"name":"Indomie Box 40pcs Chicken","price":280,"old":320,"cat":"Food","img":"https://images.unsplash.com/photo-1612929633738-8fe44f7ec841?w=400","stock":70},
    {"id":14,"name":"Generator 2.5KVA - Petrol","price":3200,"old":3800,"cat":"Electronics","img":"https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=400","stock":9},
]

def base_html(title, content):
    h = f"<!DOCTYPE html><html><head><title>{title}</title><meta name='viewport' content='width=device-width, initial-scale=1'><script src='https://cdn.tailwindcss.com'></script><link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css'></head>"
    h += '<body class="bg-gray-100"><header class="bg-white shadow sticky top-0 z-50"><div class="bg-blue-700 text-white text-center py-1 text-xs">🚚 Free Delivery Accra over GHS 500 | 0302 123 456</div>'
    h += '<nav class="max-w-7xl mx-auto p-3 flex justify-between items-center"><a href="/" class="font-black text-xl text-blue-700">ToolMill<span class="text-orange-500">MALL</span>.GH</a><div class="flex gap-3 text-sm items-center"><a href="/">Home</a><a href="/cart">Cart (<span id="cartcount">0</span>)</a><a href="/admin" class="bg-black text-white px-3 py-1 rounded-full">Admin</a></div></nav></header>'
    h += f'<main class="max-w-7xl mx-auto p-3">{content}</main><footer class="bg-black text-white mt-10 p-6 text-center text-xs">© 2026 ToolMillMALL.GH | WhatsApp Orders | pub-8472497143438792 | toolmill.help@gmail.com</footer>'
    h += """<script>let cart=JSON.parse(localStorage.getItem('tm_cart')||'[]');function updateCount(){let e=document.getElementById('cartcount');if(e)e.innerText=cart.length}function addToCart(id){let p=products.find(x=>x.id==id);cart.push(p);localStorage.setItem('tm_cart',JSON.stringify(cart));updateCount();alert(p.name+' added to cart!');}updateCount();</script></body></html>"""
    return h

@app.route("/ads.txt")
def ads(): return "google.com, pub-8472497143438792, DIRECT, f08c47fec0942fa0", 200, {'Content-Type':'text/plain'}

@app.route("/")
def home():
    js = str(PRODUCTS).replace("'", '"')
    grid = "<div class='bg-gradient-to-r from-blue-600 to-orange-500 text-white p-5 rounded-xl mb-4'><h1 class='text-2xl font-black'>GHANA'S BIGGEST MALL</h1><p class='text-sm'>Real Photos • WhatsApp Order • Pay MoMo</p></div><div class='grid grid-cols-2 md:grid-cols-4 gap-3'>"
    for p in PRODUCTS:
        disc = int((1-p['price']/p['old'])*100) if p['old']>0 else 0
        grid += f"<div class='bg-white rounded-xl shadow overflow-hidden'><img src='{p['img']}' class='w-full h-40 object-cover'><div class='p-3'><h3 class='font-bold text-xs h-8 overflow-hidden'>{p['name']}</h3><div class='flex gap-1 mt-2 items-center'><b class='text-blue-700 text-sm'>GHS {p['price']}</b><span class='text-[10px] line-through text-gray-400'>GHS {p['old']}</span><span class='bg-red-500 text-white text-[9px] px-1 rounded'>-{disc}%</span></div><button onclick='addToCart({p['id']})' class='w-full mt-2 bg-orange-500 text-white py-2 rounded-full text-xs font-bold'>Add to Cart</button><a href='/product/{p['id']}' class='block text-center text-[11px] text-blue-600 mt-1'>View Details</a></div></div>"
    grid += f"</div><script>let products={js}</script>"
    return base_html("ToolMillMALL.GH", grid)

@app.route("/product/<int:pid>")
def product_page(pid):
    p = next((x for x in PRODUCTS if x['id']==pid), None)
    if not p: return "Not found"
    js=str(PRODUCTS).replace("'",'"')
    html=f"<div class='bg-white rounded-xl shadow p-4 grid md:grid-cols-2 gap-4'><img src='{p['img']}' class='w-full h-72 object-cover rounded-xl'><div><h1 class='font-black text-xl'>{p['name']}</h1><p class='text-sm text-gray-500'>{p['cat']} | Stock: {p['stock']}</p><p class='text-3xl font-black text-blue-700 mt-3'>GHS {p['price']}</p><p class='text-sm mt-4'>✅ Pay with MoMo<br>✅ Free Delivery Accra over GHS 500<br>✅ WhatsApp Order Instant</p><button onclick='addToCart({p['id']})' class='w-full mt-6 bg-orange-500 text-white py-3 rounded-full font-bold'>Add to Cart</button><a href='/cart' class='block text-center mt-3 bg-green-600 text-white py-2 rounded-full text-sm'>Go to Cart & WhatsApp Order</a></div></div><script>let products={js}</script>"
    return base_html(p['name'], html)

@app.route("/cart")
def cart_page():
    html = f"""
    <h1 class='text-xl font-bold'>Your Cart</h1>
    <div class='bg-white rounded-xl shadow p-4 mt-4'>
    <div id='cartlist' class='space-y-2'></div>
    <div class='mt-6 border-t pt-4'>
    <p class='font-black text-xl'>Total: GHS <span id='total'>0</span></p>
    <input id='custname' placeholder='Your Name' class='w-full mt-3 p-3 border rounded'>
    <input id='custmomo' placeholder='Your MoMo Number 024XXXXXXX' class='w-full mt-2 p-3 border rounded'>
    <input id='custaddr' placeholder='Delivery Address e.g. Accra, Madina' class='w-full mt-2 p-3 border rounded'>
    <button onclick='checkoutWA()' class='w-full mt-4 bg-green-600 text-white py-3 rounded-full font-bold text-lg'><i class="fa-brands fa-whatsapp"></i> Order via WhatsApp</button>
    <p class='text-xs text-gray-500 mt-2 text-center'>Clicking will open WhatsApp with your order details to us</p>
    <button onclick='localStorage.clear();location.reload()' class='w-full mt-3 bg-gray-200 py-2 rounded-full text-sm'>Clear Cart</button>
    </div>
    </div>
    <script>
    let cart=JSON.parse(localStorage.getItem('tm_cart')||'[]');
    let list=document.getElementById('cartlist');
    let total=0;
    if(cart.length==0){{list.innerHTML='<p class="text-gray-500">Cart empty. Add products from home.</p>';}}
    else{{cart.forEach(p=>{{total+=p.price; list.innerHTML+='<div class="flex justify-between py-2 border-b text-sm"><span>'+p.name+'</span><b>GHS '+p.price+'</b></div>';}});}}
    document.getElementById('total').innerText=total;
    function checkoutWA(){{
        let name=document.getElementById('custname').value||'Customer';
        let momo=document.getElementById('custmomo').value;
        let addr=document.getElementById('custaddr').value;
        if(cart.length==0){{alert('Cart empty');return;}}
        if(!momo){{alert('Enter MoMo number');return;}}
        let msg='*NEW ORDER - ToolMillMALL.GH*%0A%0A';
        msg+='Name: '+name+'%0AMoMo: '+momo+'%0AAddress: '+addr+'%0A%0A*Items:*%0A';
        cart.forEach(p=>{{msg+='- '+p.name+' = GHS '+p.price+'%0A';}});
        msg+='%0A*TOTAL: GHS '+total+'*%0A%0APlease confirm delivery.';
        let url='https://wa.me/{WHATSAPP_NUMBER}?text='+msg;
        window.open(url,'_blank');
    }}
    </script>
    """
    return base_html("Cart - WhatsApp Order", html)

@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method=="POST":
        if request.form.get("pwd")!="admin123": return base_html("Admin","Wrong password <a href='/admin'>Back</a>")
        name=request.form.get("name"); price=request.form.get("price"); old=request.form.get("old"); cat=request.form.get("cat"); img=request.form.get("img_url")
        # handle file upload
        file = request.files.get('file')
        if file and file.filename!='':
            data = file.read()
            b64 = base64.b64encode(data).decode('utf-8')
            mime = file.mimetype or 'image/jpeg'
            img = f"data:{mime};base64,{b64}"
        if name and price:
            nid=max([p['id'] for p in PRODUCTS])+1 if PRODUCTS else 1
            PRODUCTS.append({{"id":nid,"name":name,"price":int(price),"old":int(old) if old else int(price)+300,"cat":cat,"img":img if img else "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400","stock":20}})
            return redirect("/admin?ok=1&pwd=admin123")
    ok=request.args.get("ok")
    msg="<div class='bg-green-100 text-green-700 p-3 rounded mb-3 font-bold'>✅ Product Added! Check Home</div>" if ok else ""
    rows="".join([f"<tr class='border-b text-xs'><td class='p-2'><img src='{p['img']}' class='w-10 h-10 object-cover rounded'></td><td class='p-2'>{p['name'][:20]}</td><td class='p-2'>GHS {p['price']}</td><td class='p-2'><a href='/admin/delete/{p['id']}?pwd=admin123' class='text-red-600'>Delete</a></td></tr>" for p in PRODUCTS[::-1][:30]])
    html=f"""
    <h1 class='text-xl font-black'>Admin Panel - Upload & WhatsApp</h1>{msg}
    <div class='grid md:grid-cols-2 gap-4 mt-4'>
    <div class='bg-white p-5 rounded-xl shadow'>
    <h2 class='font-bold mb-3'>Add Product (Upload from Phone)</h2>
    <form method='POST' enctype='multipart/form-data' class='space-y-3'>
    <input type='hidden' name='pwd' value='admin123'>
    <input name='name' placeholder='Product Name' class='w-full p-3 border rounded' required>
    <input name='price' type='number' placeholder='Price GHS' class='w-full p-3 border rounded' required>
    <input name='old' type='number' placeholder='Old Price (for discount)' class='w-full p-3 border rounded'>
    <select name='cat' class='w-full p-3 border rounded'><option>Electronics</option><option>Fashion</option><option>Food</option><option>Home</option><option>Beauty</option></select>
    <label class='block text-sm font-bold'>Upload Photo from Phone:</label>
    <input type='file' name='file' accept='image/*' class='w-full p-2 border rounded bg-gray-50'>
    <p class='text-xs text-center'>OR paste Image URL</p>
    <input name='img_url' placeholder='https://...' class='w-full p-3 border rounded'>
    <button class='w-full bg-black text-white py-3 rounded-full font-bold'>Add Product to Mall</button>
    </form>
    <div class='bg-yellow-50 p-3 rounded mt-4 text-xs'><b>Change WhatsApp Number:</b> In code line 5, edit WHATSAPP_NUMBER = "233..." to your real number (without +)</div>
    </div>
    <div class='bg-white p-4 rounded-xl shadow'><h2 class='font-bold mb-3'>Products ({len(PRODUCTS)})</h2><div class='max-h-[600px] overflow-y-auto'><table class='w-full'>{rows}</table></div><a href='/' class='block mt-4 text-center bg-blue-600 text-white py-2 rounded-full'>View Shop →</a></div>
    </div>
    """
    if not request.args.get("pwd") and request.method=="GET":
        html="<h1 class='font-black text-xl'>Admin Login</h1><div class='bg-white p-6 rounded-xl shadow mt-4 max-w-sm'><form method='POST'><input name='pwd' type='password' placeholder='Password: admin123' class='w-full p-3 border rounded' required><button class='w-full mt-3 bg-black text-white py-3 rounded-full font-bold'>Login</button></form></div>"
    return base_html("Admin", html)

@app.route("/admin/delete/<int:pid>")
def adel(pid):
    if request.args.get("pwd")!="admin123": return "Unauthorized"
    global PRODUCTS; PRODUCTS=[p for p in PRODUCTS if p['id']!=pid]; return redirect("/admin?pwd=admin123")

if __name__=="__main__": app.run(host="0.0.0.0", port=10000)
