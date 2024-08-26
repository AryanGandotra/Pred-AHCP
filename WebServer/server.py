from flask import Flask, render_template, request, send_file
import csv
from itertools import product
import math
import pickle
import pandas as pd
import time
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

model = pickle.load(open("Web Server/RandomForest.pkl", "rb"))

column_names = model.feature_names_in_


def AAC(given_string, data_row, header_row):
    allowed_string = "AMVFIHYLWCDKSTGQEPRN"
    Dict = {char: 0 for char in allowed_string}

    for i in given_string:
        if i not in allowed_string:
            raise ValueError("The string you entered is invalid.")
        else:
            Dict[i] += 1

    for i in Dict:
        Dict[i] = Dict[i] / len(given_string)
    header_row.extend(["Sequence"] + [char for char in sorted(allowed_string)])
    data_row.extend([given_string] + [Dict[key]
                    for key in sorted(Dict.keys())])


def EAAC(given_string, data_row, header_row):
    allowed_string = "AMVFIHYLWCDKSTGQEPRN"

    if len(given_string) > 36:
        raise ValueError("The string you entered is invalid.")
        return
    elif len(given_string) < 36:
        for char in given_string:
            if char not in allowed_string:
                raise ValueError("The string you entered is invalid.")
                return
        given_string = given_string.ljust(36, " ")
        allowed_string = allowed_string.replace("_", "")
    else:
        for char in given_string:
            if char not in allowed_string:
                raise ValueError("The string you entered is invalid.")
                return

    i = 0
    j = i + 5
    while j <= len(given_string):
        window_name = f"SW.{i + 1}"
        freq_dict = {char: 0 for char in allowed_string}
        for k in given_string[i:j]:
            if k != " ":
                freq_dict[k] += 1

        freq_list = [freq_dict[char] / 5 for char in sorted(allowed_string)]
        data_row.extend(freq_list)

        header_row.extend(
            [f"{window_name}.{char}" for char in sorted(allowed_string)])

        i += 1
        j += 1


def CKSAAP(seq, data_row, header_row):
    allowed_chars = "ACDEFGHIKLMNPQRSTVWY"
    for i in seq:
        if i not in allowed_chars:
            raise ValueError("The string you entered is invalid.")
            exit()

    total_data = []
    object_data = []

    for k in range(4):
        pairs = ["".join(pair) for pair in product(allowed_chars, repeat=2)]
        pairs = {pair: 0 for pair in pairs}
        for i in range(len(seq)):
            for j in range(i + k + 1, len(seq)):
                if j - i == k + 1:
                    pair = seq[i] + seq[j]
                    if set(pair).issubset(set(allowed_chars)):
                        if pair in pairs:
                            pairs[pair] += 1
                        else:
                            pairs[pair] = 1
        if k == 0:
            for l in pairs:
                pairs[l] = pairs[l] / (len(seq) - 1)
        elif k == 1:
            for l in pairs:
                pairs[l] = pairs[l] / (len(seq) - 2)
        elif k == 2:
            for l in pairs:
                pairs[l] = pairs[l] / (len(seq) - 3)
        elif k == 3:
            for l in pairs:
                pairs[l] = pairs[l] / (len(seq) - 4)

        object_data.extend([pairs[pair] for _ in range(1) for pair in pairs])
    total_data.append(object_data)

    data_row.extend(total_data[0])
    headers = [f"{pair}.gap{k}" for k in range(4) for pair in pairs]
    header_row.extend(headers)


