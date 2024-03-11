#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE D3_TI_2023")


# In[10]:


import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database = "D3_TI_2023"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
  
# creating table
tabelMataKuliah = """CREATE TABLE Mata_Kuliah (
                   Kode_Mata_Kuliah VARCHAR(10) NOT NULL PRIMARY KEY,
                   Nama_Mata_Kuliah  VARCHAR(50) NOT NULL,
                   Waktu DATE,
                   Ruangan VARCHAR (10)
                   )"""
  
# table created
cursorObject.execute(tabelMataKuliah)
  
# disconnecting from server
dataBase.close()


# In[11]:


import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database = "D3_TI_2023"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
  
# creating table
tabelMataKuliah = """CREATE TABLE Mata_Kuliah (
                   Nim VARCHAR(10) NOT NULL PRIMARY KEY,
                   Nama_Mahasiswa VARCHAR(30) NOT NULL,
                   Alamat VARCHAR(255),
                   Mata_Kuliah_Diikuti VARCHAR(10),
                   FOREIGN KEY(Mata_Kuliah_Diikuti) REFERENCES Mata_Kuliah(Kode_Mata_Kuliah)
                   )"""
  
# table created
cursorObject.execute(tabelMahasiswa)
  
# disconnecting from server
dataBase.close()


# In[13]:


import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database = "D3_TI_2023"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
  
# creating table
tabelMataKuliah = """CREATE TABLE Dosen (
                   Nip VARCHAR(20) NOT NULL PRIMARY KEY,
                   Nama_Dosen VARCHAR(50) NOT NULL,
                   Mata_Kuliah_Ajar VARCHAR(50),
                   FOREIGN KEY(Mata_Kuliah_Ajar) REFERENCES Mata_Kuliah(Kode_Mata_Kuliah)
                   )"""
  
# table created
cursorObject.execute(tabelDosen)
  
# disconnecting from server
dataBase.close()


# In[ ]:




