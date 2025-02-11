import requests
import sys

  ##examplesub.txt dosyasının yolu belirtilmeli, örneğin: "/subdomains/examplesub.txt"
sub_list = open("./subdomains/examplesub.txt").read()  ## .txt dosyası ayarlanabilir veya değiştirilebilir.  ( .txt can be change.)
subdoms = sub_list.splitlines()                       


def main():
    for sub in subdoms:
        sub_domains = f"https://{sub}.{sys.argv[1]}"

        try:
            requests.get(sub_domains)

        except requests.ConnectionError:
            pass

        else:
            print("Valid domain: ", sub_domains)


if __name__ == "__main__":
    main()
