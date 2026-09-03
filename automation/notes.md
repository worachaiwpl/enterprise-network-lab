\# Netmiko Connection Test



\## เป้าหมาย

ทดสอบว่า Python + Netmiko เชื่อมต่อ SSH ไปยัง Cisco router ใน EVE-NG ได้จริง



\## ผลลัพธ์

เชื่อมต่อสำเร็จ ดึงผลลัพธ์ show version ได้ครบถ้วน



\## ปัญหาที่เจอ / วิธีแก้

\- native ssh command บนเครื่อง host ขึ้น error "no matching key exchange method found" 

&#x20; เพราะ OpenSSH เวอร์ชันใหม่ปิด algorithm รุ่นเก่า (diffie-hellman-group1-sha1) ที่ Cisco IOS/IOL ใช้

\- แก้ด้วย: ssh -oKexAlgorithms=+diffie-hellman-group14-sha1 (สำหรับ manual SSH)

\- Netmiko/Paramiko ไม่เจอปัญหานี้ เชื่อมต่อผ่านได้ปกติโดยไม่ต้องปรับอะไรเพิ่ม

