from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>KV Website ❤️</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        body {
            margin: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #090018, #35105b, #08001c);
            color: white;
            text-align: center;
            overflow: hidden;
        }

        .card {
            padding: 35px 25px;
            width: 85%;
            max-width: 420px;
            border: 1px solid #b66cff;
            border-radius: 25px;
            background: rgba(255,255,255,0.08);
            box-shadow: 0 0 30px #a020f0;
        }

        h1 {
            color: #ff69b4;
            font-size: 32px;
        }

        h2 {
            color: #ffffff;
        }

        .heart {
            font-size: 55px;
            animation: beat 1s infinite;
        }

        @keyframes beat {
            50% { transform: scale(1.3); }
        }

        button {
            padding: 12px 22px;
            margin: 10px;
            border: none;
            border-radius: 25px;
            background: #d946ef;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }

        a {
            text-decoration: none;
        }

        footer {
            margin-top: 25px;
            color: #d8b4fe;
        }
    </style>
</head>

<body>
    <div class="card">
        <div class="heart">❤️</div>

        <h1>I LOVE YOU MACHA</h1>
        <h2>I AM KV 😎</h2>

        <p>Welcome to my personal website!</p>

        <a href="https://www.instagram.com/" target="_blank">
            <button>Instagram</button>
        </a>

        <a href="https://www.whatsapp.com/" target="_blank">
            <button>WhatsApp</button>
        </a>

        <footer>Made with ❤️ by KV</footer>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)