def Composition(seq, data_row, header_row):
    Charge = []
    Charge.append(["K", "R"])
    Charge.append(
        ["A", "N", "C", "Q", "G", "H", "I", "L",
            "M", "F", "P", "S", "T", "W", "Y", "V"]
    )
    Charge.append(["D", "E"])

    Hydrophobicity_CASG920101 = []
    Hydrophobicity_CASG920101.append(
        ["K", "D", "E", "Q", "P", "S", "R", "N", "T", "G"])
    Hydrophobicity_CASG920101.append(["A", "H", "Y", "M", "L", "V"])
    Hydrophobicity_CASG920101.append(["F", "I", "W", "C"])

    Hydrophobicity_FASG890101 = []
    Hydrophobicity_FASG890101.append(["K", "E", "R", "S", "Q", "D"])
    Hydrophobicity_FASG890101.append(["N", "T", "P", "G"])
    Hydrophobicity_FASG890101.append(
        ["A", "Y", "H", "W", "V", "M", "F", "L", "I", "C"])

    NormalizedvanderWaalsvolume = []
    NormalizedvanderWaalsvolume.append(["G", "A", "S", "T", "P", "D", "C"])
    NormalizedvanderWaalsvolume.append(["N", "V", "E", "Q", "I", "L"])
    NormalizedvanderWaalsvolume.append(["M", "H", "K", "F", "R", "Y", "W"])

    Polarity = []
    Polarity.append(["L", "I", "F", "W", "C", "M", "V", "Y"])
    Polarity.append(["P", "A", "T", "G", "S"])
    Polarity.append(["H", "Q", "R", "K", "N", "E", "D"])

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
    Solventaccessibility.append(["R", "K", "Q", "E", "N", "D"])
    Solventaccessibility.append(["M", "P", "S", "T", "H", "Y"])

    properties = {
        "hydrophobicity_CASG920101": Hydrophobicity_CASG920101,
        "hydrophobicity_FASG890101": Hydrophobicity_FASG890101,
        "normwaalsvolume": NormalizedvanderWaalsvolume,
        "polarity": Polarity,
        "polarizability": Polarizability,
        "charge": Charge,
        "secondarystruct": Secondarystructure,
        "solventaccess": Solventaccessibility,
    }

    for property_name, property_values in properties.items():
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

    header = []
    for property_name, property_values in properties.items():
        for group_num, group in enumerate(property_values, start=1):
            header.append(f"{property_name}.G{group_num}")
    header_row.extend(header)

    data = []
    for property_name, property_values in properties.items():
        for group in property_values:
            group_freq = sum(char in group for char in seq) / len(seq)
            data.append(group_freq)
    data_row.extend(data)


def Transition(seq, data_row, header_row):
    Charge = []
    Charge.append(["K", "R"])
    Charge.append(
        ["A", "N", "C", "Q", "G", "H", "I", "L",
            "M", "F", "P", "S", "T", "W", "Y", "V"]
    )
    Charge.append(["D", "E"])

    Hydrophobicity_CASG920101 = []
    Hydrophobicity_CASG920101.append(
        ["K", "D", "E", "Q", "P", "S", "R", "N", "T", "G"])
    Hydrophobicity_CASG920101.append(["A", "H", "Y", "M", "L", "V"])
    Hydrophobicity_CASG920101.append(["F", "I", "W", "C"])

    Hydrophobicity_FASG890101 = []
    Hydrophobicity_FASG890101.append(["K", "E", "R", "S", "Q", "D"])
    Hydrophobicity_FASG890101.append(["N", "T", "P", "G"])
    Hydrophobicity_FASG890101.append(
        ["A", "Y", "H", "W", "V", "M", "F", "L", "I", "C"])

    NormalizedvanderWaalsvolume = []
    NormalizedvanderWaalsvolume.append(["G", "A", "S", "T", "P", "D", "C"])
    NormalizedvanderWaalsvolume.append(["N", "V", "E", "Q", "I", "L"])
    NormalizedvanderWaalsvolume.append(["M", "H", "K", "F", "R", "Y", "W"])

    Polarity = []
    Polarity.append(["L", "I", "F", "W", "C", "M", "V", "Y"])
    Polarity.append(["P", "A", "T", "G", "S"])
    Polarity.append(["H", "Q", "R", "K", "N", "E", "D"])

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
    Solventaccessibility.append(["R", "K", "Q", "E", "N", "D"])
    Solventaccessibility.append(["M", "P", "S", "T", "H", "Y"])

    properties = {
        "hydrophobicity_CASG920101": Hydrophobicity_CASG920101,
        "hydrophobicity_FASG890101": Hydrophobicity_FASG890101,
        "normwaalsvolume": NormalizedvanderWaalsvolume,
        "polarity": Polarity,
        "polarizability": Polarizability,
        "charge": Charge,
        "secondarystruct": Secondarystructure,
        "solventaccess": Solventaccessibility,
    }

    result = []

    for property_name, property_groups in properties.items():
        prev_group = 0
        curr_group = 0

        freq_1221 = 0
        freq_1331 = 0
        freq_2332 = 0

        for letter in seq:
            for i, group in enumerate(property_groups):
                if letter in group:
                    curr_group = i + 1
                    break

            if (
                curr_group == 1
                and prev_group == 2
                or curr_group == 2
                and prev_group == 1
            ):
                freq_1221 += 1
            elif (
                curr_group == 1
                and prev_group == 3
                or curr_group == 3
                and prev_group == 1
            ):
                freq_1331 += 1
            elif (
                curr_group == 2
                and prev_group == 3
                or curr_group == 3
                and prev_group == 2
            ):
                freq_2332 += 1

            prev_group = curr_group

        result.append(freq_1221 / (len(seq) - 1))
        result.append(freq_1331 / (len(seq) - 1))
        result.append(freq_2332 / (len(seq) - 1))

    name = ["1221", "1331", "2332"]
    header = []
    for property_name, property_values in properties.items():
        for group_num, group in enumerate(property_values, start=1):
            header.append(f"{property_name}.Tr{name[group_num-1]}")

    header_row.extend(header)
    data_row.extend(result)


