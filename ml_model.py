# ml_model.py
# Simple rule-based plastic-to-fuel yield estimator

def estimate_yield(plastic_type: str, mass_kg: float, method: str = "pyrolysis"):
    """
    Estimate fuel yield and emission comparison for given plastic input.
    """

    plastic_type = (plastic_type or '').upper()

    # Approximate fuel yields (liters per kg) for common plastics
    yield_ratios = {
        "PET": 0.6,
        "HDPE": 0.8,
        "LDPE": 0.75,
        "PP": 0.7,
        "PS": 0.65,
        "PVC": 0.4
    }

    # Base emission factors (kg CO2 per liter of fuel)
    fuel_emission_factor = 2.31  # kg CO₂/liter (diesel equivalent)
    plastic_emission_factor = 3.14  # if burned directly

    yield_ratio = yield_ratios.get(plastic_type, 0.6)
    estimated_fuel = mass_kg * yield_ratio

    # Emissions comparison
    emissions_plastic_burn = mass_kg * plastic_emission_factor
    emissions_from_fuel = estimated_fuel * fuel_emission_factor
    net_reduction = emissions_plastic_burn - emissions_from_fuel

    # Energy efficiency approximation (simple heuristic)
    efficiency = round((yield_ratio / 0.8) * 90, 2)

    return {
        "plastic_type": plastic_type,
        "method": method,
        "input_mass_kg": mass_kg,
        "estimated_fuel_liters": round(estimated_fuel, 2),
        "emissions_from_fuel": round(emissions_from_fuel, 2),
        "emissions_plastic_burn": round(emissions_plastic_burn, 2),
        "net_emission_reduction": round(net_reduction, 2),
        "energy_efficiency_percent": efficiency
    }
