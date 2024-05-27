### DATA KONTAK TELEFON - PERSONAL INFO - CHELSEA FC PLAYERS###
daftarKontakTelepon = [
    {
        'ID' : '28',
        'Name' : 'Djordje Petrovic',
        'Phone Number' : '081234567890',
        'Email' : 'djordjepetrovic@chelsea.co.uk',
        'Position' : 'Goal Keeper',
        'National Team' : 'Serbia'
    },
    {
        'ID' : '6',
        'Name' : 'Thiago Silva',
        'Phone Number' : '081378910834',
        'Email' : 'thiagosilva@chelsea.co.uk',
        'Position' : 'Center-Back',
        'National Team' : 'Brazil'
    },
    {
        'ID' : '23',
        'Name' : 'Conor Gallagher',
        'Phone Number' : '081526781093',
        'Email' : 'conor.gallagher@chelsea.co.uk',
        'Position' : 'Midfielder',
        'National Team' : 'England'
    },
    {
        'ID' : '10',
        'Name' : 'Mykhailo Mudryk',
        'Phone Number' : '082176893561',
        'Email' : 'misha.mudryk@chelsea.co.uk',
        'Position' : 'Winger',
        'National Team' : 'Ukraine'
    },
    {
        'ID' : '20',
        'Name' : 'Cole Palmer',
        'Phone Number' : '085198032784',
        'Email' : 'cold.palmer@chelsea.co.uk',
        'Position' : 'Attacking Midfielder//Winger',
        'National Team' : 'England'
    },
]

daftarKontakTeleponUpdate = daftarKontakTelepon.copy()
ID = 0
# ----------------------------------------------------------------------------------------------------------------------#
## FUNCTION READ ##
def readData():
    print('''
    -------- MENAMPILKAN DATA KONTAK TELEPON & PERSONAL INFO --------

        1. Menampilkan Data Kontak & Personal Info Seluruh Pemain
        2. Menampilkan Daftar ID Seorang Pemain
        3. Menampilkan Nama Lengkap Seorang Pemain
        4. Menampilkan Kontak Telpon Seorang Pemain
        5. Menampilkan Email Seorang Pemain
        6. Menampilkan Posisi Seorang Pemain
        7. Menampilkan Kewarganegaraan Seorang Pemain
        8. Kembali ke Main Menu
    
    -----------------------------------------------------------------
    ''')
    subOption = input(  'Select Sub-Menu1-8!    ')
    if subOption == '1':
        if len(daftarKontakTeleponUpdate) == 0:
            print('\n   DATA TIDAK DITEMUKAN!   ')
            readData()
        else:
            for player in daftarKontakTeleponUpdate:
                print(f"ID: {player['ID']}, Nama: {player['Name']}, Telepon: {player['Phone Number']}, Email: {player['Email']}, Posisi: {player['Position']}, Tim Nasional: {player['National Team']}")
            readData()
    elif subOption == '2':
        if len(daftarKontakTeleponUpdate) == 0:
            print('\n   DATA TIDAK DITEMUKAN!   ')
            readData()
        else:
            ID = input('Masukkan ID Pemain: ')
            found = False
            for player in daftarKontakTeleponUpdate:
                if player['ID'] == ID:
                    print(f"\n      Berikut data seorang pemain yang memiliki ID {ID}:")
                    print(f"ID: {player['ID']}, Nama: {player['Name']}, Telepon: {player['Phone Number']}, Email: {player['Email']}, Posisi: {player['Position']}, Tim Nasional: {player['National Team']}")
                    found = True
                    break
            if not found:
                print('\n   DATA TIDAK DITEMUKAN!   ')
            readData()

    elif subOption == '3':
        if len(daftarKontakTeleponUpdate) == 0:
            print('\n   DATA TIDAK DITEMUKAN!   ')
            readData()
        else:
            ID = input('Masukkan ID Pemain: ')
            found = False
            for player in daftarKontakTeleponUpdate:
                if player['ID'] == ID:
                    print(f"\n      Nama Lengkap Pemain dengan ID {ID} adalah: {player['Name']}")
                    found = True
                    break
            if not found:
                print('\n   DATA TIDAK DITEMUKAN!   ')
            readData()     

    elif subOption == '4':
        if len(daftarKontakTeleponUpdate) == 0:
            print('\n   DATA TIDAK DITEMUKAN!   ')
            readData()
        else:
            ID = input('Masukkan ID Pemain: ')
            found = False
            for player in daftarKontakTeleponUpdate:
                if player['ID'] == ID:
                    print(f"\n      Kontak Telpon Pemain dengan ID {ID} adalah: {player['Phone Number']}")
                    found = True
                    break
            if not found:
                print('\n   DATA TIDAK DITEMUKAN!   ')
            readData()
    elif subOption == '5':
        if len(daftarKontakTeleponUpdate) == 0:
            print('\n   DATA TIDAK DITEMUKAN!   ')
            readData()
        else:
            ID = input('Masukkan ID Pemain: ')
            found = False
            for player in daftarKontakTeleponUpdate:
                if player['ID'] == ID:
                    print(f"\n      Email Pemain dengan ID {ID} adalah: {player['Email']}")
                    found = True
                    break
            if not found:
                print('\n   DATA TIDAK DITEMUKAN!   ')
            readData()

    elif subOption == '6':
        if len(daftarKontakTeleponUpdate) == 0:
            print('\n   DATA TIDAK DITEMUKAN!   ')
            readData()
        else:
            ID = input('Masukkan ID Pemain: ')
        found = False
        for player in daftarKontakTeleponUpdate:
            if player['ID'] == ID:
                print(f"\n      Posisi Pemain dengan ID {ID} adalah: {player['Position']}")
                found = True
                break
        if not found:
            print('\n   DATA TIDAK DITEMUKAN!   ')
        readData()
            
    elif subOption == '7':
        if len(daftarKontakTeleponUpdate) == 0:
            print('\n   DATA TIDAK DITEMUKAN!   ')
            readData()
        else:
            ID = input('Masukkan ID Pemain: ')
        found = False
        for player in daftarKontakTeleponUpdate:
            if player['ID'] == ID:
                print(f"\n      Kewarganegaraan Pemain dengan ID {ID} adalah: {player['National Team']}")
                found = True
                break
        if not found:
            print('\n   DATA TIDAK DITEMUKAN!   ')
        readData()
    
    elif subOption == '8':
            main_menu()
    else:
        print('\n   INVALID ANSWER!   ')
        readData()
