QA_DATA = [
    # Greetings
    {
        "keywords": ["halo", "hai", "hello", "hi", "hey"],
        "answer": "Halo kak 👋 Lagi cari snack apa nih? Manis atau gurih? 😄",
    },
    {
        "keywords": ["selamat", "pagi", "siang", "sore", "malam"],
        "answer": "Halo kak 👋 Lagi cari snack apa nih? Manis atau gurih? 😄",
    },
    # Thanks
    {
        "keywords": ["makasih", "terima kasih", "thank", "thanks", "thx"],
        "answer": "Sama-sama kak 😊 Selamat ngemil! 🍫🥜 Kalau butuh apa-apa tinggal tanya ya 👍",
    },

    # === PRODUK ===
    # All products
    {
        "keywords": ["produk", "product", "snack", "what", "have", "semua", "list", "apa saja", "ada apa", "jual", "sell", "kategori"],
        "answer": (
            "GarudaFood punya banyak pilihan kak! 😄\n\n"
            "🥜 Kacang – kacang atom, kacang kulit, kacang telur\n"
            "🌽 Pilus – snack jagung bulat, ada yang pedas!\n"
            "🍫 Chocolatos – wafer stick & drink coklat\n"
            "🍪 Gery – biskuit & wafer aneka rasa\n"
            "🥔 Leo – chips kentang & singkong\n"
            "🍫 Beng-Beng – wafer bar coklat caramel\n"
            "🍮 Okky – jelly & minuman buah\n\n"
            "Mau yang mana kak? 😊"
        ),
    },

    # Chocolatos flavors
    {
        "keywords": ["chocolatos", "rasa", "varian", "flavor", "variant", "apa aja", "ada apa"],
        "answer": (
            "Chocolatos ada 2 jenis kak:\n\n"
            "🍫 Wafer Stick: coklat, cappuccino\n"
            "🥤 Drink: coklat original, dark chocolate\n\n"
            "Semua enak, tapi yang wafer stick paling hits! 😄 Mau yang mana?"
        ),
    },
    # Chocolatos general
    {
        "keywords": ["chocolatos", "wafer stick", "coklat stick"],
        "answer": (
            "🍫 Chocolatos itu snack wafer stick coklat yang ringan & crunchy!\n\n"
            "Ada varian wafer stick & drink\n"
            "Harga mulai Rp2.000 aja kak\n\n"
            "Mau tau varian rasanya? 😄"
        ),
    },

    # Kacang flavors
    {
        "keywords": ["kacang", "rasa", "varian", "flavor", "apa aja"],
        "answer": (
            "Kacang GarudaFood ada beberapa varian kak:\n\n"
            "🥜 Kacang Atom – original, pedas\n"
            "🥜 Kacang Kulit – original, rendang\n"
            "🥜 Kacang Telur – gurih, pedas\n\n"
            "Yang paling laris itu kacang atom pedas 🔥 Mau coba?"
        ),
    },
    # Kacang general
    {
        "keywords": ["kacang", "peanut", "kacang garuda"],
        "answer": (
            "🥜 Kacang GarudaFood itu klasik & enak banget!\n\n"
            "Ada kacang atom, kacang kulit, sama kacang telur\n"
            "Tinggi protein, cocok ngemil kapan aja 💪\n\n"
            "Mau yang gurih biasa atau pedas kak?"
        ),
    },

    # Pilus
    {
        "keywords": ["pilus", "jagung", "corn", "bulat"],
        "answer": (
            "🌽 Pilus itu snack jagung bulat yang nagih banget!\n\n"
            "Varian: original, pedas, mie goreng\n"
            "Yang pilus mie goreng lagi hits banget sekarang 🔥\n\n"
            "Mau coba kak?"
        ),
    },

    # Beng-Beng
    {
        "keywords": ["beng-beng", "beng beng", "bengbeng"],
        "answer": (
            "🍫 Beng-Beng ENAK BANGET kak 😆🔥\n\n"
            "• Wafer crunchy berlapis\n"
            "• Caramel di tengah\n"
            "• Dibalut coklat susu\n\n"
            "Ada Original & Maxx (ukuran lebih besar)\n"
            "Best seller nih, langsung checkout aja kak 👍"
        ),
    },

    # Leo
    {
        "keywords": ["leo", "chips", "keripik", "cracker", "kentang", "singkong"],
        "answer": (
            "🥔 Leo Chips itu crunchy & addictive kak!\n\n"
            "Rasa: BBQ, Cheese, Spicy, Original, Seaweed\n"
            "Ada juga dari singkong, lebih kriuk!\n\n"
            "Suka yang rasa apa? 😄"
        ),
    },

    # Gery
    {
        "keywords": ["gery", "biskuit", "biscuit", "cookie"],
        "answer": (
            "🍪 Gery punya banyak pilihan kak!\n\n"
            "• Gery Malkist – crispy berlapis\n"
            "• Gery Saluut – wafer roll coklat\n"
            "• Gery Cheese – gurih keju\n\n"
            "Cocok buat cemilan atau bekal anak 😊"
        ),
    },

    # Okky
    {
        "keywords": ["okky", "jelly", "minuman", "drink"],
        "answer": (
            "🍮 Okky Jelly seger & rendah kalori kak!\n\n"
            "Rasa: strawberry, grape, lychee, orange\n"
            "Ada juga Okky Jelly Drink yang bisa langsung diminum 🥤\n\n"
            "Favorit anak-anak nih 😄"
        ),
    },

    # === PERTANYAAN UMUM ===

    # Spicy or not
    {
        "keywords": ["pedas", "spicy", "pedes", "nggak pedas", "tidak pedas", "ada pedas"],
        "answer": (
            "Ada yang pedas & nggak pedas kak 😊\n\n"
            "🌶️ Yang pedas: kacang atom pedas, pilus pedas, Leo spicy\n"
            "😌 Yang nggak pedas: kacang kulit original, Chocolatos, Beng-Beng\n\n"
            "Suka yang pedas atau yang aman? 😄"
        ),
    },

    # Best seller
    {
        "keywords": ["laris", "best seller", "populer", "hits", "terlaris", "paling", "favorit"],
        "answer": (
            "Best seller GarudaFood nih kak 🔥\n\n"
            "1. 🥜 Kacang Atom – klasik, semua orang suka\n"
            "2. 🍫 Chocolatos – favorit anak muda\n"
            "3. 🌽 Pilus Mie Goreng – lagi hits banget!\n\n"
            "Stok terbatas, langsung checkout aja kak 👍"
        ),
    },

    # Size / isi
    {
        "keywords": ["isi", "ukuran", "size", "banyak", "besar", "kecil", "kemasan", "gram"],
        "answer": (
            "Tergantung kemasannya kak 😊\n\n"
            "📦 Kemasan kecil – buat ngemil harian\n"
            "📦 Kemasan besar – buat sharing atau keluarga\n\n"
            "Mau yang buat sendiri atau buat rame-rame?"
        ),
    },

    # For kids
    {
        "keywords": ["anak", "kids", "anak-anak", "bocah", "balita", "cocok anak"],
        "answer": (
            "Cocok buat anak-anak kak 👍\n\n"
            "Rekomendasi:\n"
            "🍫 Chocolatos – ringan & manis\n"
            "🍮 Okky Jelly – seger & fun\n"
            "🍪 Gery – biskuit yang lembut\n\n"
            "Hindari yang terlalu pedas ya buat anak kecil 😊"
        ),
    },

    # Expired / shelf life
    {
        "keywords": ["expired", "kadaluarsa", "tahan", "lama", "exp", "basi"],
        "answer": (
            "Snack GarudaFood umumnya tahan lama kak 😊\n\n"
            "Cek tanggal kadaluarsa di kemasan ya\n"
            "Simpan di tempat kering & sejuk biar tetap kriuk! 👍"
        ),
    },

    # Ready stock
    {
        "keywords": ["ready", "stok", "stock", "ada", "tersedia", "masih ada"],
        "answer": "Ready kak 👍 Stok masih ada, langsung aja checkout di keranjang kuning sebelum habis! 🛒",
    },

    # Shipping
    {
        "keywords": ["kirim", "pengiriman", "delivery", "kapan", "sampai", "ongkir", "ekspedisi"],
        "answer": (
            "Pengiriman cepat kak! 🚀\n\n"
            "Diproses sesuai antrian order hari ini\n"
            "Bisa pilih ekspedisi sesuai kebutuhan\n\n"
            "Langsung checkout sekarang biar cepet nyampe 😊"
        ),
    },

    # Price
    {
        "keywords": ["harga", "price", "berapa", "cost", "murah"],
        "answer": (
            "Harga produk GarudaFood:\n\n"
            "🥜 Kacang – Rp5.000–35.000\n"
            "🍫 Chocolatos – Rp2.000–5.000\n"
            "🍪 Gery – Rp3.000–15.000\n"
            "🍮 Okky Jelly – Rp1.500–5.000\n"
            "🥔 Leo Chips – Rp5.000–20.000\n"
            "🍫 Beng-Beng – Rp3.000–8.000\n\n"
            "Terjangkau semua kak! Langsung checkout aja 🛒"
        ),
    },

    # Where to buy
    {
        "keywords": ["beli", "where", "toko", "store", "alfamart", "indomaret", "shopee", "tokopedia", "online"],
        "answer": (
            "🛒 Bisa beli di:\n\n"
            "Offline: Indomaret, Alfamart, Hypermart, warung terdekat\n"
            "Online: Tokopedia, Shopee, Lazada – cari 'Garuda Food'\n\n"
            "Tersedia di seluruh Indonesia 🇮🇩"
        ),
    },

    # Halal
    {
        "keywords": ["halal", "mui", "sertifikat"],
        "answer": "✅ Semua produk GarudaFood udah bersertifikat Halal MUI kak! Logo halal ada di setiap kemasan 😊",
    },

    # Nutrition
    {
        "keywords": ["kalori", "nutrition", "gizi", "sehat", "protein", "lemak"],
        "answer": (
            "Info gizi per sajian:\n\n"
            "🥜 Kacang (30g) – ~170 kkal, 7g protein\n"
            "🍫 Chocolatos (1 stick) – ~45 kkal\n"
            "🍮 Okky Jelly (1 cup) – ~80 kkal, 0g lemak\n"
            "🥔 Leo Chips (25g) – ~130 kkal\n"
            "🍫 Beng-Beng (1 bar) – ~130 kkal\n\n"
            "Cek label kemasan untuk info lengkap ya kak 😊"
        ),
    },

    # Sweet recommendation
    {
        "keywords": ["manis", "sweet", "coklat", "chocolate"],
        "answer": (
            "Kalau suka manis, coba ini kak 😊\n\n"
            "🍫 Beng-Beng – wafer + caramel + coklat, best seller!\n"
            "🍫 Chocolatos – wafer stick coklat, ringan & crunchy\n"
            "🍪 Gery Saluut – wafer roll coklat\n\n"
            "Mau yang lebih kenyang atau yang ringan aja?"
        ),
    },

    # Savory
    {
        "keywords": ["gurih", "asin", "savory", "salty"],
        "answer": (
            "Kalau gurih nih rekomendasinya kak 👍\n\n"
            "🥜 Kacang Garuda – classic & protein tinggi\n"
            "🥔 Leo Chips – crispy, banyak rasa\n"
            "🌽 Pilus – snack jagung yang nagih\n\n"
            "Lagi pengen yang pedas atau biasa?"
        ),
    },

    # Closing / push to buy
    {
        "keywords": ["checkout", "beli sekarang", "order", "pesan", "promo", "diskon"],
        "answer": (
            "Yuk kak langsung checkout sekarang! 🛒🔥\n\n"
            "Lagi ada promo & stok terbatas\n"
            "Klik keranjang kuning sebelum kehabisan ya! 😄"
        ),
    },

    # Vague
    {
        "keywords": ["enak", "bagus", "rekomen", "suggest", "saran"],
        "answer": "Hehe banyak pilihannya kak 😄 Lagi pengen yang:\n👉 manis\n👉 gurih\n👉 pedas\n👉 atau ringan buat ngemil?",
    },
]

OUT_OF_SCOPE = (
    "Maaf kak 😊 Aku khusus bantu soal produk snack GarudaFood aja nih\n"
    "Kalau mau rekomendasi snack enak, aku siap bantu! 👌"
)

CLOSING = (
    "Yuk kak langsung checkout! 🛒🔥\n"
    "Lagi promo & stok terbatas, jangan sampe kehabisan ya 😄"
)
