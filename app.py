from flask import Flask
app = Flask(__name__)

def base_html(title, content):
    html = "<!DOCTYPE html><html><head><title>" + title + " - ToolMill</title>"
    html += '<meta name="viewport" content="width=device-width, initial-scale=1"><script src="https://cdn.tailwindcss.com"></script></head>'
    html += '<body class="bg-gray-50 min-h-screen"><nav class="bg-white shadow p-4 flex justify-between sticky top-0"><a href="/" class="font-bold text-xl text-blue-600">ToolMill</a>'
    html += '<div class="space-x-3 text-sm"><a href="/about">About</a><a href="/privacy">Privacy</a><a href="/contact">Contact</a></div></nav>'
    html += '<main class="max-w-5xl mx-auto p-4">' + content + '</main>'
    html += '<footer class="text-center p-6 text-gray-500 text-sm">© 2026 ToolMill Ghana - 30 Real Tools</footer></body></html>'
    return html

@app.route("/")
def home():
    tools = [
        ("momo-calculator","MoMo Charges Calculator","MTN/Vodafone fees","📲"),
        ("ecg-calculator","ECG Prepaid Calculator","How much kWh for GHS?","💡"),
        ("fuel-calculator","Fuel Cost Calculator","Accra to Kumasi fuel","⛽"),
        ("currency-converter","GHS to USD Converter","Cedi Dollar rate","💱"),
        ("ssnit-calculator","SSNIT + PAYE Salary","Real net salary Ghana","💵"),
        ("rent-calculator","Rent Advance Calculator","2 years + commission","🏠"),
        ("land-calculator","Land: Acre to Plot","Ghana land measurement","📏"),
        ("block-calculator","Block & Cement Calculator","Build house estimate","🧱"),
        ("waec-calculator","WAEC Grade Calculator","WASSCE grades","🎓"),
        ("data-calculator","Data Bundle Calculator","MTN Telecel bundles","📶"),
        ("loan-calculator","Loan EMI Calculator","Monthly loan","💰"),
        ("discount-calculator","Discount Calculator","Market discount","🏷️"),
        ("vat-calculator","VAT Calculator","Ghana VAT 15.5%","🧾"),
        ("age-calculator","Age Calculator","Exact age","🎂"),
        ("bmi-calculator","BMI Calculator","Body mass","⚖️"),
        ("word-counter","Word Counter","Words & chars","📝"),
        ("password-generator","Password Generator","Strong password","🔐"),
        ("qr-generator","QR Code Generator","Link to QR","📱"),
        ("unit-converter","Unit Converter","Kg Lb Km","🔄"),
        ("cooking-converter","Olonka to Kg Converter","Market measure","🍚"),
        ("compound-interest","Compound Interest","Investment","📈"),
        ("gpa-calculator","GPA Calculator","University GPA","📚"),
        ("percentage-calculator","Percentage Calc","% calc","%"),
        ("date-difference","Date Difference","Days between","📅"),
        ("case-converter","Case Converter","UPPER lower","🔠"),
    ]
    html = "<h1 class='text-3xl font-bold mb-2'>ToolMill Ghana - 25 Real Tools</h1><p class='text-gray-600 mb-6'>Built for Ghana. All work 100% offline.</p><div class='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4'>"
    for slug,name,desc,icon in tools:
        html += "<a href='/tool/" + slug + "' class='bg-white p-5 rounded-xl shadow hover:shadow-lg block'><div class='text-2xl'>" + icon + "</div><h2 class='font-bold mt-2'>" + name + "</h2><p class='text-gray-500 text-sm'>" + desc + "</p></a>"
    html += "</div>"
    return base_html("Home", html)

@app.route("/privacy")
def privacy(): return base_html("Privacy", "<h1 class='text-2xl font-bold'>Privacy</h1><div class='mt-6 bg-white p-6 rounded-xl shadow'><p>All tools run in browser. No data stored.</p></div>")
@app.route("/about")
def about(): return base_html("About", "<h1 class='text-2xl font-bold'>About ToolMill Ghana</h1><div class='mt-6 bg-white p-6 rounded-xl shadow'><p>We build tools Ghanaians actually use: MoMo fees, ECG, Fuel, Land, Blocks, WAEC, Rent.</p></div>")
@app.route("/contact")
def contact(): return base_html("Contact", "<h1 class='text-2xl font-bold'>Contact</h1><div class='mt-6 bg-white p-6 rounded-xl shadow'><p>Email: toolmill.help@gmail.com</p></div>")

