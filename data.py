import pandas as pd

dt = pd.read_excel("dataset/intent.xlsx", keep_default_na=False)

intents = []

intents.append(
        {"tag": "greeting",
         "patterns": [i for i in dt['greeting']],
         "responses": ["selamat datang di toko kami"],
        }
)

intents.append(
        {"tag": "product",
         "patterns": [i for i in dt['product']],
         "responses": ["Halo kak, ini daftar produk yang tersedia di toko kami\n----------Daftar Produk----------\n-Celana Dalam\n-Sandal Japit\n-Sepatu Bot\n-Celana Jeans"]
        }
)

intents.append(
        {"tag": "price",
         "patterns": [i for i in dt['price']],
         "responses": ["Halo kak, ini daftar harga di setiap produk yang tersedia di toko kami\n----------Daftar Harga----------\n-Celana Dalam Rp.7000\n-Sandal Japit Rp.8000\n-Sepatu Bot Rp.50000\n-Celana Jeans Rp.80000"]
        }
)

intents.append(
        {"tag": "shipping",
         "patterns": [i for i in dt['shipping']],
         "responses": ["Kami menyediakan jasa pengiriman melalui\n----------Jasa Pengiriman----------\n-JNE\n-J&T\n-Tiki\n-GrabSend\n-GoSend\n-SiCepat\n-Kantor POS"]
        }
)

intents.append(
        {"tag": "payment",
         "patterns": [i for i in dt['payment']],
         "responses": ["Kami menyediakan pembayaran via\n----------Pembayaran----------\n-OVO\n-GoPay\n-DANA\n-M-Banking\n-Indomaret\n-Alfamart"]
        }
)