def Distribution(seq, data_row, header_row):
    Charge = []
    Charge.append(["K", "R"])
    Charge.append(
        ["A", "N", "C", "Q", "G", "H", "I", "L",
            "M", "F", "P", "S", "T", "W", "Y", "V"]
    )
    Charge.append(["D", "E"])

    Hydrophobicity_CASG920101 = []
    Hydrophobicity_CASG920101.append(
        ["K", "D", "E", "Q", "P", "S", "R", "N", "T", "G"])
    Hydrophobicity_CASG920101.append(["A", "H", "Y", "M", "L", "V"])
    Hydrophobicity_CASG920101.append(["F", "I", "W", "C"])

    Hydrophobicity_FASG890101 = []
    Hydrophobicity_FASG890101.append(["K", "E", "R", "S", "Q", "D"])
    Hydrophobicity_FASG890101.append(["N", "T", "P", "G"])
    Hydrophobicity_FASG890101.append(
        ["A", "Y", "H", "W", "V", "M", "F", "L", "I", "C"])

    NormalizedvanderWaalsvolume = []
    NormalizedvanderWaalsvolume.append(["G", "A", "S", "T", "P", "D", "C"])
    NormalizedvanderWaalsvolume.append(["N", "V", "E", "Q", "I", "L"])
    NormalizedvanderWaalsvolume.append(["M", "H", "K", "F", "R", "Y", "W"])

    Polarity = []
    Polarity.append(["L", "I", "F", "W", "C", "M", "V", "Y"])
    Polarity.append(["P", "A", "T", "G", "S"])
    Polarity.append(["H", "Q", "R", "K", "N", "E", "D"])

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
    Solventaccessibility.append(["R", "K", "Q", "E", "N", "D"])
    Solventaccessibility.append(["M", "P", "S", "T", "H", "Y"])

    properties = {
        "hydrophobicity_CASG920101": Hydrophobicity_CASG920101,
        "hydrophobicity_FASG890101": Hydrophobicity_FASG890101,
        "normwaalsvolume": NormalizedvanderWaalsvolume,
        "polarity": Polarity,
        "polarizability": Polarizability,
        "charge": Charge,
        "secondarystruct": Secondarystructure,
        "solventaccess": Solventaccessibility,
    }

    header = []
    for property_name, property_values in properties.items():
        for group_num, group in enumerate(property_values, start=1):
            for res in range(0, 101, 25):
                header.append(f"{property_name}.{group_num}.residue{res}")
    header_row.extend(header)

    data = []

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

        add = []
        while len(subarrays) < 3:
            subarrays.append(add)

        total_length = len(seq)

        for group_num, subarray in enumerate(subarrays):
            if subarray:
                if len(subarray) % 2 == 0:
                    res_0 = subarray[0] / total_length * 100
                    if len(subarray) < 4:
                        res_25 = (
                            subarray[math.floor(
                                len(subarray) / 4)] / total_length * 100
                        )
                    else:
                        res_25 = (
                            subarray[math.floor((len(subarray)) / 4) - 1]
                            / total_length
                            * 100
                        )
                    res_50 = (
                        subarray[math.floor(
                            len(subarray) / 2) - 1] / total_length * 100
                    )
                    res_75 = (
                        subarray[math.floor((len(subarray) - 1) * 3 / 4)]
                        / total_length
                        * 100
                    )
                    res_100 = subarray[len(subarray) - 1] / total_length * 100
                    data.extend([res_0, res_25, res_50, res_75, res_100])

                elif len(subarray) % 2 == 1:
                    res_0 = subarray[0] / total_length * 100
                    if len(subarray) < 4:
                        res_25 = (
                            subarray[math.floor(
                                len(subarray) / 4)] / total_length * 100
                        )
                    else:
                        res_25 = (
                            subarray[math.floor((len(subarray)) / 4) - 1]
                            / total_length
                            * 100
                        )
                    res_50 = (
                        subarray[math.floor(
                            len(subarray) / 2) - 1] / total_length * 100
                    )
                    res_75 = (
                        subarray[math.floor(len(subarray) * 3 / 4) - 1]
                        / total_length
                        * 100
                    )
                    res_100 = subarray[len(subarray) - 1] / total_length * 100
                    data.extend([res_0, res_25, res_50, res_75, res_100])
            else:
                data.extend([0] * 5)
    data_row.extend(data)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/process", methods=["POST"])
