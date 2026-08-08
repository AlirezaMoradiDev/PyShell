from pathlib import Path
import head

def test_main(monkeypatch, capsys):

    input_file = Path("test.txt")

    monkeypatch.setattr(
        head, 
        "argv",
        ["head.py", str(input_file), '-n', 1]
    )

    head.main()

    captured = capsys.readouterr()

    assert captured.out == "line--> 1: hello \n\n"