# domací ukol 1
# Tvým úkolem je vytvořit program pro zjednodušený výpočet daně z nemovitostí. Aplikace bude postavená na principech OOP. Viz https://moje.czechitas.cz/cs/udalosti/prehled/2625-programovani-v-pythonu/domaci-ukol/941

from math import ceil
from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum

# V rámci aplikace nejprve vytvoř třídu Locality, která označuje lokalitu, kde se nemovitost nachází. Třída bude mít atributy name (název katastru/obce) a locality_coefficient (tzv. místní koeficient, který se používá k výpočtu daně).

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

Manetin = Locality("Manětín", 0.8)
Brno = Locality("Brno", 3)

# Vytvoř třídu Property, která bude reprezentovat nějakou nemovitost. Třída bude mít atribut locality (lokalita, kde se pozemek nachází, bude to objekt třídy Locality).
# Bonus: Uprav třídu Property na abstraktní třídu. 


class Property(ABC):
    @abstractmethod
    def __init__ (self, locality):
        self.locality = locality

#Bonus: Podívej se na to, jak fungují tzv. enum třídy. Můžeš si přečíst například tento text. Zkus vytvořit třídu pro typy pozemků (zemědělský pozemek, stavební pozemek, les, zahrada) a použít ji ve třídě Estate.

class estate_type(Enum):
    land = 1
    building_site = 2
    forrest = 3
    garden = 4


# Dále vytvoř třídu Estate, která reprezentuje pozemek a je potomkem třídy Property. Třída bude mít atributy locality, estate_type (typ pozemku), area (plocha pozemku v metrech čtverečních). Dále přidej metodu calculate_tax(), která spočítá výši daně pro pozemek a vrátí hodnotu jak celé číslo (pro zaokrouhlení použij funkci ceil() z modulu math). Daň vypočítej pomocí vzorce: plocha pozemku * koeficient dle typu pozemku (atribut estate_type) * místní koeficient. U atributu estate_type následující hodnoty a koeficienty:

@dataclass
class Estate(Property):
    locality: str
    estate_type: Enum
    area: str

    def calculate_tax(self):
        if self.locality == "Manětín":
            coefficient = getattr(Manetin, "locality_coefficient")
        if self.locality == "Brno":
            coefficient = getattr(Brno, "locality_coefficient")  
 

        if self.estate_type == 1:
            self.tax = ceil(self.area * 0.85 * coefficient)
            return f"Daň u této nemovitosti je {self.tax}."
        elif self.estate_type == 2:
            self.tax = ceil(self.area * 9 * coefficient)
            return f"Daň u této nemovitosti je {self.tax}."
        elif self.estate_type == 3:
            self.tax = ceil(self.area * 0.35 * coefficient)
            return f"Daň u této nemovitosti je {self.tax}."
        elif self.estate_type == 4:
            self.tax = ceil(self.area * 2 * coefficient)
            return f"Daň u této nemovitosti je {self.tax}."
        else:
            return "Není validní typ pozemku."
        
# Bonus: Ke třídě Estate a Residence přidej výpisy informací do metody __str__(). 
        
    def __str__(self):
        if self.locality == "Manětín":
            coefficient = getattr(Manetin, "locality_coefficient")
        if self.locality == "Brno":
            coefficient = getattr(Brno, "locality_coefficient")

        if self.estate_type == 1:
            return f"Jedná se o zamědělský pozemek, lokalita {self.locality} (koeficient {coefficient}), {self.area} metrů čtverečních, dań {self.tax} Kč."
        if self.estate_type == 2:
            return f"Jedná se o stavební pozemek, lokalita {self.locality} (koeficient {coefficient}), {self.area} metrů čtverečních, dań {self.tax} Kč."
        if self.estate_type == 3:
            return f"Jedná se o les, lokalita {self.locality} (koeficient {coefficient}), {self.area} metrů čtverečních, dań {self.tax} Kč."
        if self.estate_type == 4:
            return f"Jedná se o zahradu, lokalita {self.locality} (koeficient {coefficient}), {self.area} metrů čtverečních, dań {self.tax} Kč."

pozemek = Estate("Manětín", 1, 900)
pozemek_2 = Estate("Manětín", "lands", 900)

# Vytvoř třídu Residence`, která reprezentuje byt, dům či jinou stavbu a je potomkem třídy Property. Třída bude mít atributy locality, area (podlahová plocha bytu nebo domu) a commercial (pravdivostní hodnota, která určuje, zda se jedná o nemovitost používanou k podnikání). Dále přidej metodu calculate_tax(), která spočítá výši daně pro byt a vrátí hodnotu jako číslo. Daň vypočítej pomocí vzorce: podlahová plocha * koeficient lokality * 15. Pokud je hodnota parametru commercial True, tj. pokud jde o komerční nemovitost, vynásob celou daň číslem 2.
class Residence(Property):
    def __init__(self, locality, area, commercial):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        if self.locality == "Manětín":
            coefficient = getattr(Manetin, "locality_coefficient")
        if self.locality == "Brno":
            coefficient = getattr(Brno, "locality_coefficient")

        if self.commercial == False:
            self.tax = ceil(self.area * coefficient * 15)
            return f"Daň u této nemovitosti je {self.tax}."
        else:
            self.tax = ceil(self.area * coefficient * 15 * 2)
            return f"Daň u této nemovitosti je {self.tax}."

 # Bonus: Ke třídě Estate a Residence přidej výpisy informací do metody __str__(). 
         
    def __str__(self):
        if self.locality == "Manětín":
            coefficient = getattr(Manetin, "locality_coefficient")
        if self.locality == "Brno":
            coefficient = getattr(Brno, "locality_coefficient")

        if self.commercial == True:
            return f"Jedná se o nebytový prostor, lokalita {self.locality} (koeficient {coefficient}), {self.area} metrů čtverečních, dań {self.tax} Kč."  
        if self.commercial == False:
            return f"Jedná se o bytový prostor, lokalita {self.locality} (koeficient {coefficient}), {self.area} metrů čtverečních, dań {self.tax} Kč."  

dum = Residence("Manětín", 120, False)
kancelar = Residence("Brno", 90, True)


# Přidej třídu TaxReport, která bude reprezentovat daňové přiznání. Třída bude mít atributy name (jméno osoby, která přiznání podává) a property_list, což je seznam nemovitostí, které jsou v přiznání uvedeny. Dále přidej metodu add_property(), která bude mít jako parametr objekt (nemovitost, která je součástí přiznání) a vloží ji do seznamu property_list. Dále přidej metodu calculate_tax(), která vypočte daň ze všech nemovitostí v seznamu property_list.


@dataclass
class TaxReport:
    name: str
    property_list: list

    def add_property(self):
        return self.property_list.append(Františkovy_majetky)
    
    
    def calculate_tax(self):
        total_tax = sum(p.tax for p in self.property_list)
        return f"Celková daň pro {self.name} je {total_tax} Kč."

Františkovy_majetky = [pozemek, dum, kancelar]
Frantiskovo_priznani = TaxReport ("František Novák", Františkovy_majetky)



print (pozemek.calculate_tax())
print (pozemek_2.calculate_tax())
print (pozemek.__str__())
print (dum.calculate_tax())
print (dum.__str__())
print (kancelar.calculate_tax())
print (kancelar.__str__())
print (Frantiskovo_priznani.calculate_tax())