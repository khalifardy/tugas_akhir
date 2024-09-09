import math
import numpy as np


class KomodoMlipirAlgorithm:
    """
    Implementasi Algoritma Komodo Mlipir.

    Metode oleh:
        Prof. Dr. Suyanto, S.T., M.Sc. (2021)

    Implementasi Python oleh:
        Pejalan Sunyi (2024)

    Parameters:
        n (int): Jumlah populasi.
        p (float): Proporsi jantan besar.
        d (float): Tingkat mlipir.
        fitness_function (callable): Fungsi fitness yang akan dioptimalkan.
        search_space (dict): Batasan pencarian untuk setiap parameter.
        max_iter (int): Jumlah iterasi maksimum.
        random_state (int): Seed untuk keacakan.
        problem (str): Jenis masalah, "maximize" atau "minimize".
        alpha (float): Radius parthenogenesis.
        stop_criteria (float): Kriteria penghentian.
    """

    def __init__(
        self,
        n: int,
        p: float,
        d: float,
        fitness_function: callable,
        search_space: dict,
        max_iter: int = 100,
        random_state: int = 42,
        problem: str = "maximize",
        alpha: float = 0.1,
        stop_criteria: float = None,
    ):
        self.n = n
        self.p = p
        self.d = d
        self.fitness_function = fitness_function
        self.search_space = search_space
        self.max_iter = max_iter
        self.random_state = random_state
        self.problem = problem.lower()
        self.alpha = alpha
        self.stop_criteria = stop_criteria

        self.population = []
        self.male_large = []
        self.male_small = []
        self.female = None

        self.male_large_fitness = []
        self.male_small_fitness = []
        self.female_fitness = None

        self.history = {"best_fitness": [], "best_solution": []}
        self.best_fitness = None
        self.best_solution = None

        self.rng = np.random.default_rng(self.random_state)

    def initialize_population(self):
        """
        Inisialisasi populasi awal secara acak berdasarkan search_space.
        """
        for _ in range(self.n):
            individual = np.array([
                self.rng.uniform(low, high)
                for low, high in self.search_space.values()
            ])
            self.population.append(individual)
            

    def calculate_fitness(self):
        """
        Menghitung nilai fitness untuk setiap individu dalam populasi.
        """
        fitness_values = np.array([
            self.fitness_function(individual)
            for individual in self.population
        ])
        return fitness_values

    def sort_population(self, fitness_values):
        """
        Mengurutkan populasi berdasarkan nilai fitness.

        Args:
            fitness_values (np.array): Array nilai fitness.

        Returns:
            Tuple: Populasi dan fitness yang sudah diurutkan.
        """
        if self.problem == "maximize":
            sorted_indices = np.argsort(fitness_values)[::-1]
        elif self.problem == "minimize":
            sorted_indices = np.argsort(fitness_values)
        else:
            raise ValueError("Parameter 'problem' harus 'maximize' atau 'minimize'.")

        sorted_population = [self.population[i] for i in sorted_indices]
        sorted_fitness = fitness_values[sorted_indices]
        return sorted_population, sorted_fitness

    def split_population(self, sorted_population, sorted_fitness):
        """
        Membagi populasi menjadi jantan besar, betina, dan jantan kecil.

        Args:
            sorted_population (list): Populasi yang sudah diurutkan.
            sorted_fitness (np.array): Fitness yang sudah diurutkan.
        """
        num_male_large = math.floor(self.n * self.p)
        self.male_large = sorted_population[:num_male_large]
        self.male_large_fitness = sorted_fitness[:num_male_large]

        self.female = sorted_population[num_male_large]
        self.female_fitness = sorted_fitness[num_male_large]

        self.male_small = sorted_population[num_male_large + 1:]
        self.male_small_fitness = sorted_fitness[num_male_large + 1:]

    def male_large_movement(self):
        """
        Mengupdate posisi jantan besar berdasarkan interaksi antar jantan besar.

        Returns:
            list: Daftar individu jantan besar yang telah diperbarui.
        """
        updated_males = []
        for i, male in enumerate(self.male_large):
            movement = np.zeros_like(male)
            for j, other_male in enumerate(self.male_large):
                if i != j:
                    r1 = self.rng.normal(0.5, 0.1)
                    r2 = self.rng.normal(0.5, 0.1)
                    if self.problem == "maximize":
                        if (
                            self.male_large_fitness[j] > self.male_large_fitness[i]
                            and r2 < 0.5
                        ):
                            movement += r1 * (other_male - male)
                        else:
                            movement += r1 * (male - other_male)
                    else:
                        if (
                            self.male_large_fitness[j] < self.male_large_fitness[i]
                            and r2 < 0.5
                        ):
                            movement += r1 * (other_male - male)
                        else:
                            movement += r1 * (male - other_male)
                            
            updated_male = male + movement
            updated_male = self.clip_individual(updated_male)
            updated_males.append(updated_male)
        return updated_males

    def female_movement(self):
        """
        Mengupdate posisi betina melalui kawin atau parthenogenesis.

        Returns:
            np.array: Individu betina yang telah diperbarui.
        """
        r = self.rng.uniform()
        r1 = self.rng.normal(0.5, 0.1)
        if r < 0.5:
            # Kawin dengan jantan besar terbaik
            male = self.male_large[0]
            offspring1 = r1 * self.female + (1 - r1) * male
            offspring2 = r1 * male + (1 - r1) * self.female

            fitness1 = self.fitness_function(offspring1)
            fitness2 = self.fitness_function(offspring2)
            
            if self.problem == "maximize":
                offspring = offspring1 if fitness1 > fitness2 else offspring2
            else :
                offspring = offspring1 if fitness1 < fitness2 else offspring2
                
            print("Betina kawin dengan jantan besar.")
        else:
            # Parthenogenesis
            ub_lb = np.array([
                high - low
                for low, high in self.search_space.values()
            ])
            offspring = self.female + ub_lb * ((2 * r1 - 1) * self.alpha)
            offspring = self.clip_individual(offspring)
            print("Betina melakukan parthenogenesis.")
        return offspring

    def male_small_movement(self):
        """
        Mengupdate posisi jantan kecil berdasarkan interaksi dengan jantan besar.

        Returns:
            list: Daftar individu jantan kecil yang telah diperbarui.
        """
        updated_males = []
        for male in self.male_small:
            movement = np.zeros_like(male)
            for large_male in self.male_large:
                r1 = self.rng.normal(0.5, 0.1)
                r2 = self.rng.uniform()
                if r2 < self.d:
                    movement += r1 * (large_male - male)
            updated_male = male + movement
            updated_male = self.clip_individual(updated_male)
            updated_males.append(updated_male)
        return updated_males

    def clip_individual(self, individual):
        """
        Membatasi nilai individu agar tetap dalam batas search_space.

        Args:
            individual (np.array): Individu yang akan dibatasi.

        Returns:
            np.array: Individu yang telah dibatasi.
        """
        clipped = np.array([
            np.clip(value, low, high)
            for value, (low, high) in zip(individual, self.search_space.values())
        ])
        return clipped

    def optimize(self):
        """
        Menjalankan proses optimasi menggunakan Algoritma Komodo Mlipir.

        Returns:
            dict: Solusi terbaik dan nilai fitness terbaik.
        """
        self.initialize_population()
        for iteration in range(self.max_iter):
            if iteration == 0:
                fitness_values = self.calculate_fitness()
                sorted_pop, sorted_fit = self.sort_population(fitness_values)
            self.split_population(sorted_pop, sorted_fit)

            # Pergerakan masing-masing kelompok
            new_male_large = self.male_large_movement()
            new_female = self.female_movement()
            new_male_small = self.male_small_movement()

            # Membentuk populasi baru
            self.population += new_male_large + [new_female] + new_male_small
            new_populasi,fitness_values = self.sort_population(self.calculate_fitness())
            self.population = new_populasi[:self.n]
            sorted_pop = self.population
            sorted_fit = fitness_values[:self.n]

            # Evaluasi populasi baru
            self.best_fitness = fitness_values[0]
            self.best_solution = self.population[0]

            # Menyimpan sejarah
            self.history["best_fitness"].append(self.best_fitness)
            self.history["best_solution"].append(self.best_solution)

            print(
                f"Generasi {iteration + 1}: Best Fitness = {self.best_fitness}, "
                f"Best Solution = {self.best_solution}"
            )

            # Pengecekan kriteria penghentian
            if self.stop_criteria is not None:
                if abs(self.best_fitness - self.stop_criteria) <= 0.1:
                    print("Kriteria penghentian tercapai.")
                    break

        return {
            "best_solution": self.best_solution,
            "best_fitness": self.best_fitness,
            "history": self.history,
        }
