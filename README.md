# Subdomain Finder

Bu araç, belirli bir ana domain için geçerli alt domainleri (subdomain) bulur. `subdomains.txt` dosyasındaki potansiyel alt domain listesini okur, her alt domain için URL'ler oluşturur ve HTTP istekleri göndererek geçerli olup olmadıklarını kontrol eder.

## Gereksinimler

- Python 3.x
- "requests" kütüphanesi
- "sys"      kütüphanesi

**Kütüphaneleri yüklemek için aşağıdaki komutlardan birini kullanabilirsiniz:**

pip install requests, sys             

pip install -r requirements.txt


**Alt domain listesini hazırlayın:**

    Script ile aynı dizinde `subdomains.txt` adında bir dosya oluşturun. Bu dosya, her satırda bir alt domain olacak şekilde yazılmalıdır. Örneğin:

    ```
    www
    blog
    mail
    dev
    ```

 **Script'i çalıştırın:**

    Terminal veya komut istemcisini açın ve aşağıdaki komutu kullanın. `example.com` yerine hedef domaininizi yazın:

    ```bash
    python find_subdomains.py example.com
    ```