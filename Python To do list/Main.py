
#Inisialisasi list kosong
tasks = []


#Untuk membuka menu
def main_menu():
    while True:
      print("\n Menu")  
      print("1. Lihat tugas. ")
      print("2. tambah tugas. ")
      print("3. Hapus tugas. ")
      print("4. Keluar. ")
    
      pilihan = input("Tentukan pilihan: ")
    
      if pilihan == '1':
          lihat_tugas()
    
      elif pilihan == '2':
          add_task()
        
      elif pilihan == '3':
            hapus_tugas()
    
      elif pilihan == '4':
           print("Program akan ditutup. ")
           break
      else:
          print("Invalid.Silahkan coba lagi.")


#Tambah tugas

def add_task():
    nama_tugas = input("Masukkan nama tugas: ")
    tenggat = input("Masukkan deadline(DD-MM-YYYY): ")
    status = input("Apakah sudah selesai? y/n: ")
    
    task = {"Nama": nama_tugas,  "Tenggat": tenggat, "selesai" : status == 'y'}
    tasks.append(task)
    print(f"Tugas '{nama_tugas}' berhasil ditambahkan!")
    
#lihat tugas
def lihat_tugas():
    if not tasks:
        print("Tidak ada tugas!")
    else:
        for index, task in enumerate(tasks, 1):
            status = "selesai" if  task["selesai"] else "Belum selesai"
            print(f"{index}. Tugas: {task ['Nama']}, Tenggat: {task['Tenggat']}, Status: {status}")
            
#hapus tugas

def hapus_tugas():
    lihat_tugas()
    index_tugas = int(input("Masukkan nomor tugas yang ingin dihapus: ")) -1
    if 0 <= index_tugas < len(tasks):
        removed_tasks = tasks.pop(index_tugas)
        print(f"Tugas '{removed_tasks['Nama']}' berhasil dihapus!")
    else:
        print("Invalid")


main_menu()
        
input("Enter untuk keluar. ")        


   
        