# Gizli Notlar Uygulaması

Bu depo, Python'ın standart GUI (Grafik Kullanıcı Arayüzü) kütüphanesi olan `tkinter` ve `base64` kullanılarak geliştirilmiş basit bir gizli notlar uygulaması içermektedir. Kullanıcılar, kişisel notlarını oluşturabilir, kaydedebilir ve temel bir şifreleme yöntemiyle koruyabilirler. Şifreleme, kullanıcının belirlediği ana bir paroladan türetilen bir anahtar kullanılarak gerçekleştirilir.

**Uyarı:** Bu uygulamada kullanılan şifreleme temel düzeydedir ve öncelikle kişisel kullanım içindir. Hassas ve kritik veriler için daha güçlü şifreleme yöntemleri kullanılması önerilir.

## Özellikler

* **Kullanıcı Dostu Arayüz:** Basit ve sezgisel bir grafik arayüzü sunar.
* **Not Oluşturma ve Görüntüleme:** Yeni gizli notlar oluşturabilir ve mevcut notları görüntüleyebilirsiniz.
* **Temel Şifreleme:** Notlar, kullanıcının belirlediği ana bir paroladan türetilen bir anahtar kullanılarak şifrelenir.
* **Güvenli Kayıt:** Şifrelenmiş notlar güvenli bir şekilde dosyaya kaydedilir.
* **Kolay Erişim:** Kaydedilmiş notlar, doğru ana parola girilerek kolayca deşifre edilip görüntülenebilir.

## Nasıl Çalıştırılır?

1.  Öncelikle bilgisayarınızda Python 3'ün kurulu olduğundan emin olun.
2.  Bu depoyu bilgisayarınıza klonlayın veya ZIP olarak indirin:
    ```bash
    git clone [https://github.com/ozzencben/SecretNotes.git](https://github.com/ozzencben/SecretNotes.git)
    cd SecretNotes
    ```
    
3.  Uygulamayı çalıştırmak için terminal veya komut istemcisinde şu komutu girin:
    ```bash
    python main.py
    ```

## Kullanım

1.  Uygulama penceresi açıldığında, notlarınızı girmek için metin alanını kullanın.
2.  Notlarınızı şifrelemek ve kaydetmek için "Kaydet ve Şifrele" butonuna tıklayın. Sizden bir ana parola girmeniz istenecektir. Bu parolayı güvenli bir yerde saklayın, çünkü notlarınızı tekrar açmak için bu parolaya ihtiyacınız olacak.
3.  Kaydedilmiş notları açmak için "Notları Çöz" butonuna tıklayın. Sizden ana parolayı girmeniz istenecektir. Doğru parolayı girdiğinizde, notlarınız deşifre edilerek görüntülenecektir.

## Geliştirme Ortamı

Bu uygulama aşağıdaki teknolojiler kullanılarak geliştirilmiştir:

* **Python:** Programlama dili.
* **Tkinter:** Grafik kullanıcı arayüzü (GUI) kütüphanesi (Python'ın standart kütüphanesinde bulunur).
* **base64:** Şifrelenmiş veriyi güvenli bir şekilde saklamak için kullanılan temel bir kodlama kütüphanesi.

## Şifreleme Hakkında

Bu uygulamada kullanılan şifreleme, karakter tabanlı basit bir şifreleme algoritmasıdır ve temel bir anahtar (ana paroladan türetilir) kullanır. Güvenlik açısından güçlü bir şifreleme yöntemi değildir ve karmaşık saldırılara karşı savunmasız olabilir. Bu uygulama öncelikle kişisel notların temel düzeyde korunması amacıyla tasarlanmıştır. Hassas ve kritik veriler için daha güvenli ve standart şifreleme kütüphanelerinin (örneğin `cryptography` kütüphanesi) kullanılması önerilir.

## Katkılar

Bu basit bir kişisel proje olsa da, eğer fikirlenirseniz veya katkıda bulunmak isterseniz çekinmeyin! Hata bildirimleri ve iyileştirme önerileri memnuniyetle karşılanır. Katkıda bulunmak için lütfen aşağıdaki adımları izleyin:

1.  Bu depoyu fork'layın.
2.  Kendi branch'inizi oluşturun (`git checkout -b feature/yeni-ozellik`).
3.  Değişikliklerinizi commit'leyin (`git commit -am 'Yeni özellik eklendi'`).
4.  Kendi branch'inize push'layın (`git push origin feature/yeni-ozellik`).
5.  Pull request oluşturun.

## Lisans

Bu proje altında herhangi bir özel lisans belirtilmemiştir. Aksi belirtilmediği sürece, kodun kullanımı ve dağıtımı konusunda dikkatli olun.

## İletişim

Herhangi bir sorunuz veya geri bildiriminiz için benimle [ozzencben@gmail.com] üzerinden iletişime geçebilirsiniz.

---

Gizli notlarınızı güvenle saklamanız dileğiyle! 🗝️
