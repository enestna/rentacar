# database.py

import mysql.connector


DB_OKUL_NUMARASI = "90240000227"
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "deneme"
DB_PORT = 3306
DB_NAME = f"db{DB_OKUL_NUMARASI}"

def get_db_connection(database=None):
    """MySQL sunucusuna bağlantı kurar."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
            database=database if database else "",
            use_pure=True
        )
        return conn
    except mysql.connector.Error as err:
        print(f"HATA: MySQL Bağlantı Hatası! Hata: {err}")
        return None

def fix_table_columns():
    """Tablo yapısını onarır ve eksik sütunları (menzil, indirim) ekler."""
    conn = get_db_connection(database=DB_NAME)
    if conn is None: return
    cursor = conn.cursor()
    try:

        try:
            cursor.execute("ALTER TABLE araclar MODIFY cekis VARCHAR(50)")
        except: pass


        try:
            cursor.execute("ALTER TABLE araclar ADD COLUMN menzil INT DEFAULT NULL")
            print("BİLGİ: 'menzil' sütunu araclar tablosuna eklendi.")
        except: pass


        try:
            cursor.execute("ALTER TABLE kiralamalar ADD COLUMN indirim DECIMAL(10, 2) DEFAULT 0.00")
            print("BİLGİ: 'indirim' sütunu kiralamalar tablosuna eklendi.")
        except: pass

        conn.commit()
    except:
        pass
    finally:
        cursor.close()
        conn.close()

def add_sample_data():
    """Tablolar boşsa otomatik olarak örnek kayıt ekler."""
    conn = get_db_connection(database=DB_NAME)
    if conn is None: return
    cursor = conn.cursor()

    try:

        cursor.execute("SELECT COUNT(*) FROM musteriler")
        if cursor.fetchone()[0] == 0:
            print("BİLGİ: Örnek müşteriler ekleniyor...")
            sql_musteri = """
            INSERT INTO musteriler (ad, soyad, tc_kimlik, dogum_tarihi, adres, telefon_ev, telefon_cep, meslek, ehliyet_sinifi, medeni_durum, egitim_durumu)
            VALUES
            ('yusuf', 'islam', '11234567845', '1990-01-01', 'İzmir', '02321111111', '05551111345', 'Mühendis', 'B', 'Bekar', 'Lisans'),
            ('samet', 'sayım', '24568876534', '1995-05-15', 'İstanbul', '02122222222', '0555245222', 'Doktor', 'B', 'Evli', 'Yüksek Lisans'),
            ('enes', 'tuna', '12345678910', '1985-08-20', 'Ankara', '03123333333', '0555333453', 'Öğretmen', 'E', 'Evli', 'Lisans')
            """
            cursor.execute(sql_musteri)
            conn.commit()


        cursor.execute("SELECT COUNT(*) FROM araclar")
        if cursor.fetchone()[0] == 0:
            print("BİLGİ: Örnek araçlar  ekleniyor...")
            sql_arac = """
            INSERT INTO araclar (arac_turu, marka, model, uretim_yili, yakit_turu, vites, motor_gucu, kasa_tipi, motor_hacmi, cekis, kapi_sayisi, renk, motor_no, sasi_no, gunluk_bedel, kirada, kullanim_disi, menzil)
            VALUES
            ('Otomobil', 'Mercedes', 'Benz', 2023, 'Benzin', 'Manuel', 95, 'Sedan', 1400, 'Önden Çekiş', 4, 'Beyaz', 'MTR001', 'SAS001', 1500.00, 0, 0, NULL),
            ('Otomobil', 'TOGG', 'T10X', 2024, 'Elektrik', 'Otomatik', 160, 'SUV', 0, 'Arkadan İtiş', 5, 'Kırmızı', 'MTR002', 'SAS002', 2000.00, 0, 0, 523),
            ('Arazi Aracı', 'Ford', 'Ranger', 2024, 'LPG', 'Manuel', 110, 'SUV', 1600, '4x4', 5, 'Siyah', 'MTR003', 'SAS003', 2500.00, 0, 0, NULL)
            """
            cursor.execute(sql_arac)
            conn.commit()

    except mysql.connector.Error as err:
        print(f"HATA: Örnek veri eklenirken sorun oluştu: {err}")
    finally:
        cursor.close()
        conn.close()

def create_database_and_tables():
    """Veritabanını ve tabloları oluşturur."""

    conn = get_db_connection()
    if conn is None: return

    cursor = conn.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci")
        print(f"BİLGİ: Veritabanı '{DB_NAME}' kontrol edildi.")
    except mysql.connector.Error as err:
        print(f"HATA: Veritabanı oluşturma başarısız: {err}")
        conn.close()
        return

    conn.close()
    conn = get_db_connection(database=DB_NAME)
    if conn is None: return

    cursor = conn.cursor()

    queries = [
        """
        CREATE TABLE IF NOT EXISTS musteriler (
            musteri_id INT AUTO_INCREMENT PRIMARY KEY, ad VARCHAR(50) NOT NULL, soyad VARCHAR(50) NOT NULL,
            tc_kimlik VARCHAR(11) UNIQUE NOT NULL, dogum_tarihi DATE, adres VARCHAR(255),
            telefon_ev VARCHAR(20), telefon_cep VARCHAR(20), meslek VARCHAR(50),
            ehliyet_sinifi VARCHAR(10), medeni_durum VARCHAR(20), egitim_durumu VARCHAR(50)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS araclar (
            arac_id INT AUTO_INCREMENT PRIMARY KEY, arac_turu VARCHAR(50) NOT NULL, marka VARCHAR(50) NOT NULL,
            model VARCHAR(50) NOT NULL, uretim_yili INT, yakit_turu VARCHAR(20), vites VARCHAR(20),
            motor_gucu INT, kasa_tipi VARCHAR(50), motor_hacmi INT, cekis VARCHAR(50), kapi_sayisi INT,
            renk VARCHAR(30), motor_no VARCHAR(50) UNIQUE, sasi_no VARCHAR(50) UNIQUE NOT NULL,
            gunluk_bedel DECIMAL(10, 2) NOT NULL, kirada BOOLEAN DEFAULT FALSE, kullanim_disi BOOLEAN DEFAULT FALSE,
            menzil INT DEFAULT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS kiralamalar (
            kiralama_id INT AUTO_INCREMENT PRIMARY KEY, musteri_id INT NOT NULL, arac_id INT NOT NULL,
            kiralama_tarihi DATE NOT NULL, kiralanan_gun INT NOT NULL, yolculuk_nereye VARCHAR(255),
            toplam_ucret DECIMAL(10, 2) NOT NULL,
            indirim DECIMAL(10, 2) DEFAULT 0.00,
            teslim_tarihi DATE NULL,
            FOREIGN KEY (musteri_id) REFERENCES musteriler(musteri_id),
            FOREIGN KEY (arac_id) REFERENCES araclar(arac_id)
        )
        """
    ]

    try:
        for query in queries:
            cursor.execute(query)
        print("BİLGİ: Tablolar kontrol edildi.")
        conn.commit()

        fix_table_columns()
        add_sample_data()

    except mysql.connector.Error as err:
        print(f"HATA: Tablo işlemleri başarısız: {err}")

    cursor.close()
    conn.close()
