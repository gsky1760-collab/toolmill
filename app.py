from flask import Flask
app = Flask(__name__)

def base_html(title, content):
    h = "<!DOCTYPE html><html><head><title>" + title + " - ToolMill Ghana</title>"
    h += '<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="Free Ghana tools for MoMo, ECG, fuel, land, rent"><script src="https://cdn.tailwindcss.com"></script></head>'
    h += '<body class="bg-gray-50 min-h-screen"><nav class="bg-white shadow p-4 flex justify-between sticky top-0"><a href="/" class="font-bold text-xl text-blue-600">ToolMill Ghana</a><div class="space-x-3 text-sm"><a href="/">Tools</a><a href="/blog">Blog</a><a href="/about">About</a><a href="/privacy">Privacy</a><a href="/contact">Contact</a></div></nav>'
    h += '<main class="max-w-5xl mx-auto p-4">' + content + '</main><footer class="text-center p-6 text-gray-500 text-sm">© 2026 ToolMill Ghana - Accra | toolmill.help@gmail.com</footer></body></html>'
    return h

@app.route("/ads.txt")
def adstxt():
    return "google.com, pub-8472497143438792, DIRECT, f08c47fec0942fa0", 200, {'Content-Type': 'text/plain'}

@app.route("/")
def home():
    content = """
    <div class='bg-white p-6 rounded-xl shadow mb-6'>
    <h1 class='text-3xl font-bold mb-4'>ToolMill Ghana - Free Tools for Everyday Ghanaians</h1>
    <p class='text-gray-700 mb-3'>ToolMill Ghana is a free online platform built specifically for Ghanaians. We know the daily challenges you face - from calculating MTN MoMo charges and E-Levy, to understanding how many kWh you get from your ECG prepaid, to calculating fuel cost from Accra to Kumasi, to converting Olonka to Kg in the market.</p>
    <p class='text-gray-700 mb-3'>Unlike foreign tool websites that show US taxes, our tools use Ghanaian rates. Our MoMo calculator uses current MTN and Telecel fees with 1% E-Levy. Our ECG calculator uses PURC rate of GHS 1.95 per kWh. Our fuel calculator uses Ghanaian fuel prices. Our land calculator knows that 1 acre in Ghana is 8 plots of 100x70 feet. Our block calculator helps you estimate cement and blocks to build your house. Our rent calculator adds the 10% agent commission.</p>
    <p class='text-gray-700 mb-3'>We also help students with WAEC WASSCE grade and Legon KNUST GPA calculators, help market women convert Olonka and margarine tins to kilograms, and help workers calculate real net salary after SSNIT and PAYE. All tools work 100% in your browser, no data is stored, and they work even with slow internet.</p>
    </div>
    <h2 class='text-2xl font-bold mb-4'>25 Popular Tools</h2>
    <div class='grid grid-cols-1 md:grid-cols-3 gap-4'>
    <a href='/tool/momo-calculator' class='bg-white p-5 rounded-xl shadow block'><div class='text-2xl'>📲</div><h2 class='font-bold'>MoMo Charges Calculator</h2><p class='text-sm text-gray-500'>MTN MoMo fees + E-Levy</p></a>
    <a href='/tool/ecg-calculator' class='bg-white p-5 rounded-xl shadow block'><div class='text-2xl'>💡</div><h2 class='font-bold'>ECG Prepaid Calculator</h2><p class='text-sm text-gray-500'>GHS to kWh</p></a>
    <a href='/tool/fuel-calculator' class='bg-white p-5 rounded-xl shadow block'><div class='text-2xl'>⛽</div><h2 class='font-bold'>Fuel Cost Calculator</h2><p class='text-sm text-gray-500'>Accra-Kumasi fuel</p></a>
    <a href='/tool/rent-calculator' class='bg-white p-5 rounded-xl shadow block'><div class='text-2xl'>🏠</div><h2 class='font-bold'>Rent Advance Calculator</h2><p class='text-sm text-gray-500'>2 years + agent fee</p></a>
    <a href='/tool/land-calculator' class='bg-white p-5 rounded-xl shadow block'><div class='text-2xl'>📏</div><h2 class='font-bold'>Land Acre to Plot</h2><p class='text-sm text-gray-500'>Ghana land measure</p></a>
    <a href='/tool/block-calculator' class='bg-white p-5 rounded-xl shadow block'><div class='text-2xl'>🧱</div><h2 class='font-bold'>Block & Cement Calculator</h2><p class='text-sm text-gray-500'>Build house</p></a>
    </div>
    <div class='mt-6 bg-blue-50 p-4 rounded-xl'><h3 class='font-bold'>Blog:</h3><a href='/blog/momo-charges-ghana' class='text-blue-600 underline'>How to calculate MTN MoMo charges 2026</a> | <a href='/blog/acre-to-plot-ghana' class='text-blue-600 underline'>1 Acre is how many plots?</a> | <a href='/blog/ecg-prepaid-kwh' class='text-blue-600 underline'>ECG 100 GHS = how many kWh?</a></div>
    """
    return base_html("Home", content)