# ----------------------------------------------------------------------------------------------------------------------#
## FUNCTION CREATE ##
def createData():
    print('''
    -------- MENAMBAHKAN DAFTAR KONTAK TELEPON & PERSONAL INFO --------

    1. Menambahkan Daftar Kontak Telepon & Personal Info
    2. Kembali ke Main Menu
    -------------------------------------------------------------------
    ''')
    subOption = input('Pilih Sub-Menu 1-2: ')
    if subOption == '1':
        newID = input('Masukkan ID Pemain: ')
        newName = input('Masukkan Nama Pemain: ')
        newPhoneNumber = input('Masukkan Nomor Telepon Pemain: ')
        newEmail = input('Masukkan Email Pemain: ')
        newPosition = input('Masukkan Posisi Pemain: ')
        newNationalTeam = input('Masukkan Tim Nasional Pemain: ')

        newPlayer = {
            'ID': newID,
            'Name': newName,
            'Phone Number': newPhoneNumber,
            'Email': newEmail,
            'Position': newPosition,
            'National Team': newNationalTeam
        }

        daftarKontakTeleponUpdate.append(newPlayer)
        print('\nData pemain baru telah berhasil ditambahkan!')
        createData()
    elif subOption == '2':
        main_menu()
    else:
        print('\nPilihan tidak valid, silakan coba lagi.')
        createData()       
# ----------------------------------------------------------------------------------------------------------------------#
## FUNCTION UPDATE ##

