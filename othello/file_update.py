DATA_COL_NUM = 2
ONE = 1
ZERO = 0
DEFAULT_VAL = 0


class fileUpdate:
    def __init__(self, file_name):
        self.file_name = file_name
        self.read_file()

    def read_file(self):
        """Read the file"""
        try:
            opened_file = open(self.file_name, "r")
        except FileNotFoundError:
            print("Unable to open", self.file_name)
            return

        raw_data = []
        for line in opened_file:
            raw_data.append(line.rstrip())

        opened_file.close()

        self.scores = [[DEFAULT_VAL for _ in range(DATA_COL_NUM)]
                       for _ in range(len(raw_data))]

        i = DEFAULT_VAL
        for data in raw_data:
            temp = data.rsplit(" ", ONE)
            self.scores[i][ZERO] = temp[ZERO]
            self.scores[i][ONE] = int(temp[ONE])
            i += ONE

    def update_file(self, new_player, new_score):
        """Updates the file"""
        try:
            opened_file = open(self.file_name, "w")
        except FileNotFoundError:
            print("Unable to open", self.file_name)
            return

        if self.scores:
            if new_score >= self.scores[ZERO][ONE]:
                self.scores.insert(ZERO, [new_player, new_score])
            else:
                self.scores.append([new_player, new_score])
        else:
            self.scores.append([new_player, new_score])

        for i in range(len(self.scores)):
            opened_file.write(self.scores[i][ZERO])
            opened_file.write(" ")
            opened_file.write(str(self.scores[i][ONE]))
            opened_file.write("\n")

        opened_file.close()
