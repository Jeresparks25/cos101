print("Physics Formula Calculator - Set 4")
print("Choose a formula:")
print("a → Q = mcΔT               (Heat Energy)")
print("b → Q = mL                  (Latent Heat)")
print("c → Efficiency = (U/I)×100  (Efficiency)")
print("d → GPE = mgh               (Potential Energy)")
print("e → v = f * λ               (Wave Speed)")

choice = input("Enter a, b, c, d, or e: ").lower()

# a → Q = mcΔT
if choice == "a":
    print("\nFormula selected: Q = mcΔT")
    m = float(input("Enter mass (m): "))
    c = float(input("Enter specific heat capacity (c): "))
    dT = float(input("Enter temperature change (ΔT): "))
    Q = m * c * dT
    print("Heat Energy =", Q, "J")

# b → Q = mL
elif choice == "b":
    print("\nFormula selected: Q = mL")
    m = float(input("Enter mass (m): "))
    L = float(input("Enter latent heat (L): "))
    Q = m * L
    print("Heat Energy =", Q, "J")

# c → Efficiency = (Useful / Input) × 100
elif choice == "c":
    print("\nFormula selected: Efficiency = (Useful/Input) × 100")
    useful = float(input("Enter useful energy output: "))
    input_energy = float(input("Enter input energy: "))
    eff = (useful / input_energy) * 100
    print("Efficiency =", eff, "%")

# d → GPE = mgh
elif choice == "d":
    print("\nFormula selected: GPE = mgh")
    m = float(input("Enter mass (m): "))
    g = float(input("Enter gravity (g): "))
    h = float(input("Enter height (h): "))
    GPE = m * g * h
    print("Gravitational Potential Energy =", GPE, "J")

# e → v = f * λ
elif choice == "e":
    print("\nFormula selected: v = f * λ")
    f = float(input("Enter frequency (f): "))
    lamb = float(input("Enter wavelength (λ): "))
    v = f * lamb
    print("Wave Speed =", v, "m/s")

else:
    print("Invalid option. Please run the program again.")