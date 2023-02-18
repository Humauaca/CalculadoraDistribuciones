from scipy import stats

class Distribuciones:
    def __init__(self):
        self.distribuciones = {
            "binomial": stats.binom,
            "normal": stats.norm,
            "geometrica": stats.geom,
            "poisson": stats.poisson
        }

    def calcular_igual(self, distribucion, x, *args):
        funcion = self.distribuciones[distribucion]
        if distribucion == "normal":
            mu, sigma = args
            return funcion.pdf(x, mu, sigma)
        elif distribucion == "binomial":
            n, p = args
            return funcion.pmf(x, n, p)
        elif distribucion == "geometrica":
            p = args[0]
            return funcion.pmf(x, p)
        elif distribucion == "poisson":
            lam = args[0]
            return funcion.pmf(x, lam)

    def calcular_menor(self, distribucion, x, *args):
        function = self.distribuciones[distribucion]
        if distribucion == "normal":
            mu, sigma = args
            return function.cdf(x, mu, sigma) - function.pdf(x, mu, sigma)
        elif distribucion == "binomial":
            n, p = args
            return function.cdf(x, n, p) - function.pmf(x, n, p)
        elif distribucion == "geometrica":
            p = args[0]
            return function.cdf(x, p) - function.pmf(x, p)
        elif distribucion == "poisson":
            lam = args[0]
            return function.cdf(x, lam) - function.pmf(x, lam)
    
    def calcular_menor_igual(self, distribucion, x, *args):
        funcion = self.distribuciones[distribucion]
        if distribucion == "normal":
            mu, sigma = args
            return funcion.cdf(x, mu, sigma)
        elif distribucion == "binomial":
            n, p = args
            return funcion.cdf(x, n, p) 
        elif distribucion == "geometrica":
            p = args[0]
            return funcion.cdf(x, p)
        elif distribucion == "poisson":
            lam = args[0]
            return funcion.cdf(x, lam)

    def calcular_entre(self, distribucion, x1, x2, *args):
        funcion = self.distribuciones[distribucion]
        if distribucion == "normal":
            mu, sigma = args
            return funcion.cdf(x2, mu, sigma) - funcion.cdf(x1, mu, sigma)
        elif distribucion == "binomial":
            n, p = args
            return funcion.cdf(x2 , n, p) - funcion.cdf(x1 , n, p)
        elif distribucion == "geometrica":
            p = args[0]
            return funcion.cdf(x2, p) - funcion.cdf(x1, p)
        elif distribucion == "poisson":
            lam = args[0]
            return funcion.cdf(x2, lam) - funcion.cdf(x1, lam)
    
    def calcular_mayor(self, distribucion, x, *args):
        funcion = self.distribuciones[distribucion]
        if distribucion == "normal":
            mu, sigma = args
            return funcion.sf(x, mu, sigma)
        elif distribucion == "binomial":
            n, p = args
            return funcion.sf(x, n, p)
        elif distribucion == "geometrica":
            p = args[0]
            return funcion.sf(x, p)
        elif distribucion == "poisson":
            lam = args[0]
            return funcion.sf(x, lam)
    
    def calcular_mayor_igual(self,distribucion, x, *args):
        funcion = self.distribuciones[distribucion]
        if distribucion == "normal":
            mu, sigma = args
            return funcion.sf(x, mu, sigma) + funcion.pdf(x, mu, sigma)
        elif distribucion == "binomial":
            n, p = args
            return funcion.sf(x, n, p) + funcion.pmf(x, n, p)
        elif distribucion == "geometrica":
            p = args[0]
            return funcion.sf(x, p) + funcion.pmf(x, p)
        elif distribucion == "poisson":
            lam = args[0]
            return funcion.sf(x, lam) + funcion.pmf(x, lam)

    
