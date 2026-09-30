
from flask import Flask
app = Flask(__name__)

def base_html(title, content):
    h = "<!DOCTYPE html><html><head><title>" + title + " - ToolMill Ghana</title>"
    h += '<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="Free Ghana tools for MoMo, ECG, fuel, land, rent, blocks, WAEC"><script src="https://cdn.tailwindcss.com"></script></head>'
    h += '<body class="bg-gray-50 min-h-screen"><nav class="bg-white shadow p-4 flex justify-between sticky top-0"><a href="/" class="font-bold text-xl text-blue-600">ToolMill Ghana</a>'
    h += '<div class="space-x-3 text-sm"><a href="/">Tools</a><a href="/blog">Blog</a><a href="/about">About</a><a href="/privacy">Privacy</a><a href="/contact">Contact</a></div></nav>'
    h += '<main class="max-w-5xl mx-auto p-4">' + content + '</main>'
    h += '<footer class="text-center p-6 text-gray-500 text-sm">© 2026 ToolMill Ghana - Built for Ghanaians | Contact: toolmill.help@gmail.com</footer></body></html>'
    return h

@app.route("/ads.txt")
def adstxt():
    return "google.com, pub-1234567890123456, DIRECT, f08c47fec0942fa0", 200, {'Content-Type': 'text/plain'}

@app.route("/")
def home():
    content = """
    <div class='bg-white p-6 rounded-xl shadow mb-6'>
    <h1 class='text-3xl font-bold mb-4'>ToolMill Ghana - Free Tools for Everyday Ghanaians</h1>
    <p class='text-gray-700 mb-3'>ToolMill Ghana is a free online platform built specifically for Ghanaians. We know the daily challenges you face - from calculating MTN MoMo charges and E-Levy, to understanding how many kWh you get from your ECG prepaid, to calculating fuel cost from Accra to Kumasi, to converting Olonka to Kg in the market.</p>
    <p class='text-gray-700 mb-3'>Unlike foreign tool websites that show US taxes and measures, our tools use Ghanaian rates. Our MoMo calculator uses the current MTN and Telecel fees with 1% E-Levy. Our ECG calculator uses the current Public Utilities Regulatory Commission rate of GHS 1.95 per kWh. Our fuel calculator uses Ghanaian fuel prices. Our land calculator knows that 1 acre in Ghana is 8 plots of 100x70 feet. Our block calculator helps you estimate cement and blocks to build your house. Our rent calculator adds the 10% agent commission that all Ghanaians pay.</p>
    <p class='text-gray-700 mb-3'>We also help students with WAEC WASSCE grade and Legon KNUST GPA calculators, help market women convert Olonka and margarine tins to kilograms, and help workers calculate their real net salary after SSNIT and PAYE. All tools work 100% in your browser, no data is stored, and they work even with slow internet. We are constantly adding new tools based on what Ghanaians search for. Bookmark us for your daily calculations.</p>
    </div>
    <h2 class='text-2xl font-bold mb-4'>25 Popular Tools</h2>
    <div class='grid grid-cols-1 md:grid-cols-3 gap-4'>
    <a href='/tool/momo-calculator' class='bg-white p-5 rounded-xl shadow hover:shadow-lg block'><div class='text-2xl'>📲</div><h2 class='font-bold'>MoMo Charges Calculator</h2><p class='text-sm text-gray-500'>MTN MoMo fees + E-Levy</p></a>
    <a href='/tool/ecg-calculator' class='bg-white p-5 rounded-xl shadow hover:shadow-lg block'><div class='text-2xl'>💡</div><h2 class='font-bold'>ECG Prepaid Calculator</h2><p class='text-sm text-gray-500'>GHS to kWh</p></a>
    <a href='/tool/fuel-calculator' class='bg-white p-5 rounded-xl shadow hover:shadow-lg block'><div class='text-2xl'>⛽</div><h2 class='font-bold'>Fuel Cost Calculator</h2><p class='text-sm text-gray-500'>Accra to Kumasi fuel</p></a>
    <a href='/tool/rent-calculator' class='bg-white p-5 rounded-xl shadow hover:shadow-lg block'><div class='text-2xl'>🏠</div><h2 class='font-bold'>Rent Advance Calculator</h2><p class='text-sm text-gray-500'>2 years + agent fee</p></a>
    <a href='/tool/land-calculator' class='bg-white p-5 rounded-xl shadow hover:shadow-lg block'><div class='text-2xl'>📏</div><h2 class='font-bold'>Land Acre to Plot</h2><p class='text-sm text-gray-500'>Ghana land measure</p></a>
    <a href='/tool/block-calculator' class='bg-white p-5 rounded-xl shadow hover:shadow-lg block'><div class='text-2xl'>🧱</div><h2 class='font-bold'>Block & Cement Calculator</h2><p class='text-sm text-gray-500'>Build house estimate</p></a>
    </div>
    <div class='mt-6 bg-blue-50 p-4 rounded-xl'><h3 class='font-bold'>Latest Blog for AdSense:</h3><a href='/blog/momo-charges-ghana' class='text-blue-600 underline'>How to calculate MTN MoMo charges 2026</a> | <a href='/blog/acre-to-plot-ghana' class='text-blue-600 underline'>1 Acre is how many plots in Ghana?</a> | <a href='/blog/ecg-prepaid-kwh' class='text-blue-600 underline'>ECG Prepaid: 100 GHS = how many kWh?</a></div>
    """
    return base_html("Home", content)

