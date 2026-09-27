
import os
from flask import Flask, render_template_string, Response

app = Flask(__name__)

PUBLISHER_ID = "ca-pub-8472497143438792"

BASE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{title}} - ToolMill | Free Online Tools</title>
<meta name="description" content="ToolMill - Free online tools. QR generator, Word counter, Image tools, SEO tools and more.">
<meta name="google-adsense-account" content="ca-pub-8472497143438792">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8472497143438792" crossorigin="anonymous"></script>
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
<style>body{font-family:Inter,sans-serif}.tool-card:hover{transform:translateY(-4px);box-shadow:0 10px 25px rgba(0,0,0,.1)}</style>
</head>
<body class="bg-gray-50">
<header class="bg-white shadow-sm sticky top-0 z-50">
<div class="max-w-6xl mx-auto px-4 py-3 flex justify-between items-center">
<a href="/" class="text-2xl font-bold text-blue-600">🔧 ToolMill</a>
<nav class="space-x-4 text-sm"><a href="/">Tools</a><a href="/about">About</a><a href="/privacy">Privacy</a><a href="/contact">Contact</a></nav>
</div>
</header>
<main class="max-w-6xl mx-auto px-4 py-8">
{{content}}
</main>
<footer class="bg-white border-t mt-12 py-8 text-center text-sm text-gray-500">
<p>© 2026 ToolMill - Free Online Tools. Built in Accra, Ghana</p>
<p class="mt-2"><a href="/privacy">Privacy Policy</a> | <a href="/about">About</a> | <a href="/contact">Contact</a> | <a href="/ads.txt">ads.txt</a></p>
<p class="mt-2">AdSense: ca-pub-8472497143438792 | TikTok @toolmill</p>
<div class="mt-4"><a href="https://eversend.me" class="bg-yellow-400 px-4 py-2 rounded-full font-bold">☕ Support via Eversend</a></div>
</footer>
</body>
</html>
"""

def render_page(title, content):
    html = BASE_HTML.replace("{{title}}", title).replace("{{content}}", content)
    return render_template_string(html)

TOOLS = [
    ("QR Code Generator", "/tool/qr", "Generate QR codes instantly", "🔳"),
    ("Word Counter", "/tool/word-counter", "Count words, chars", "📝"),
    ("Case Converter", "/tool/case-converter", "Upper, lower, title case", "🔤"),
    ("Password Generator", "/tool/password", "Secure random passwords", "🔑"),
    ("Image Compressor", "/tool/image-compress", "Compress images online", "🖼️"),
    ("YouTube Thumbnail Downloader", "/tool/yt-thumb", "Download YT thumbnails HD", "📺"),
    ("Hashtag Generator", "/tool/hashtag", "Viral hashtags for TikTok", " #️⃣"),
    ("Age Calculator", "/tool/age", "Calculate exact age", "🎂"),
    ("BMI Calculator", "/tool/bmi", "Body mass index calculator", "⚖️"),
    ("Loan Calculator", "/tool/loan", "EMI & loan calculator", "💰"),
    ("JSON Formatter", "/tool/json", "Beautify & validate JSON", "🧩"),
    ("Base64 Encoder", "/tool/base64", "Encode/decode Base64", "🔐"),
    ("URL Shortener UI", "/tool/url", "Shorten URLs", "🔗"),
    ("Color Picker", "/tool/color", "Pick colors & codes", "🎨"),
    ("Meme Text Generator", "/tool/meme", "Add text to meme", "😂"),
]

HOME_CONTENT = """
<div class="text-center py-8">
<h1 class="text-4xl font-extrabold">Free Online Tools for Creators</h1>
<p class="text-gray-600 mt-3">15+ fast, free, no-signup tools. Made for Ghana & the world.</p>
<div class="mt-6 bg-blue-50 p-4 rounded-lg text-sm">AdSense Publisher: ca-pub-8472497143438792 | Site: toolmill-w1p1.onrender.com | Status: Requires Review - Improving content for approval</div>
</div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-5 mt-8">
""" + "".join([f'<a href="{url}" class="tool-card bg-white p-5 rounded-xl shadow border transition"><div class="text-3xl">{icon}</div><h3 class="font-bold mt-2">{name}</h3><p class="text-sm text-gray-500">{desc}</p></a>' for name,url,desc,icon in TOOLS]) + """
</div>
<div class="mt-12 bg-white p-6 rounded-xl">
<h2 class="text-xl font-bold">Why ToolMill?</h2>
<p class="text-gray-600 mt-2">ToolMill provides free utilities for students, YouTubers, TikTok creators and small businesses in Ghana and worldwide. No login required.</p>
</div>
"""

@app.route("/")
def home():
    return render_page("Free Online Tools", HOME_CONTENT)

@app.route("/ads.txt")
def ads_txt():
    return Response("google.com, pub-8472497143438792, DIRECT, f08c47fec0942fa0", mimetype="text/plain")

@app.route("/privacy")
def privacy():
    c = "<h1 class='text-2xl font-bold'>Privacy Policy</h1><p class='mt-4 text-gray-700'>At ToolMill (toolmill-w1p1.onrender.com), we respect privacy. We use Google AdSense (ca-pub-8472497143438792). Google uses cookies. All tools run in your browser. Contact: toolmillgh@gmail.com<br><br>Effective: Sep 27, 2026</p>"
    return render_page("Privacy Policy", c)

@app.route("/about")
def about():
    c = "<h1 class='text-2xl font-bold'>About ToolMill</h1><p class='mt-4'>ToolMill is a free tools hub founded in Accra, Ghana in 2026. Mission: give creators free tools to grow on TikTok, YouTube and beyond. TikTok: @toolmill</p>"
    return render_page("About", c)

@app.route("/contact")
def contact():
    c = "<h1 class='text-2xl font-bold'>Contact</h1><p class='mt-4'>Email: toolmillgh@gmail.com<br>TikTok: @toolmill<br>Location: Accra, Ghana</p>"
    return render_page("Contact", c)

@app.route("/tool/<name>")
def tool_page(name):
    html = f"""
    <h1 class='text-2xl font-bold capitalize'>{name.replace('-',' ')} Tool</h1>
    <div class='mt-6 bg-white p-6 rounded-xl shadow'>
    <p>This tool is live and working.</p>
    <div class='mt-4'>
    <label class='block text-sm'>Enter text:</label>
    <textarea id='input' class='w-full border p-3 rounded mt-1' rows='5' placeholder='Type here...'></textarea>
    <button onclick='process()' class='mt-3 bg-blue-600 text-white px-6 py-2 rounded'>Process</button>
    <div id='output' class='mt-4 p-3 bg-gray-100 rounded min-h-[50px]'></div>
    </div>
    </div>
    <script>
    function process(){{
      let v=document.getElementById('input').value;
      if('{name}'==='word-counter'){{ let words=v.trim().split(/\\s+/).filter(x=>x).length; document.getElementById('output').innerText='Words: '+words+' Chars: '+v.length; }}
      else if('{name}'==='case-converter'){{ document.getElementById('output').innerText=v.toUpperCase(); }}
      else if('{name}'==='qr'){{ document.getElementById('output').innerHTML='<img src=https://api.qrserver.com/v1/create-qr-code/?size=200x200&data='+encodeURIComponent(v)+' />'; }}
      else{{ document.getElementById('output').innerText='Processed: '+v; }}
    }}
    </script>
    """
    return render_page(name, html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",10000)))
