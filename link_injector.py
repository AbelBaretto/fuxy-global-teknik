import os
import re

# Peta kata kunci dan link tujuan (Bos Abel bisa tambah atau ubah daftarnya di sini)
LINK_MAPS = {
    r"\b(service servo|servo motor|overhaul servo)\b": '<a href="https://www.fuxiglobalteknik.com/2026/06/jasa-service-servo-motor-servo-drive.html" target="_blank">\\1</a>',
    r"\b(inverter|vfd|variable frequency drive)\b": '<a href="https://www.fuxiglobalteknik.com/search/label/Inverter" target="_blank">\\1</a>',
    r"\b(rewinding servo|gulung dinamo|rewinding stator)\b": '<a href="https://www.fuxiglobalteknik.com/search/label/Service%20Servo" target="_blank">\\1</a>',
    r"\b(penyebab motor servo overheat)\b": '<a href="https://www.fuxiglobalteknik.com/2026/06/penyebab-servo-motor-overheat-dan-cara.html" target="_blank">\\1</a>',
    r"\b(proses rewinding motor servo)\b": '<a href="https://www.fuxiglobalteknik.com/2026/06/bedah-proses-rewinding-motor-servo.html" target="_blank">\\1</a>',
    r"\b(jasa perbaikan ac spindle motor servo)\b": '<a href="https://www.fuxiglobalteknik.com/2026/06/jasa-perbaikan-ac-spindle-motor-servo.html" target="_blank">\\1</a>',
    r"\b(jasa repair servo motor)\b": '<a href="https://www.fuxiglobalteknik.com/2026/06/jasa-maintenance-repair-servo.html" target="_blank">\\1</a>',
    r"\b(pengadaan unit baru servo motor dan servo drive)\b": '<a href="https://www.fuxiglobalteknik.com/2026/06/pengadaan-unit-baru-servo-motor-drive.html" target="_blank">\\1</a>',
    r"\b(jasa repair inverter industri)\b": '<a href="https://www.fuxiglobalteknik.com/2026/06/jasa-repair-inverter-industri.html" target="_blank">\\1</a>',
    r"\b(jasa service serno motor di indonesia)\b": '<a href="https://www.fuxiglobalteknik.com/2026/06/jasa-service-servo-motor-di-indonesia.html" target="_blank">\\1</a>',
    r"\b(jasa service serno drive di indonesia)\b": '<a href="https://www.fuxiglobalteknik.com/2026/06/jasa-service-servo-drive-di-indonesia.html" target="_blank">\\1</a>'
}

TARGET_DIR = 'articles'

def inject_links_to_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    
    # Lakukan pencarian dan penggantian kata kunci berdasarkan map di atas
    for pattern, replacement in LINK_MAPS.items():
        # Menggunakan regex compile untuk pencarian yang tidak sensitif huruf besar/kecil (case-insensitive)
        regex = re.compile(pattern, re.IGNORECASE)
        
        # Cek apakah kata kunci ada dan BELUM dibungkus oleh tag anchor <a>
        if regex.search(content):
            # Logika sederhana agar tidak menimpa kata yang sudah menjadi link
            # Skrip hanya mengganti teks murni yang berdiri bebas
            new_content = regex.sub(replacement, content)
            if new_content != content:
                content = new_content
                modified = True

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[SUCCESS] Link berhasil ditanam di: {file_path}")

def main():
    if not os.path.exists(TARGET_DIR):
        print(f"Folder '{TARGET_DIR}' tidak ditemukan.")
        return

    # Pindai semua file di dalam folder target
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith('.html') or file.endswith('.md'):
                file_path = os.path.join(root, file)
                inject_links_to_file(file_path)

if __name__ == "__main__":
    main()