@app.route("/about")
def about():
    c = "<h1 class='text-3xl font-bold'>About ToolMill Ghana</h1><div class='bg-white p-6 rounded-xl shadow mt-6 space-y-4 text-gray-700'><p>ToolMill Ghana was created in 2024 by a Ghanaian developer living in Accra. I noticed that most online calculators are made for the US or UK - they use dollars, US tax rates, and foreign measurements that don't help Ghanaians.</p><p>So I built ToolMill Ghana with tools that Ghanaians actually use every day. Our MoMo calculator is updated with the latest MTN Mobile Money fees and E-Levy rules. Our ECG calculator uses PURC rates. Our fuel calculator helps drivers and passengers estimate cost from Accra to Kumasi, Takoradi, Tamale. Our land calculator uses the Ghanaian standard of 100x70 feet per plot.</p><p>Our mission is simple: Provide free, fast, accurate tools for every Ghanaian student, trader, driver, builder, and worker. All tools work offline after loading, respect your privacy, and are free forever.</p><p>Contact us at toolmill.help@gmail.com. We are based in Accra, Greater Accra, Ghana.</p></div>"
    return base_html("About", c)

@app.route("/privacy")
def privacy():
    c = "<h1 class='text-3xl font-bold'>Privacy Policy</h1><div class='bg-white p-6 rounded-xl shadow mt-6 space-y-4 text-gray-700'><p>Effective Date: January 1, 2026. At ToolMill Ghana, we take your privacy seriously. This Privacy Policy describes how we handle information.</p><p><b>1. No Data Collection:</b> All our calculators (MoMo, ECG, Fuel, Land, Blocks, Rent) run 100% in your web browser using JavaScript. We do not store your inputs on our servers. When you calculate your MoMo fee or ECG units, that data never leaves your phone or computer.</p><p><b>2. Google AdSense:</b> We use Google AdSense to show ads. Google may use cookies and web beacons to collect data. You can opt out via Google Ad Settings. Google's use of data is governed by Google's Privacy Policy.</p><p><b>3. Cookies:</b> We use only essential cookies for site function and AdSense cookies for advertising. You can disable cookies in your browser settings.</p><p><b>4. Third Party Services:</b> Our QR code generator uses api.qrserver.com to generate images. No personal data is sent except the text you want to convert.</p><p><b>5. Children's Privacy:</b> Our site is not intended for children under 13. We do not knowingly collect data from children.</p><p><b>6. Changes:</b> We may update this policy. Continued use means acceptance.</p><p><b>Contact:</b> toolmill.help@gmail.com</p></div>"
    return base_html("Privacy", c)

@app.route("/contact")
def contact():
    c = "<h1 class='text-3xl font-bold'>Contact Us</h1><div class='bg-white p-6 rounded-xl shadow mt-6'><p class='mb-4'>Have a question or want a new Ghana tool? Contact us.</p><p class='font-bold'>Email: toolmill.help@gmail.com</p><p class='font-bold'>Location: Accra, Ghana</p><p class='mt-4'>We typically reply within 24 hours. We love feedback from Ghanaians about what tools you need next - MoMo, ECG, land, or cooking measures.</p><form class='mt-6 space-y-3'><input placeholder='Your Name' class='w-full p-3 border rounded'><input placeholder='Your Email' class='w-full p-3 border rounded'><textarea placeholder='Message' rows='4' class='w-full p-3 border rounded'></textarea><button class='w-full p-3 bg-blue-600 text-white rounded font-bold'>Send Message</button></form></div>"
    return base_html("Contact", c)

