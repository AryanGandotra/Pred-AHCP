import csv


def Transition():

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

    for property_name, property_groups in properties.items():
        print("Property:", property_name, property_groups)

    seq = "VSFAIKWEYVLLL"
    result = []
    result.append(seq)

    for property_name, property_groups in properties.items():

        prev_group = None
        curr_group = None

        freq_1221 = 0
        freq_1331 = 0
        freq_2332 = 0
        print("_______________________________________________________________")
        print()
        print("Sequence:", seq)
        print("Property:", property_name)
        print()

        for letter in seq:
            for i, group in enumerate(property_groups):
                if letter in group:
                    curr_group = i + 1
                    break

            if curr_group == 1 and prev_group == 2 or curr_group == 2 and prev_group == 1:
                freq_1221 += 1
            elif curr_group == 1 and prev_group == 3 or curr_group == 3 and prev_group == 1:
                freq_1331 += 1
            elif curr_group == 2 and prev_group == 3 or curr_group == 3 and prev_group == 2:
                freq_2332 += 1

            prev_group = curr_group

        print("Frequency 1221:", freq_1221/(len(seq)-1))
        print("Frequency 1331:", freq_1331/(len(seq)-1))
        print("Frequency 2332:", freq_2332/(len(seq)-1))

        result.append(freq_1331/(len(seq)-1))
        result.append(freq_1221/(len(seq)-1))
        result.append(freq_2332/(len(seq)-1))

    with open("TRANSITION.csv", "w", newline="") as csvfile:
        name = ["1331", "1221", "2332"]
        writer = csv.writer(csvfile)
        header_row = ["Seq"]
        for property_name, property_values in properties.items():
            for group_num, group in enumerate(property_values, start=1):
                header_row.append(f"{property_name}.{name[group_num-1]}")
        writer.writerow(header_row)
        writer.writerow(result)
    print("CSV file 'output.csv' has been generated.")


seq = 'VSFAIKWEYVLLL'
Transition()