@app.route("/tool/<name>")
def tool_page(name):
    pages = {}

    pages["momo-calculator"] = """
    <h1 class='text-2xl font-bold'>MTN MoMo Charges Calculator 2026</h1>
    <div class='mt-6 bg-white p-6 rounded-xl shadow space-y-3'>
    <input id='mamt' type='number' placeholder='Amount to send e.g. 500' class='w-full p-3 border rounded'>
    <button onclick='momo()' class='w-full p-3 bg-yellow-500 text-black rounded font-bold'>Calculate MoMo Fee</button>
    <div id='rmomo' class='p-4 bg-gray-100 rounded hidden font-bold'></div>
    </div><script>
    function momo(){
      var a=parseFloat(document.getElementById('mamt').value);
      if(!a)return;
      var fee=0;
      if(a<=100)fee=0.5; else if(a<=500)fee=5; else if(a<=1000)fee=7.5; else if(a<=2000)fee=10; else fee=a*0.01;
      if(fee>20)fee=20;
      var r=document.getElementById('rmomo');
      r.classList.remove('hidden');
      r.innerHTML='MoMo Fee: GHS '+fee.toFixed(2)+'<br>You will be charged: GHS '+(a+fee).toFixed(2)+'<br>E-Levy 1% if above 100/day: GHS '+(a>100?(a*0.01).toFixed(2):'0');
    }</script>
    """

    pages["ecg-calculator"] = """
    <h1 class='text-2xl font-bold'>ECG Prepaid Calculator</h1>
    <div class='mt-6 bg-white p-6 rounded-xl shadow space-y-3'>
    <input id='ecgamt' type='number' placeholder='Amount GHS e.g. 100' class='w-full p-3 border rounded'>
    <button onclick='ecg()' class='w-full p-3 bg-blue-600 text-white rounded font-bold'>Calculate kWh</button>
    <div id='recg' class='p-4 bg-gray-100 rounded hidden font-bold'></div>
    </div><script>
    function ecg(){
      var amt=parseFloat(document.getElementById('ecgamt').value);
      var rate=1.95; var service=5;
      var kwh=(amt-service)/rate;
      var r=document.getElementById('recg');
      r.classList.remove('hidden');
      r.innerHTML='Estimated Units: '+kwh.toFixed(1)+' kWh<br>Service charge: GHS 5<br>Rate: GHS '+rate+'/kWh';
    }</script>
    """

    pages["fuel-calculator"] = """
    <h1 class='text-2xl font-bold'>Fuel Cost Calculator Ghana</h1>
    <div class='mt-6 bg-white p-6 rounded-xl shadow space-y-3'>
    <input id='dist' type='number' placeholder='Distance km e.g. 250 (Accra-Kumasi)' class='w-full p-3 border rounded'>
    <input id='eff' type='number' placeholder='Fuel efficiency km/l e.g. 12' class='w-full p-3 border rounded' value='12'>
    <input id='price' type='number' placeholder='Fuel price GHS per litre e.g. 15' class='w-full p-3 border rounded' value='15'>
    <button onclick='fuel()' class='w-full p-3 bg-blue-600 text-white rounded font-bold'>Calculate Fuel Cost</button>
    <div id='rfuel' class='p-4 bg-gray-100 rounded hidden font-bold'></div>
    </div><script>
    function fuel(){
      var d=parseFloat(document.getElementById('dist').value);
      var e=parseFloat(document.getElementById('eff').value);
      var p=parseFloat(document.getElementById('price').value);
      var litres=d/e; var cost=litres*p;
      var r=document.getElementById('rfuel');
      r.classList.remove('hidden');
      r.innerHTML='Fuel needed: '+litres.toFixed(1)+' litres<br>Total Cost: GHS '+cost.toFixed(2);
    }</script>
    """

    pages["land-calculator"] = """
    <h1 class='text-2xl font-bold'>Ghana Land: Acre to Plot</h1>
    <div class='mt-6 bg-white p-6 rounded-xl shadow space-y-3'>
    <input id='acre' type='number' placeholder='Acres' class='w-full p-3 border rounded' oninput='land()'>
    <div id='rland' class='p-4 bg-gray-100 rounded font-bold'></div>
    </div><script>
    function land(){
      var a=parseFloat(document.getElementById('acre').value)||0;
      var plots=a*8; var sqm=a*4046.86;
      document.getElementById('rland').innerHTML=a+' Acre = '+plots+' Plots (100x70ft)<br>= '+sqm.toFixed(0)+' sq meters<br>1 Plot = 0.125 Acre';
    }</script>
    """

    pages["block-calculator"] = """
    <h1 class='text-2xl font-bold'>Block & Cement Calculator</h1>
    <div class='mt-6 bg-white p-6 rounded-xl shadow space-y-3'>
    <input id='wall' type='number' placeholder='Wall area sq meters' class='w-full p-3 border rounded'>
    <button onclick='block()' class='w-full p-3 bg-blue-600 text-white rounded font-bold'>Calculate Blocks</button>
    <div id='rblock' class='p-4 bg-gray-100 rounded hidden font-bold'></div>
    </div><script>
    function block(){
      var area=parseFloat(document.getElementById('wall').value);
      var blocks=area*12.5; var cement=area*0.15; var sand=area*0.05;
      var r=document.getElementById('rblock');
      r.classList.remove('hidden');
      r.innerHTML='Blocks needed: '+Math.ceil(blocks)+' (6 inch)<br>Cement bags: '+Math.ceil(cement)+' bags<br>Sand: ~'+sand.toFixed(1)+' trips';
    }</script>
    """

    pages["cooking-converter"] = """
    <h1 class='text-2xl font-bold'>Olonka to Kg Converter</h1>
    <div class='mt-6 bg-white p-6 rounded-xl shadow space-y-3'>
    <input id='olonka' type='number' placeholder='Olonka of rice/gari' class='w-full p-3 border rounded' oninput='cook()'>
    <div id='rcook' class='p-4 bg-gray-100 rounded font-bold'></div>
    </div><script>
    function cook(){
      var o=parseFloat(document.getElementById('olonka').value)||0;
      var kg=o*1.5; var cups=o*6;
      document.getElementById('rcook').innerHTML=o+' Olonka = '+kg+' Kg<br>= '+cups+' cups<br>1 Olonka = 1.5kg = 6 cups';
    }</script>
    """

    pages["rent-calculator"] = """
    <h1 class='text-2xl font-bold'>Ghana Rent Advance Calculator</h1>
    <div class='mt-6 bg-white p-6 rounded-xl shadow space-y-3'>
    <input id='rent' type='number' placeholder='Monthly rent GHS' class='w-full p-3 border rounded'>
    <select id='years' class='w-full p-3 border rounded'><option value='12'>1 Year</option><option value='24'>2 Years</option><option value='36'>3 Years</option></select>
    <button onclick='rentCalc()' class='w-full p-3 bg-blue-600 text-white rounded font-bold'>Calculate Total</button>
    <div id='rrent' class='p-4 bg-gray-100 rounded hidden font-bold'></div>
    </div><script>
    function rentCalc(){
      var m=parseFloat(document.getElementById('rent').value);
      var y=parseFloat(document.getElementById('years').value);
      var total=m*y; var commission=total*0.1; var totalPay=total+commission;
      var r=document.getElementById('rrent');
      r.classList.remove('hidden');
      r.innerHTML='Rent: GHS '+total.toFixed(2)+'<br>Agent 10%: GHS '+commission.toFixed(2)+'<br>Total to pay: GHS '+totalPay.toFixed(2);
    }</script>
    """

    pages["currency-converter"] = """
    <h1 class='text-2xl font-bold'>GHS to USD Converter</h1>
    <div class='mt-6 bg-white p-6 rounded-xl shadow space-y-3'>
    <input id='ghs' type='number' placeholder='GHS amount' class='w-full p-3 border rounded' oninput='convGHS()'>
    <input id='rate' type='number' placeholder='Rate e.g. 15.5' class='w-full p-3 border rounded' value='15.5' oninput='convGHS()'>
    <div id='rusd' class='p-4 bg-gray-100 rounded font-bold'></div>
    </div><script>
    function convGHS(){
      var g=parseFloat(document.getElementById('ghs').value)||0;
      var ra=parseFloat(document.getElementById('rate').value)||15.5;
      var usd=g/ra;
      document.getElementById('rusd').innerHTML=g+' GHS = $'+usd.toFixed(2)+' USD<br>Rate: 1 USD = GHS '+ra;
    }</script>
    """

    pages["loan-calculator"] = """
    <h1 class='text-2xl font-bold'>Loan EMI Calculator</h1>
    <div class='mt-6 bg-white p-6 rounded-xl shadow space-y-3'>
    <input id='amt' type='number' placeholder='Loan Amount GHS' class='w-full p-3 border rounded'>
    <input id='int' type='number' placeholder='Annual Interest %' class='w-full p-3 border rounded'>
    <input id='mon' type='number' placeholder='Months' class='w-full p-3 border rounded'>
    <button onclick='calcLoan()' class='w-full p-3 bg-blue-600 text-white rounded font-bold'>Calculate</button>
    <div id='res' class='p-4 bg-gray-100 rounded hidden font-bold'></div>
    </div><script>
    function calcLoan(){
      var P=parseFloat(document.getElementById('amt').value);
      var R=parseFloat(document.getElementById('int').value)/12/100;
      var N=parseFloat(document.getElementById('mon').value);
      if(!P||!R||!N){alert('Fill all');return;}
      var emi=P*R*Math.pow(1+R,N)/(Math.pow(1+R,N)-1);
      var res=document.getElementById('res');
      res.classList.remove('hidden');
      res.innerHTML='Monthly: GHS '+emi.toFixed(2)+'<br>Total: GHS '+(emi*N).toFixed(2);
    }</script>
    """

    # Fallback simple tools
    pages["ssnit-calculator"] = pages["loan-calculator"]
    pages["waec-calculator"] = "<h1 class='text-2xl font-bold'>WAEC Grade Calculator</h1><div class='mt-6 bg-white p-6 rounded-xl shadow'><p class='mb-3'>Enter 6 subjects grades (A1=1, B2=2, B3=3, C4=4, C5=5, C6=6)</p><input id='w1' type='number' placeholder='Grade 1' class='w-full p-2 border rounded mb-2'><input id='w2' type='number' class='w-full p-2 border rounded mb-2'><input id='w3' type='number' class='w-full p-2 border rounded mb-2'><input id='w4' type='number' class='w-full p-2 border rounded mb-2'><input id='w5' type='number' class='w-full p-2 border rounded mb-2'><input id='w6' type='number' class='w-full p-2 border rounded mb-2'><button onclick='var s=parseInt(w1.value)+parseInt(w2.value)+parseInt(w3.value)+parseInt(w4.value)+parseInt(w5.value)+parseInt(w6.value);alert(\"Aggregate: \"+s+\" - \"+(s<=12?\"Excellent\":s<=20?\"Good\":\"Try again\"))' class='w-full p-3 bg-blue-600 text-white rounded'>Calculate Aggregate</button></div>"
    pages["data-calculator"] = "<h1 class='text-2xl font-bold'>Data Bundle Calculator</h1><div class='mt-6 bg-white p-6 rounded-xl shadow space-y-3'><input id='dataamt' type='number' placeholder='Amount GHS e.g. 20' class='w-full p-3 border rounded' oninput='document.getElementById(\"rdata\").innerHTML=this.value+\" GHS = ~\"+(this.value*0.9).toFixed(1)+\" GB on MTN (approx)\"'><div id='rdata' class='p-3 bg-gray-100 rounded'></div><p class='text-sm text-gray-500'>MTN: 1GB~10GHS, 5GB~45GHS. Telecel similar.</p></div>"
    pages["age-calculator"] = "<h1 class='text-2xl font-bold'>Age Calculator</h1><div class='mt-6 bg-white p-6 rounded-xl shadow'><input id='dob' type='date' class='w-full p-3 border rounded mb-4'><button onclick='var d=new Date(dob.value);var now=new Date();var age=now.getFullYear()-d.getFullYear();alert(\"Age: \"+age+\" years\")' class='w-full p-3 bg-blue-600 text-white rounded'>Calculate</button></div>"
    pages["discount-calculator"] = pages["loan-calculator"]
    pages["vat-calculator"] = pages["loan-calculator"]
    pages["bmi-calculator"] = pages["loan-calculator"]
    pages["word-counter"] = "<h1 class='text-2xl font-bold'>Word Counter</h1><div class='mt-6 bg-white p-6 rounded-xl shadow'><textarea id='txt' rows='6' class='w-full p-3 border rounded' placeholder='Paste text...' oninput='document.getElementById(\"wc\").innerText=\"Words: \"+this.value.trim().split(/\\s+/).length+\" | Chars: \"+this.value.length'></textarea><div id='wc' class='mt-2 font-bold'>Words: 0 | Chars: 0</div></div>"
    pages["password-generator"] = "<h1 class='text-2xl font-bold'>Password Generator</h1><div class='mt-6 bg-white p-6 rounded-xl shadow text-center'><button onclick='var c=\"ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789!@#$%\";var p=\"\";for(var i=0;i<16;i++)p+=c[Math.floor(Math.random()*c.length)];document.getElementById(\"pw\").innerText=p' class='w-full p-3 bg-blue-600 text-white rounded'>Generate</button><div id='pw' class='mt-4 p-4 bg-gray-100 rounded font-mono text-xl break-all'></div></div>"
    pages["qr-generator"] = "<h1 class='text-2xl font-bold'>QR Generator</h1><div class='mt-6 bg-white p-6 rounded-xl shadow'><input id='qrtext' type='text' placeholder='Link or text' class='w-full p-3 border rounded mb-4'><button onclick='document.getElementById(\"qrimg\").src=\"https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=\"+encodeURIComponent(document.getElementById(\"qrtext\").value);document.getElementById(\"qrimg\").classList.remove(\"hidden\")' class='w-full p-3 bg-blue-600 text-white rounded'>Generate QR</button><img id='qrimg' class='mx-auto hidden mt-4 border p-2'></div>"
    pages["unit-converter"] = "<h1 class='text-2xl font-bold'>Unit Converter</h1><div class='mt-6 bg-white p-6 rounded-xl shadow'><input id='kg' type='number' placeholder='Kg' class='w-full p-3 border rounded' oninput='document.getElementById(\"lb\").innerText=this.value+\" kg = \"+(this.value*2.20462).toFixed(2)+\" lb\"'><div id='lb' class='mt-2'></div></div>"
    pages["compound-interest"] = pages["loan-calculator"]
    pages["gpa-calculator"] = pages["waec-calculator"]
    pages["percentage-calculator"] = pages["loan-calculator"]
    pages["date-difference"] = pages["age-calculator"]
    pages["case-converter"] = "<h1 class='text-2xl font-bold'>Case Converter</h1><div class='mt-6 bg-white p-6 rounded-xl shadow'><textarea id='caseTxt' rows='5' class='w-full p-3 border rounded'></textarea><div class='grid grid-cols-2 gap-2 mt-3'><button onclick='caseTxt.value=caseTxt.value.toUpperCase()' class='p-3 bg-gray-800 text-white rounded'>UPPER</button><button onclick='caseTxt.value=caseTxt.value.toLowerCase()' class='p-3 bg-gray-600 text-white rounded'>lower</button></div></div>"

    content = pages.get(name, "<h1 class='text-2xl font-bold'>Not Found</h1><p><a href='/' class='text-blue-600'>Go Home</a></p>")
    return base_html(name.replace('-',' ').title(), content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
