# AppointmentManagerAPI

AppointmentManagerAPI, randevu yönetimi için geliştirilmiş bir Python REST API uygulamasıdır. Kullanıcılar, hizmet sağlayıcılar ve randevu işlemlerini yönetmek için kullanılır.

## Özellikler

- Kullanıcı yönetimi (kayıt, giriş, güncelleme vb.)
- Hizmet sağlayıcı yönetimi
- Randevu oluşturma, güncelleme ve silme işlemleri
- Temiz, modüler Python mimarisi


## Kurulum

1. **Gereksinimler:**
    - Python 3.8+
    - Gerekli kütüphaneler (ör. Flask, FastAPI veya kullanılan framework)

2. **Bağımlılıkları yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Veritabanı Kurulumu:**
    - `db/` klasörü altında gerekli migration veya setup işlemlerini yapın.
    - (Gerekirse: README’ye özel bir açıklama ekleyebilirsin.)

4. **API’yi başlatın:**
    ```bash
    python main.py
    ```
    veya
    ```bash
    python run_api.py
    ```

5. **API Endpoints**
    - `/users`  : Kullanıcı işlemleri
    - `/providers` : Hizmet sağlayıcı işlemleri
    - `/appointments` : Randevu işlemleri

