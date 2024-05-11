# Real-Time Face Mask Detection with Streamlit and YOLOv8

#### Link Demo: [FaceMask-Detection](https://facemask-detection-82rvznihkuz6cpffsrl4ay.streamlit.app/)

# How to run locally
## Persyaratan Sistem
- **Sistem Operasi:** Windows, MacOS, atau Linux
- **Python 3.10**
- **Git**
- **Ruang Disk:** Setidaknya 3GB ruang disk yang tersedia

## Pemeriksaan Pra-instalasi

1. **Periksa Instalasi Python:**
   - Buka Command Prompt (cmd).
   - Periksa apakah Python terinstal dengan menjalankan:
     
    ```bash
    python --version
    ```
     
   - Jika Python belum terinstal, unduh dan instal dari [python.org](https://www.python.org/downloads/). Pastikan untuk memilih versi yang kompatibel dengan sistem operasi Anda.

2. **Periksa Instalasi Git:**
   - Periksa apakah Git terinstal dengan menjalankan:
     ```bash
     git --version
     ```
   - Jika Git belum terinstal, unduh dan instal dari [git-scm.com](https://git-scm.com/downloads/).

## Langkah Instalasi

### 3. Navigasi ke Folder Proyek melalui Command Prompt:
   - Ubah direktori saat ini ke folder proyek Anda menggunakan perintah cd.

### 4. Buat Lingkungan Virtual dan Folder Proyek:
   - Buat folder baru dengan nama "facemaskdetection-project" menggunakan perintah berikut:
     ```bash
     mkdir facemaskdetection-project
     ```
   - Navigasi ke folder "facemaskdetection-project":
     ```bash
     cd facemaskdetection-project
     ```
   - Buat lingkungan virtual Python baru dengan nama "your-env-name" menggunakan perintah berikut:
     ```bash
     python -m venv facemaskEnv 
     ```
     atau 
     ```bash
     py -m venv facemaskEnv
     ```
     - Aktifkan lingkungan virtual:
       - Pada Windows:
         ```bash
         .\facemaskEnv\Scripts\activate
         ```
       - Pada MacOS/Linux:
         ```bash
         source facemaskEnv/bin/activate
         ```

Sekarang Anda telah menyiapkan folder proyek bernama "facemaskdetection-project" dengan lingkungan virtual Python bernama "facemaskEnv" Selanjutnya, lanjutkan dengan langkah instalasi yang tersisa dalam folder proyek ini.

### 5. Clone Berkas Proyek:
   - Klona repositori proyek yang berisi file notebook, model, dan skrip Streamlit dari GitHub dengan perintah berikut:
     ```bash
     git clone https://github.com/dinosptr/facemask-detection.git
     ```
   - Navigasi ke folder repositori yang telah di-clone:
     ```bash
     cd facemask-detection
     ```

### 6. Install Project Dependencies:
   - Install the project's required dependencies using pip and the provided requirements.txt file:
     ```bash
     pip install -r requirements.txt
     ```

### 7. Run the Streamlit App:
To launch the Streamlit application, execute the following command in the project directory:


```bash
streamlit run Welcome.py

```
After the command to run the Streamlit script, a new line is added informing the user that they will be directed to open the app in their web browser at localhost:8501.

### 8. Tampilan Website
![Alt text](assets/website_display.png)

# Contoh output Image
![Alt text](assets/result.jpg)
![Alt text](assets/result_2.jpg)