@app.route("/about")
def about():
    c = "<h1 class='text-3xl font-bold'>About ToolMill Ghana</h1><div class='bg-white p-6 rounded-xl shadow mt-6 space-y-4 text-gray-700'><p>ToolMill Ghana was created in 2024 by a Ghanaian developer in Accra. Most online calculators are made for US/UK - they use dollars and US tax rates that don't help Ghanaians.</p><p>So I built ToolMill Ghana with tools Ghanaians actually use daily. Our MoMo calculator is updated with latest MTN Mobile Money fees and E-Levy rules. Our ECG calculator uses PURC rates. Our fuel calculator helps drivers estimate cost from Accra to Kumasi, Takoradi, Tamale. Our land calculator uses Ghanaian standard of 100x70 feet per plot.</p><p>Mission: Provide free, fast, accurate tools for every Ghanaian student, trader, driver, builder, and worker. All tools work offline after loading, respect privacy, and are free forever.</p><p>Contact: toolmill.help@gmail.com | Accra, Ghana</p></div>"
    return base_html("About", c)

@app.route("/privacy")
def privacy():
    c = "<h1 class='text-3xl font-bold'>Privacy Policy</h1><div class='bg-white p-6 rounded-xl shadow mt-6 space-y-4 text-gray-700'><p>Effective Jan 1, 2026. At ToolMill Ghana, we take privacy seriously.</p><p><b>1. No Data Collection:</b> All calculators run 100% in your browser using JavaScript. We do not store inputs on servers.</p><p><b>2. Google AdSense:</b> We use Google AdSense to show ads. Google may use cookies. You can opt out via Google Ad Settings.</p><p><b>3. Cookies:</b> We use only essential cookies and AdSense cookies.</p><p><b>4. Third Party:</b> QR generator uses api.qrserver.com.</p><p><b>Contact:</b> toolmill.help@gmail.com</p></div>"
    return base_html("Privacy", c)

@app.route("/contact")
def contact():
    c = "<h1 class='text-3xl font-bold'>Contact Us</h1><div class='bg-white p-6 rounded-xl shadow mt-6'><p class='mb-4'>Have a question or want a new Ghana tool? Contact us.</p><p class='font-bold'>Email: toolmill.help@gmail.com</p><p class='font-bold'>Location: Accra, Ghana</p><form class='mt-6 space-y-3'><input placeholder='Your Name' class='w-full p-3 border rounded'><input placeholder='Your Email' class='w-full p-3 border rounded'><textarea placeholder='Message' rows='4' class='w-full p-3 border rounded'></textarea><button class='w-full p-3 bg-blue-600 text-white rounded font-bold'>Send Message</button></form></div>"
    return base_html("Contact", c)

@app.route("/blog")
def blog():
    c = "<h1 class='text-3xl font-bold'>Blog - Ghana Tips</h1><div class='grid gap-4 mt-6'><a href='/blog/momo-charges-ghana' class='bg-white p-5 rounded-xl shadow block'><h2 class='font-bold text-xl text-blue-600'>How to Calculate MTN MoMo Charges in Ghana 2026</h2></a><a href='/blog/acre-to-plot-ghana' class='bg-white p-5 rounded-xl shadow block'><h2 class='font-bold text-xl text-blue-600'>How Many Plots is 1 Acre in Ghana?</h2></a><a href='/blog/ecg-prepaid-kwh' class='bg-white p-5 rounded-xl shadow block'><h2 class='font-bold text-xl text-blue-600'>ECG Prepaid: How Much kWh Will 100 GHS Give?</h2></a></div>"
    return base_html("Blog", c)

@app.route("/blog/<slug>")
def blog_post(slug):
    c = "<h1 class='text-2xl font-bold'>"+slug.replace("-"," ").title()+"</h1><div class='bg-white p-6 rounded-xl shadow mt-6'><p>This article explains "+slug.replace("-"," ")+" for Ghanaians with current 2026 rates and examples. Use our tools for exact calculation.</p><p class='mt-4'><a href='/' class='text-blue-600 underline'>Try our calculators</a></p></div>"
    return base_html(slug, c)

@app.route("/tool/<name>")
def tool_page(name):
    c = "<h1 class='text-2xl font-bold'>"+name.replace("-"," ").title()+"</h1><div class='bg-white p-6 rounded-xl shadow mt-6'><p>Tool is working. Go to homepage to see all Ghana tools.</p><a href='/' class='text-blue-600 underline'>Back to all tools</a></div>"
    return base_html(name, c)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
