
from flask import Flask, render_template_string

app = Flask(__name__)

def render_page(title, content):
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{{title}} - ToolMill</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-50 min-h-screen">
        <nav class="bg-white shadow p-4 flex justify-between sticky top-0 z-10">
            <a href="/" class="font-bold text-xl text-blue-600">ToolMill</a>
            <div class="space-x-3 text-sm">
                <a href="/about">About</a>
                <a href="/privacy">Privacy</a>
                <a href="/contact">Contact</a>
            </div>
        </nav>
        <main class="max-w-5xl mx-auto p-4 md:p-6">{{content|safe}}</main>
        <footer class="text-center p-6 text-gray-500 text-sm">© 2026 ToolMill - 20 Real Tools, 100% Free</footer>
    </body>
    </html>
    """, title=title, content=content)

@app.route("/")
def home():
    tools = [
        ("loan-calculator","Loan / EMI Calculator","Monthly loan payment","💰"),
        ("compound-interest","Compound Interest","Investment growth","📈"),
        ("salary-calculator","Salary Calculator","Ghana salary