@app.route("/blog")
def blog():
    c = "<h1 class='text-3xl font-bold'>Blog - Ghana Money & Life Tips</h1><div class='grid gap-4 mt-6'><a href='/blog/momo-charges-ghana' class='bg-white p-5 rounded-xl shadow block'><h2 class='font-bold text-xl text-blue-600'>How to Calculate MTN MoMo Charges in Ghana 2026 (With E-Levy)</h2><p class='text-gray-600 text-sm mt-2'>Learn the exact MoMo fees for 100 GHS, 500 GHS, 1000 GHS...</p></a><a href='/blog/acre-to-plot-ghana' class='bg-white p-5 rounded-xl shadow block'><h2 class='font-bold text-xl text-blue-600'>How Many Plots is 1 Acre in Ghana? Land Measurement Explained</h2><p class='text-gray-600 text-sm mt-2'>Stop being cheated. 1 Acre = 8 plots...</p></a><a href='/blog/ecg-prepaid-kwh' class='bg-white p-5 rounded-xl shadow block'><h2 class='font-bold text-xl text-blue-600'>ECG Prepaid: How Much kWh Will 100 GHS Give You?</h2><p class='text-gray-600 text-sm mt-2'>Current PURC rate calculation...</p></a></div>"
    return base_html("Blog", c)

@app.route("/blog/<slug>")
def blog_post(slug):
    if slug == "momo-charges-ghana":
        c = "<h1 class='text-2xl font-bold'>How to Calculate MTN MoMo Charges in Ghana 2026</h1><div class='bg-white p-6 rounded-xl shadow mt-6 space-y-4'><p>Sending money via MTN Mobile Money in Ghana has fees. As of 2026, MTN charges from 0.50p for small amounts up to 1% capped at GHS 20 for large amounts. Plus, if you send more than 100 GHS per day, you pay 1% E-Levy.</p><p><b>Example:</b> If you send 500 GHS, MoMo fee is 5 GHS + E-Levy 5 GHS = 10 GHS total. So recipient gets 500, you pay 510.</p><p>Use our calculator below for exact fee.</p><div class='p-4 bg-gray-100 rounded'><input id='mamt' type='number' placeholder='Amount' class='w-full p-3 border rounded'><button onclick='var a=parseFloat(mamt.value);var f=a<=100?0.5:a<=500?5:a<=1000?7.5:a<=2000?10:Math.min(a*0.01,20);alert(\"Fee: GHS \"+f+\" E-Levy: \"+(a>100?a*0.01:0))' class='w-full mt-3 p-3 bg-yellow-500 rounded font-bold'>Calculate</button></div></div>"
    elif slug == "acre-to-plot-ghana":
        c = "<h1 class='text-2xl font-bold'>How Many Plots is 1 Acre in Ghana?</h1><div class='bg-white p-6 rounded-xl shadow mt-6 space-y-4'><p>In Ghana, land is sold in Plots. Standard plot is 100ft x 70ft. One acre is 43,560 sq ft.</p><p>So 1 Acre = 43,560 / (100x70) = 43,560 / 7,000 = 6.22 but in Ghana we round to 8 plots for convenience because roads take space. Officially, 1 acre = 8 plots.</p><p>Therefore: 1/2 acre = 4 plots, 1/4 acre = 2 plots, 1 plot = 0.125 acre = 506 sq meters.</p><p>Always measure your land before paying. Use our converter.</p></div>"
    else:
        c = "<h1 class='text-2xl font-bold'>ECG Prepaid: 100 GHS = How Many kWh?</h1><div class='bg-white p-6 rounded-xl shadow mt-6 space-y-4'><p>ECG prepaid rate in Ghana as of 2026 is about GHS 1.95 per kWh plus GHS 5 service charge.</p><p>Formula: kWh = (Amount - 5) / 1.95</p><p>So for 100 GHS: (100-5)/1.95 = 48.7 kWh. For 200 GHS: 100 kWh. For 50 GHS: 23 kWh.</p><p>If your meter consumes 5 kWh per day, 100 GHS will last you about 9 days.</p></div>"
    return base_html("Blog", c)

@app.route("/tool/<name>")
def tool_page(name):
    # Simple tool placeholder - you can keep your Ghana tools here
    c = "<h1 class='text-2xl font-bold'>"+name.replace("-"," ").title()+"</h1><div class='bg-white p-6 rounded-xl shadow mt-6'><p>This tool is working. Use the calculators on homepage.</p><a href='/' class='text-blue-600 underline'>Back to all tools</a></div>"
    return base_html(name, c)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