def updateData():
    print('''
    -------- MENGUBAH ID NOMOR TELEPON & EMAIL PEMAIN --------
    
    1. Mengubah ID Pemain
    2. Mengubah Nomor Telepon Pemain
    3. Mengubah Email Seorang Pemain
    4. Kembali ke Main Menu
    ----------------------------------------------------------
    ''')
    subOption = input('Pilih Sub-Menu 1-2: ')
    if subOption == '1':
        oldID = input('Masukkan ID Pemain yang ingin diubah: ')
        newID = input('Masukkan ID Pemain baru: ')
        found = False
        for player in daftarKontakTeleponUpdate:
            if player['ID'] == oldID:
                player['ID'] = newID
                print(f'\nID pemain telah berhasil diubah menjadi {newID}!')
                updateData()
                found = True
                break
        if not found:
            print('\n   DATA TIDAK DITEMUKAN!   ')
            updateData()
    elif subOption == '2':
        oldID = input('Masukkan ID Pemain yang ingin diubah nomor teleponnya: ')
        newPhoneNumber = input('Masukkan Nomor Telepon Baru: ')
        found = False
        for player in daftarKontakTeleponUpdate:
            if player['ID'] == oldID:
                player['Phone Number']
                print(f'\n Nomor Telepon Pemain Telah Berhasil Diubah menjadi {newPhoneNumber}! ')
                updateData()
                found = True
                break
        if not found:
            print('\n   DATA TIDAK DITEMUKAN!   ')
            updateData()
    elif subOption == '3':
        oldID = input('Masukkan ID Pemain yang ingin diubah emailnya: ')
        newEmail = input('Masukkan Email Baru: ')
        found = False
        for player in daftarKontakTeleponUpdate:
            if player['ID'] == oldID:
                player['Email'] = newEmail
                print(f'\nEmail Pemain telah berhasil diubah menjadi {newEmail}!')
                updateData()
                found = True
                break
        if not found:
            print('\n   DATA TIDAK DITEMUKAN!   ')
            updateData()        
    elif subOption == '4':
        main_menu()
    else:
        print('\nPilihan tidak valid, silakan coba lagi.')
        updateData()
# ----------------------------------------------------------------------------------------------------------------------#
## FUNCTION DELETE ##

def deleteData():
    print('''
    -------- MENGHAPUS DATA KONTAK TELEPON & PERSONAL INFO --------
    
    1. Menghapus Data Kontak Telepon & Personal Info
    2. Kembali ke Main Menu
    ---------------------------------------------------------------
    ''')
    subOption = input('Pilih Sub-Menu 1-2: ')
    if subOption == '1':
        ID = input('Masukkan ID Pemain yang ingin dihapus: ')
        found = False
        for index, player in enumerate(daftarKontakTeleponUpdate):
            if player['ID'] == ID:
                del daftarKontakTeleponUpdate[index]
                print(f'\nData pemain dengan ID {ID} telah berhasil dihapus!')
                deleteData()
                found = True
                break
        if not found:
            print('\n   DATA TIDAK DITEMUKAN!   ')
    elif subOption == '2':
        main_menu()
    else:
        print('\nPilihan tidak valid, silakan coba lagi.')
        deleteData()
# ----------------------------------------------------------------------------------------------------------------------#
## FUNCTION EXIT PROGRAM ##

def exitprogram():
    print("\nAnda telah keluar dari program. Terima kasih telah menggunakan aplikasi ini.")
    ()
# ----------------------------------------------------------------------------------------------------------------------#
## FUNCTION MAIN MENU ##
def main_menu():
    print('''
------------------------------------------------------------------
Selamat Datang di Data Kontak Telepon & Personal Info Chelsea FC !          

Main Menu Option:
1. Menampilkan Daftar Data Kontak Telepon & Personal Info
2. Menambah Data Kontak Telepon & Personal Info
3. Mengubah Data Kontak Telepon & Personal Info
4. Menghapus Data Kontak Telepon & Personal Info
5. Keluar Dari Program Data Kontak Telepon & Personal Info
------------------------------------------------------------------         
    ''')

    main_option = input('Input Main Menu Option 1-5: ')

    if main_option == '1':
        readData()
    elif main_option == '2':
        createData()
    elif main_option == '3':
        updateData()
    elif main_option == '4':
        deleteData()
    elif main_option == '5':
        exitprogram()
    else:
        print('\n Pilihan tidak valid, silakan coba lagi.')
        main_menu()

main_menu()