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
    random_state : state untuk keacakan
    problem : masalah yang akan diselesaikan, "maximize" atau "minimize"
    alpha : radius parthenogenesis
    
    """
    
    def __init__(self, n:int, p:float, d:float, fitness_function:callable , space_search:dict, max_iter:int, info_katogorikal_tipe:list, problem:str="maximize",random_state:int=22, alpha:float = 0.1 ):
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
        self.random_state = random_state
        self.problem = problem
        self.alpha = alpha
        
    
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
                individu_komodo = np.random.default_rng(self.random_state).random(len(self.space_search.keys()))
        
                if individu_komodo in self.populasi_komodo :
                    individu_komodo = []
                else:
                    self.populasi_komodo.append(individu_komodo)
    
    def split_individu(self):
        #fungsi untuk membagi individu menjadi 3 bagian
        
        jumlah_jantan_besar = self.jantan_besar()
        
        if self.problem == "maximize":
            urutan, fitness_value = self.maximize_problem()
        else:
            urutan, fitness_value = self.minimize_problem()
                    
        
        self.jb = urutan[:jumlah_jantan_besar]
        self.betina = urutan[jumlah_jantan_besar]
        self.jk = urutan[jumlah_jantan_besar+1:]
        
        self.jb_fitness = fitness_value[:jumlah_jantan_besar]
        self.betina_fitness = fitness_value[jumlah_jantan_besar]
        self.jk_fitness = fitness_value[jumlah_jantan_besar+1:]
    
    def movement_jantan_besar(self):
        #fungsi untuk movement jantan besar
        individu_baru = []
        for i in range(len(self.jb)):
            individu1 = self.jb[i]
            w = [] 
            for j in range(len(self.populasi_komodo[self.jb[i]])):
                if i != j:
                    r1 = self.random_normal_0_1()
                    r2 = self.random_normal_0_1()
                    individu2 = self.jb[j]
                
                    if self.jb_fitness[j] > self.jb_fitness[i] or r2 < 0.5:
                        w.append(r1*(individu2-individu1))
                    else:
                        w.append(r1*(individu1-individu2))
                    individu_baru.append(individu1 + sum(w))
        
        return individu_baru
        
             
                        
        
    def movement_betina(self):
        #fungsi untuk update betina
        
        prob = self.random_normal_0_1()
        r1 = self.random_normal_0_1()
        
        if prob < 0.5 : 
            anak1 = r1 * self.betina  + (1 - r1) * self.jb[0]
            anak2 = r1 * self.jb[0] + (1-r1) * self.betina
            
            fitnes1 = self.fitness_function(anak1)
            fitnes2 = self.fitness_function(anak2)
            
            if fitnes1 > fitnes2:
                return anak1
            else:
                return anak2
            
        else:
            return self.betina + (2*r1 - 1) * self.alpha
        
        
        
        
                                
                        
                        
    def maximize_problem(self):
        #mengurutkan dari terbesar ke terkecil
        
        urutan = []
        fitness_value = []
        count = 0
        
        while len(urutan) != len(self.populasi_komodo):
            cuurent = self.fitness_function(self.populasi_komodo[count])
            idx = count
            
            if count not in urutan:
                for i in range(len(self.populasi_komodo)):
                    if self.fitness_function(self.populasi_komodo[i]) >= cuurent and i not in urutan and count != i:
                        cuurent = self.fitness_function(self.populasi_komodo[i])
                        idx = i
                urutan.append(idx)
                fitness_value.append(cuurent)
            else:
                count += 1
        
        return urutan, fitness_value
    
    def minimize_problem(self):
        #mengurutkan dari terkecil ke terbesar
        
        urutan = []
        fitness_value = []
        count = 0
        
        while len(urutan) != len(self.populasi_komodo):
            cuurent = self.fitness_function(self.populasi_komodo[count])
            idx = count
            
            if count not in urutan:
                for i in range(len(self.populasi_komodo)):
                    if self.fitness_function(self.populasi_komodo[i]) <= cuurent and i not in urutan and count != i:
                        cuurent = self.fitness_function(self.populasi_komodo[i])
                        idx = i
                urutan.append(idx)
                fitness_value.append(cuurent)
            else:
                count += 1
        
        return urutan, fitness_value
    
    def random_normal_0_1(self):
        # fungsi untuk mendapatkan nilai random dari distribusi normal
        
        while True:
            value = np.random.default_rng(self.random_state).normal(0.5,0.1)
            if 0 <=value<=1:
                return value
