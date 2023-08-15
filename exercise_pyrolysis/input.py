# Data sources
database(
    thermoLibraries = ['primaryThermoLibrary', 'BurkeH2O2', 'FFCM1(-)', 'NOx2018', 'Klippenstein_Glarborg2016', 'thermo_DFT_CCSDTF12_BAC', 'JetSurF2.0', 'CBS_QB3_1dHR', 'CurranPentane'],
    reactionLibraries = ['primaryH2O2', 'FFCM1(-)', 'CurranPentane', 'NOx2018'],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['ch_pyrolysis'],
    kineticsEstimator = 'rate rules',
    transportLibraries=['PrimaryTransportLibrary', 'OneDMinN2', 'NOx2018', 'GRI-Mech', 'NIST_Fluorine']
)

# List of species
species(
    label='C3H8',
    structure=SMILES("CCC"),
)
species(
    label='N2',
    reactive=False,
    structure=SMILES("N#N"),
)

# Reaction systems
simpleReactor(
    temperature=(700 + 273, 'K'),
    pressure=(1, 'atm'),
    initialMoleFractions={
         'C3H8': 1,  'N2': 0,
    },
    terminationRateRatio=0.05,
    terminationTime=(5 ,'s'),
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.05,
    toleranceInterruptSimulation=0.05,
    maximumEdgeSpecies=100000,
)

options(
    units='si',
    generateOutputHTML=False,
    generatePlots=True,
    saveEdgeSpecies=False,
    saveSimulationProfiles=True,
)

pressureDependence(
        method='modified strong collision',
        maximumGrainSize=(0.5, 'kcal/mol'),
        minimumNumberOfGrains=250,
        temperatures=(500, 2000, 'K', 8),
        pressures=(0.1, 100, 'bar', 5),
        interpolation=('Chebyshev', 6, 4),
        maximumAtoms=16,
)

generatedSpeciesConstraints(
    allowed=['input species','seed mechanisms','reaction libraries'],
    maximumCarbonAtoms=3,
    maximumOxygenAtoms=0,
    maximumNitrogenAtoms=0,
    maximumSiliconAtoms=0,
    maximumSulfurAtoms=0,
    maximumHeavyAtoms=3,
    maximumRadicalElectrons=1,
    maximumSingletCarbenes=0,
    maximumCarbeneRadicals=0,
)

