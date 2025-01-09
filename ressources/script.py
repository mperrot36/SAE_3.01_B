import json

with open("machines.json", "r") as file:
    data = json.load(file)

for attribute, _ in data.items():
    match attribute:
        # case "aux":
        #     print("AUX - RDSI")
        #     print(
        #         "TU A BESOIN D'AVOIR LYNX D'INSTALLER LYNX SUR LA MACHINE AVEC LA COMMANDE : apt update && apt install lynx -y"
        #     )
        #     try:
        #         print("lynx google.fr -> doit pas fonctionner")
        #         print("nc -ltnvp 2302 -> sur la machine mail")
        #         print('echo "test" | nc ' +
        #               data["mail"] + " 2302 -> doit fonctionner")
        #         print("nc -ltnvp 2302 -> sur la machine s")
        #         print("nc -ltnvp 2302 -> sur la machine bdd")
        #         print('echo "test" | nc ' +
        #               data["bdd"] + " 2302 -> doit fonctionner")
        #     except KeyError as _:
        #         print("mail ou bdd ou s ne sont pas rentrer correctement: KeyError")
        # case "bdd":
        #     print("\nBDD - RDSI")
        #     print(
        #         "TU A BESOIN D'AVOIR LYNX D'INSTALLER LYNX SUR LA MACHINE AVEC LA COMMANDE : apt update && apt install lynx -y"
        #     )
        #     try:
        #         print("lynx google.fr -> doit pas fonctionner")
        #         print("nc -ltnvp 22 -> sur la machine aux")
        #         print('echo "test" | nc ' +
        #               data["aux"] + " 22 -> doit pas fonctionner")
        #         print("nc -ltnvp 22 -> sur la machine pcrssi")
        #         print(
        #             'echo "test" | nc ' +
        #             data["pcrssi"] + " 22 -> doit pas fonctionner"
        #         )
        #         print("nc -ltnvp 22 -> sur la machine pcche")
        #         print(
        #             'echo "test" | nc ' +
        #             data["pcche"] + " 22 -> doit pas fonctionner"
        #         )
        #         print("nc -ltnvp 22 -> sur la machine pcec")
        #         print(
        #             'echo "test" | nc ' +
        #             data["pcec"] + " 22 -> doit pas fonctionner"
        #         )
        #     except KeyError as _:
        #         print(
        #             "pcrssi ou pcche ou pcec ou aux ne sont pas rentrer correctement: KeyError"
        #         )
        # case "dns":
        #     print("\nDNS - RDSI")
        #     print(
        #         "TU A BESOIN D'AVOIR LYNX D'INSTALLER LYNX SUR LA MACHINE AVEC LA COMMANDE : apt update && apt install lynx -y"
        #     )
        #     try:
        #         print("lynx google.fr -> doit pas fonctionner")
        #         print("ping " + data["pcrssi"] + " -> doit pas fonctionner")
        #     except KeyError as _:
        #         print("pcrssi ne sont pas rentrer correctement: KeyError")
        case "mail":
            print("\nMAIL - RDSI")
            print(
                "TU A BESOIN D'AVOIR LYNX D'INSTALLER LYNX SUR LA MACHINE AVEC LA COMMANDE : apt update && apt install lynx -y"
            )
            try:
                print("lynx google.fr -> doit pas fonctionner")
                print("nc -ltnvp 4567")
                # print('echo "test" | nc ' +
                #       data["mail"] + " 4567 -> sur la machine pcetu, doit fontctionner")
                # print('echo "test" | nc ' +
                #       data["mail"] + " 4567 -> sur la machine pcs, doit fonctionner")
                print('echo "test" | nc ' +
                      data["mail"] + " 4567 -> sur la machine pcens, doit fonctionner")
                # print('echo "test" | nc ' +
                #       data["mail"] + " 4567 -> sur la machine pcc, doit fonctionner")
                # print('echo "test" | nc ' +
                #       data["mail"] + " 4567 -> sur la machine s, doit pas fonctionner")
                # print(
                #     'echo "test" | nc ' + data["mail"] +
                #     " 4567 -> sur la machine pcp, doit pas fonctionner"
                # )
                # print(
                #     'echo "test" | nc ' + data["mail"] +
                #     " 4567 -> sur la machine pcv, doit pas fonctionner"
                # )
                print('echo "test" | nc ' +
                      data["mail"] + " 4567 -> sur la machine pcec, doit fonctionner")
                print('echo "test" | nc ' +
                      data["mail"] + " 4567 -> sur la machine pcche, doit fonctionner")
                print('echo "test" | nc ' +
                      data["mail"] + " 4567 -> sur la machine pcdsi, doit fonctionner")
                # print('echo "test" | nc ' +
                #       data["mail"] + " 4567 -> sur la machine pcrssi, doit fonctionner")
            except KeyError as _:
                print(
                    "huh: KeyError"
                )
        case "pcc":
            print("\nPCC - RCOMPTA")
            print(
                "TU A BESOIN D'AVOIR LYNX D'INSTALLER LYNX SUR LA MACHINE AVEC LA COMMANDE : apt update && apt install lynx -y"
            )
            try:
                print("lynx google.fr -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine mail")
                print('echo "test" | nc ' +
                      data["mail"] + " 4567 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 80 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 443 -> doit fonctionner")
                print("nc -ltnvp 1224 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 1224 -> doit fonctionner")
            except KeyError as _:
                print("mail ou s ne sont pas rentrer correctement: KeyError")
        case "pcche":
            print("\nPCCHE - RCHERCHEUR")
            print(
                "TU A BESOIN D'AVOIR LYNX D'INSTALLER LYNX SUR LA MACHINE AVEC LA COMMANDE : apt update && apt install lynx -y"
            )
            try:
                print("lynx google.fr -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine mail")
                print('echo "test" | nc ' +
                      data["mail"] + " 4567 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 80 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 443 -> doit fonctionner")
                print("nc -ltnvp 1224 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 1224 -> doit pas fonctionner")
                print("nc -ltnvp 22 -> sur la machine bdd")
                print('echo "test" | nc ' +
                      data["bdd"] + " 22 -> doit fonctionner")
            except KeyError() as _:
                print("mail ou s ou bdd ne sont pas rentrer correctement: KeyError")
        case "pcdsi":
            print("\nPCDSI - RDSI")
            print(
                "TU A BESOIN D'AVOIR LYNX D'INSTALLER LYNX SUR LA MACHINE AVEC LA COMMANDE : apt update && apt install lynx -y"
            )
            try:
                print("lynx google.fr -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine mail")
                print('echo "test" | nc ' +
                      data["mail"] + " 4567 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 80 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 443 -> doit fonctionner")
                print("nc -ltnvp 1224 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 1224 -> doit fonctionner")
                print("nc -ltnvp 22 -> sur la machine bdd")
                print('echo "test" | nc ' +
                      data["bdd"] + " 22 -> doit pas fonctionner")
            except KeyError() as _:
                print("mail ou s ou bdd ne sont pas rentrer correctement: KeyError")
        case "pcec":
            print("\nPCEC - REC")
            print(
                "TU A BESOIN D'AVOIR LYNX D'INSTALLER LYNX SUR LA MACHINE AVEC LA COMMANDE : apt update && apt install lynx -y"
            )
            try:
                print("lynx google.fr -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine mail")
                print('echo "test" | nc ' +
                      data["mail"] + " 4567 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 80 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 443 -> doit fonctionner")
                print("nc -ltnvp 1224 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 1224 -> doit pas fonctionner")
                print("nc -ltnvp 22 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 22 -> doit fonctionner")
                print("nc -ltnvp 3306 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 3306 -> doit fonctionner")
            except KeyError() as _:
                print("mail ou s ou bdd ne sont pas rentrer correctement: KeyError")
        case "pcetu":
            print("\nPCETU - RETUDIANTS")
            print(
                "TU A BESOIN D'AVOIR LYNX D'INSTALLER LYNX SUR LA MACHINE AVEC LA COMMANDE : apt update && apt install lynx -y"
            )
            try:
                print("lynx google.fr -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine mail")
                print('echo "test" | nc ' +
                      data["mail"] + " 4567 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 80 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 443 -> doit fonctionner")
                print("nc -ltnvp 1224 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 1224 -> doit pas fonctionner")
            except KeyError() as _:
                print("mail ou s ne sont pas rentrer correctement: KeyError")
        case "pcp":
            print("\nPCP - RPATIENTS")
            print(
                "TU A BESOIN D'AVOIR LYNX D'INSTALLER LYNX SUR LA MACHINE AVEC LA COMMANDE : apt update && apt install lynx -y"
            )
            try:
                print("lynx google.fr -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 80 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 443 -> doit fonctionner")
            except KeyError() as _:
                print("s n'est pas rentrer correctement: KeyError")
        case "pcrssi":
            print("\nPCDRSSI - RDSI")
            print(
                "TU A BESOIN D'AVOIR LYNX D'INSTALLER LYNX SUR LA MACHINE AVEC LA COMMANDE : apt update && apt install lynx -y"
            )
            try:
                print("lynx google.fr -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine mail")
                print('echo "test" | nc ' +
                      data["mail"] + " 4567 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 80 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 443 -> doit fonctionner")
                print("nc -ltnvp 1224 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 1224 -> doit fonctionner")
                print("nc -ltnvp 22 -> sur la machine bdd")
                print('echo "test" | nc ' +
                      data["bdd"] + " 22 -> doit fonctionner")
            except KeyError() as _:
                print("mail ou s ou bdd ne sont pas rentrer correctement: KeyError")
        case "pcs":
            print("\nPCS - RSOIGNANTS")
            print(
                "TU A BESOIN D'AVOIR LYNX D'INSTALLER LYNX SUR LA MACHINE AVEC LA COMMANDE : apt update && apt install lynx -y"
            )
            try:
                print("lynx google.fr -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine mail")
                print('echo "test" | nc ' +
                      data["mail"] + " 4567 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 80 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 443 -> doit fonctionner")
                print("nc -ltnvp 1224 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 1224 -> doit fonctionner")
            except KeyError as _:
                print("mail ou s ne sont pas rentrer correctement: KeyError")
        case "pcv":
            print("\nPCV - RVISITEURS")
            print(
                "TU A BESOIN D'AVOIR LYNX D'INSTALLER LYNX SUR LA MACHINE AVEC LA COMMANDE : apt update && apt install lynx -y"
            )
            try:
                print("lynx google.fr -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 80 -> doit fonctionner")
                print("nc -ltnvp 4567 -> sur la machine s")
                print('echo "test" | nc ' +
                      data["s"] + " 443 -> doit fonctionner")
            except KeyError() as _:
                print("s n'est pas rentrer correctement: KeyError")
        case "s":
            print("\nS - RS")
            print(
                "TU A BESOIN D'AVOIR LYNX D'INSTALLER LYNX SUR LA MACHINE AVEC LA COMMANDE : apt update && apt install lynx -y"
            )
            try:
                print("lynx google.fr -> doit fonctionner")
                print("nc -ltnvp 3306 -> sur la machine bdd")
                print('echo "test" | nc ' +
                      data["s"] + " 3306 -> doit fonctionner")
            except KeyError() as _:
                print("bdd n'est pas rentrer correctement: KeyError")