def process():
    all_sequences = []
    all_probabilities = []
    all_labels = []
    error_messages = []
    fasta_sequence = request.form["sequence"]
    selected_functions = [
        "AAC",
        "EAAC",
        "CKSAAP",
        "Distribution",
        "Transition",
        "Composition",
    ]

    # Check if the sequence is in FASTA format
    if not fasta_sequence.startswith(">"):
        error_messages.append("Invalid format please enter a FASTA sequence")
        return render_template("index.html", error_message=error_messages)

    fasta_entries = fasta_sequence.strip().split("\n>")

    header_row = []
    data_rows = []

    for entry in fasta_entries:
        lines = entry.strip().split("\n")
        description = lines[0].lstrip(">")
        sequence = "".join(lines[1:])
        all_sequences.append(sequence)

        if len(sequence) < 5:
            error_messages.append(
                "Invalid sequence length. Please enter a sequence of length greater than 5"
            )
            return render_template("index.html", error_message=error_messages)

        data_row = []

        if "AAC" in selected_functions:
            try:
                AAC(sequence, data_row, header_row)
            except ValueError as e:
                error_messages.append(str(e))

        if "EAAC" in selected_functions:
            try:
                EAAC(sequence, data_row, header_row)
            except ValueError as e:
                error_messages.append(str(e))

        if "CKSAAP" in selected_functions:
            try:
                CKSAAP(sequence, data_row, header_row)
            except ValueError as e:
                error_messages.append(str(e))

        if "Distribution" in selected_functions:
            try:
                Distribution(sequence, data_row, header_row)
            except ValueError as e:
                error_messages.append(str(e))

        if "Transition" in selected_functions:
            try:
                Transition(sequence, data_row, header_row)
            except ValueError as e:
                error_messages.append(str(e))

        if "Composition" in selected_functions:
            try:
                Composition(sequence, data_row, header_row)
            except ValueError as e:
                error_messages.append(str(e))

        data_rows.append(data_row)

    if len(error_messages) > 0:
        return render_template("index.html", error_message=error_messages)

    max_columns = 2429
    header_row = header_row[:max_columns]
    data_rows = [row[:max_columns] for row in data_rows]

    timestamp = time.strftime("%d_%m_%Y_%H_%M_%S")
    filename = f"Web Server/files/output_{timestamp}.csv"

    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)

        if csvfile.tell() == 0:
            writer.writerow(header_row)

        writer.writerows(data_rows)

    file = f"Web Server/files/output_{timestamp}.csv"

    df = pd.read_csv(file)
    specific_columns = df[column_names]

    data = specific_columns.values.tolist()

    with open(file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        file_content = list(reader)

    for i in data:
        result = model.predict_proba([i])
        probability = round(result[0][1], 3)
        all_probabilities.append(probability)
        all_labels.append("AHCP")
        all_labels.append(model.predict([i])[0])

    return render_template(
        "thank.html",
        file_content=file_content,
        prob=all_probabilities,
        filename=file,
        Sequence=all_sequences,
        length=len(all_sequences),
        labels=all_labels,
    )



@app.route("/getcsv/Web Server/files/<filename>", methods=["GET"])
def getcsv(filename):
    file = f"files/{filename}"
    return send_file(file, as_attachment=True)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=3000)
