import csv


def Composition():

    seq = 'VSFAIKWEYVLLL'
    Charge = []
    Charge.append(['K', 'R'])
    Charge.append(['A', 'N', 'C', 'Q', 'G', 'H', 'I', 'L',
                   'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'])
    Charge.append(['D', 'E'])

    Hydrophobicity_CASG920101 = []
    Hydrophobicity_CASG920101.append(
        ['K', 'D', 'E', 'Q', 'P', 'S', 'R', 'N', 'T', 'G'])
    Hydrophobicity_CASG920101.append(['A', 'H', 'Y', 'M', 'L', 'V'])
    Hydrophobicity_CASG920101.append(['F', 'I', 'W', 'C'])

    Hydrophobicity_FASG890101 = []
    Hydrophobicity_FASG890101.append(
        ['K', 'E', 'R', 'S', 'Q', 'D'])
    Hydrophobicity_FASG890101.append(['N', 'T', 'P', 'G'])
    Hydrophobicity_FASG890101.append(
        ['A', 'Y', 'H', 'W', 'V', 'M', 'F', 'L', 'I', 'C'])

    NormalizedvanderWaalsvolume = []
    NormalizedvanderWaalsvolume.append(
        ['G', 'A', 'S', 'T', 'P', 'D'])
    NormalizedvanderWaalsvolume.append(['N', 'V', 'E', 'Q', 'I', 'L'])
    NormalizedvanderWaalsvolume.append(
        ['M', 'H', 'K', 'F', 'R', 'Y', 'W'])

    Polarity = []
    Polarity.append(
        ['R', 'K', 'E', 'D', 'Q', 'N'])
    Polarity.append(['G', 'A', 'S', 'T', 'P', 'H', 'Y'])
    Polarity.append(
        ['C', 'L', 'V', 'I', 'M', 'F', 'W'])

    Polarizability = []
    Polarizability.append(
        ['G', 'A', 'S', 'D', 'T'])
    Polarizability.append(['C', 'P', 'N', 'V', 'E', 'Q', 'I', 'L'])
    Polarizability.append(
        ['K', 'M', 'H', 'F', 'R', 'Y', 'W'])

    Secondarystructure = []
    Secondarystructure.append(
        ['E', 'A', 'L', 'M', 'Q', 'K', 'R', 'H'])
    Secondarystructure.append(['V', 'I', 'Y', 'C', 'W', 'F', 'T'])
    Secondarystructure.append(
        ['G', 'N', 'P', 'S', 'D'])

    Solventaccessibility = []
    Solventaccessibility.append(
        ['A', 'L', 'F', 'C', 'G', 'I', 'V', 'W'])
    Solventaccessibility.append(['P', 'K', 'Q', 'E', 'N', 'D'])
    Solventaccessibility.append(
        ['M', 'P', 'S', 'T', 'H', 'Y'])

    properties = {
        "prop_1": Charge,
        "prop_2": Hydrophobicity_CASG920101,
        "prop_3": Hydrophobicity_FASG890101,
        "prop_4": NormalizedvanderWaalsvolume,
        "prop_5": Polarity,
        "prop_6": Polarizability,
        "prop_7": Secondarystructure,
        "prop_8": Solventaccessibility
    }

    # row_data = [seq]

    for property_name, property_values in properties.items():
        # print("Property", property_name)
        seq = 'VSFAIKWEYVLLL'
        # print("Sequence: ", seq)
        grp1_freq = 0
        grp2_freq = 0
        grp3_freq = 0
        for char in seq:
            if char in property_values[0]:
                grp1_freq += 1
            elif char in property_values[1]:
                grp2_freq += 1
            elif char in property_values[2]:
                grp3_freq += 1
    filename = "COMPOSITION.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        header_row = ["Seq"]
        for property_name, property_values in properties.items():
            for group_num, group in enumerate(property_values, start=1):
                header_row.append(f"{property_name}.G{group_num}")
        writer.writerow(header_row)

        data_row = [seq]
        for property_name, property_values in properties.items():
            for group in property_values:
                group_freq = sum(char in group for char in seq) / len(seq)
                data_row.append(group_freq)
        writer.writerow(data_row)

    print(f"CSV file '{filename}' created successfully!")


seq = 'VSFAIKWEYVLLL'
Composition()
