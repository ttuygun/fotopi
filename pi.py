#!/usr/bin/python
from subprocess import call
import time
import glob
import os
import shutil

while True:
	miktar = subprocess.Popen(["df", "-h", "/"], stdout=subprocess.PIPE) #Bos-alan-tesbit-komutu
	yuzde = miktar.stdout.readlines(2) #komutdan-satir-okumak-icin
	yuzde = str(yuzde) #string etmek icin
	yuzde = yuzde.split() #satirlara ayirma gerekli cunku variable[number] okumasi yapilamiyor

	for satir in yuzde:
		if "%" in satir:
			yuzde = satir

	yuzde = yuzde[:-1] #7% degerini 7 integerine donusturmesi icin
	yuzde = int(yuzde)

   if yuzde > 15: #Niye %15; hem %20 performans tavsiyesine yakin ve 8gb sd kart icin 1.23 gb bos alani temin ettiği icin
   		for slnckdsy in sorted(glob.glob("Print/*.JPG"))[0:50]:
			#İsm(dlysyla tarih) srsina göre ilk 51 dosyayi silr; ~250 mb yer acar
       		os.remove("%s" % slnckdsy)
       		os.remove("./preview/%s" % slnckdsy)

   call(["gphoto2", "-P", "--skip-existing"])

   for path in glob.glob("./*.JPG"):
	   src = path[2:]
       if os.path.getsize(src): #boyutu varsa;
           os.system('convert %s -resize x200 -quality 20 preview/%s' % (src, src)) #boyutlu dosyanın preview imajini gonderir
           dst = "/var/www/html/print/"
           os.system("mv %s %s" %(src, dst))
           os.mknod(path[2:])
           dstpath = dst + src
           if "-p" not in dstpath:
               os.system('lp -d sanalyazici %s' % dstpath)
               #call([("lp", "-d", "sanalyazici", str(path)])
               os.rename(dstpath, (dstpath[:-4]+"-p.JPG"))
   print "Kameradan fotograf bekleniyor..."
   time.sleep(10)
   #break
