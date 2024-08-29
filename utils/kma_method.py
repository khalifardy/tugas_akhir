import numpy as np
import math

class KomodoMlipirAlgorithm:
    """
    Implementasi Algoritma Komodo Mlipir Algorithm
    metode oleh : Prof. Dr. Suyanto, S.T., M.Sc. (2021)
    code python oleh : Pejalan Sunyi (2024)
    
    Parameter init:
    n : jumlah populasi
    p : proposi penjantan besar
    d : mlipir rate
    fitness_function : fungsi fitness yang akan dioptimalkan
    space_search : batasan pencarian
    max_iter : jumlah iterasi
    info_katogorikal_tipe : tipe data kategorikal
    
    """
    
    def __init__(self, n:int, p:float, d:float, fitness_function:callable , space_search:dict, max_iter:int, info_katogorikal_tipe:list):
        self.n = n
        self.p = p
        self.d = d
        self.fitness_function = fitness_function
        self.space_search = space_search
        self.max_iter = max_iter
        self.info_katogorikal_tipe = info_katogorikal_tipe
        self.populasi_komodo = []
        self.jb = None
        self.jk = None
        self.betina = None
        self.jb_fitness = None
        self.jk_fitness = None
        self.betina_fitness = None
        self.kategorikal_index = []
        
    
    def jantan_besar(self):
        # fungsi untuk mendapatkan jumlah penjantan besar
        jb = math.floor(self.n  * self.p)
        return jb
    
    def jantan_kecil(self):
        #fungsi untuk mendapatkan jumlah penjantan kecil
        jk = self.n - self.jantan_besar() - 1
        return jk
    
    def inisialisasi_populasi(self):
        #fungsi meninisiasi populasi
        
        for _ in range(self.n):
            individu_komodo = []
            while individu_komodo not in self.populasi_komodo:
                count = 0
                for key in self.space_search.keys():
                    if key in self.info_katogorikal_tipe:
                        individu_komodo.append(np.random.choice(self.space_search[key]))
                        self.kategorikal_index.append(count)
                    else:
                        individu_komodo.append(np.random.uniform(self.space_search[key][0],self.space_search[key][1]))
                    count += 1
                if individu_komodo in self.populasi_komodo :
                    individu_komodo = []
                else:
                    self.populasi_komodo.append(individu_komodo)
    
    def split_individu(self):
        #fungsi untuk membagi individu menjadi 3 bagian
        
        jumlah_jantan_besar = self.jantan_besar()
        
        urutan = []
        fitness_value = []
        count = 0
        
        while len(urutan) != len(self.populasi_komodo):
            cuurent = self.fitness_function(self.populasi_komodo[count])
            idx = count
            
            if count not in urutan:
                for i in len(self.populasi_komodo):
                    if self.fitness_function(self.populasi_komodo[i]) > cuurent and i not in urutan and count != i:
                        cuurent = self.fitness_function(self.populasi_komodo[i])
                        idx = i
                urutan.append(idx)
                fitness_value.append(cuurent)
            else:
                count += 1
                    
        
        self.jb = urutan[:jumlah_jantan_besar]
        self.betina = urutan[jumlah_jantan_besar]
        self.jk = urutan[jumlah_jantan_besar+1:]
        
        self.jb_fitness = fitness_value[:jumlah_jantan_besar]
        self.betina_fitness = fitness_value[jumlah_jantan_besar]
        self.jk_fitness = fitness_value[jumlah_jantan_besar+1:]
        
                   
    
    def movement_jantan_besar(self):
        # fungsi untuk pergerakan jantan besar
        new_posisi = []
        for i in range(len(self.jb)):
            individu1 = self.populasi_komodo[self.jb[i]]
            new_individu = []
            w = []
            for j in range(len(self.jb)):
                
                if i != j:
                    r1 = self.random_normal_0_1()
                    r2 = self.random_normal_0_1()
                    individu2 = self.populasi_komodo[self.jb[j]]
                    if self.jb_fitness[i]>= self.jb_fitness[j] and r2 < 0.5:
                        for l in range(len(individu1)):
                            if l not in self.kategorikal_index:
                                w.append(individu1[l] + r1*(individu2[l] - individu1[l]))
                            #else:
                                
                        
                        
    
    def interpolasi_kategorikal(self, individu1, individu2,r1):
        #fungsi interpolasi untuk dimensi kategorikal (eksploitasi)
        return round(r1 *individu2 + (1-r1)*individu1)
    
    #def probablilitas_katogrikal(self,fitnes_individu1, fitnes_individu2,beta):
        #fungsi probabilitas untuk dimensi kategorikal (eksplorasi)
        #penyebut = 
        
        
    
    def random_normal_0_1(self):
        # fungsi untuk mendapatkan nilai random dari distribusi normal
        
        while True:
            value = np.random.normal(0.5,0.1)
            if 0 <=value<=1:
                return value
