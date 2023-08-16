# Data sources
database(
    thermoLibraries = ['primaryThermoLibrary'], #add the thermo librarys that are important for your system
    reactionLibraries = [], #load a pre-compiled list of parameterized reactions
    seedMechanisms = [], #you can 'seed' the core with a mechanism
    kineticsDepositories = ['training'], #load the default training data for the reaction
    kineticsFamilies = 'default', #load all the families you think you'll need (default loads everything)
    kineticsEstimator = 'rate rules', #use rate rules to estimate the kinetics
)

# List of species
species(
    label='H2',
    reactive=True,
    structure=SMILES("[H][H]"),
)

species(
    label='O2',
    reactive=True,
    structure=adjacencyList(
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
"""),
)

# Reaction systems
simpleReactor(
    temperature=(1350,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "H2": 2.0,
        "O2":1,
    },
    terminationConversion={
        'H2': 0.9,
    },
    terminationTime=(1e6,'s'),
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0.0, #if the production rate is below this threshold, the species is removed from the edge
    toleranceMoveToCore=0.1, #if the production rate exceeds this threshold, the species is moved to the core
    toleranceInterruptSimulation=0.1, #if the production rate of a species exceeds this threshold, the generation interrupted
    maximumEdgeSpecies=100000,
    filterReactions=True, #filter out reactions that are too slow
)

options(
    units='si',
    generateOutputHTML=True,
    generatePlots=False,
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
)
