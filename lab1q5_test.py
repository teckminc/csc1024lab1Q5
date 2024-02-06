import lab1q5
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('9435\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1q5.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'02:37:15') != -1

def test_case2(monkeypatch, capsys):
    number_inputs = StringIO('9630\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1q5.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'02:40:30') != -1
