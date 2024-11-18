import urllib.request

def get_public_ip():
    try:
        # ارسال درخواست به API برای دریافت آدرس IP عمومی
        public_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
        print(f'آدرس IP عمومی شما: {public_ip}')
    except Exception as e:
        # در صورت بروز خطا، پیام خطا را چاپ می‌کند
        print(f'خطایی رخ داده است: {e}')

if __name__ == "__main__":
    get_public_ip()
