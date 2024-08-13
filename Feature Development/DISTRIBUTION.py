import math
import csv


def Distribution(seq):

    Charge = []
    Charge.append(["K", "R"])
    Charge.append(
        ["A", "N", "C", "Q", "G", "H", "I", "L", "M", "F", "P", "S", "T", "W", "Y", "V"]
    )
    Charge.append(["D", "E"])

    Hydrophobicity_CASG920101 = []
    Hydrophobicity_CASG920101.append(["K", "D", "E", "Q", "P", "S", "R", "N", "T", "G"])
    Hydrophobicity_CASG920101.append(["A", "H", "Y", "M", "L", "V"])
    Hydrophobicity_CASG920101.append(["F", "I", "W", "C"])

    Hydrophobicity_FASG890101 = []
    Hydrophobicity_FASG890101.append(["K", "E", "R", "S", "Q", "D"])
    Hydrophobicity_FASG890101.append(["N", "T", "P", "G"])
    Hydrophobicity_FASG890101.append(["A", "Y", "H", "W", "V", "M", "F", "L", "I", "C"])

    NormalizedvanderWaalsvolume = []
    NormalizedvanderWaalsvolume.append(["G", "A", "S", "T", "P", "D"])
    NormalizedvanderWaalsvolume.append(["N", "V", "E", "Q", "I", "L"])
    NormalizedvanderWaalsvolume.append(["M", "H", "K", "F", "R", "Y", "W"])

    Polarity = []
    Polarity.append(["R", "K", "E", "D", "Q", "N"])
    Polarity.append(["G", "A", "S", "T", "P", "H", "Y"])
    Polarity.append(["C", "L", "V", "I", "M", "F", "W"])

    Polarizability = []
    Polarizability.append(["G", "A", "S", "D", "T"])
    Polarizability.append(["C", "P", "N", "V", "E", "Q", "I", "L"])
    Polarizability.append(["K", "M", "H", "F", "R", "Y", "W"])

    Secondarystructure = []
    Secondarystructure.append(["E", "A", "L", "M", "Q", "K", "R", "H"])
    Secondarystructure.append(["V", "I", "Y", "C", "W", "F", "T"])
    Secondarystructure.append(["G", "N", "P", "S", "D"])

    Solventaccessibility = []
    Solventaccessibility.append(["A", "L", "F", "C", "G", "I", "V", "W"])
    Solventaccessibility.append(["P", "K", "Q", "E", "N", "D"])
    Solventaccessibility.append(["M", "P", "S", "T", "H", "Y"])

    properties = {
        "prop_1": Charge,
        "prop_2": Hydrophobicity_CASG920101,
        "prop_3": Hydrophobicity_FASG890101,
        "prop_4": NormalizedvanderWaalsvolume,
        "prop_5": Polarity,
        "prop_6": Polarizability,
        "prop_7": Secondarystructure,
        "prop_8": Solventaccessibility,
    }
    with open("DISTRIBUTION.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        header_row = ["Sequence"]
        for property_name, property_values in properties.items():
            for group_num, group in enumerate(property_values, start=1):
                for res in range(0, 101, 25):
                    header_row.append(f"{property_name}.G{group_num}.res{res}")
        writer.writerow(header_row)

        # Prepare data row
        data_row = [seq]

        for property_name, property_values in properties.items():
            group_mapping = {}
            for i, letter in enumerate(seq):
                for group_number, group in enumerate(property_values):
                    if letter in group:
                        group_mapping[i + 1] = group_number + 1
                        break

            subarrays = [[] for _ in range(max(group_mapping.values()))]
            for index, group_number in group_mapping.items():
                subarrays[group_number - 1].append(index)

            total_length = len(subarrays[0] + subarrays[1] + subarrays[2])

            for group_num, subarray in enumerate(subarrays):
                if subarray:
                    res_0 = subarray[0] / total_length * 100
                    res_25 = (
                        subarray[math.floor((len(subarray) - 1) * 1 / 4)]
                        / total_length
                        * 100
                    )
                    res_50 = (
                        subarray[math.floor((len(subarray) - 1) * 2 / 4)]
                        / total_length
                        * 100
                    )
                    res_75 = (
                        subarray[math.floor((len(subarray) - 1) * 3 / 4)]
                        / total_length
                        * 100
                    )
                    res_100 = subarray[len(subarray) - 1] / total_length * 100

                    # Add data to the data row
                    data_row.extend([res_0, res_25, res_50, res_75, res_100])
                    print(res_0, res_25, res_50, res_75, res_100)
                else:
                    # Add placeholders for empty subarrays
                    data_row.extend([None] * 5)

        # Write the data row
        writer.writerow(data_row)

    print("Data saved to 'data.csv' successfully.")


seq = "VSFAIKKEYVLLL"
Distribution(seq)
