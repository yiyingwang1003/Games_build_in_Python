from file_update import fileUpdate


def test_constructor():
    fu = fileUpdate("scores.txt")
    assert fu.file_name == "scores.txt"


def test_read_file(tmpdir):
    file = tmpdir.join("scores.txt")
    file.write("Mike 15\n")
    file.write("EE 10\n", mode='a')
    fu = fileUpdate(file)
    fu.read_file()
    assert fu.scores == [['Mike', 15], ['EE', 10]]


def test_update_file(tmpdir):
    file = tmpdir.join("scores.txt")
    file.write("Mike 15\n")
    file.write("EE 10\n", mode='a')
    fu = fileUpdate(file)
    fu.update_file("Bento", 16)
    assert fu.scores == [['Bento', 16], ['Mike', 15], ['EE', 10]]
    fu.update_file("Bento W", 15)
    assert fu.scores == [['Bento', 16], ['Mike', 15], ['EE', 10],
                         ['Bento W', 15]]
